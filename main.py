import os
import time
import uuid
import gradio as gr
import cv2
import pygame
from gtts import gTTS
from speech_to_text import record_audio, transcribe_with_groq
from ai_agent import ask_agent

# 🌐 Global variables
camera = None
is_running = False
last_frame = None
session_active = True  # ✅ Controls whether the chatbot is active

# 🔊 GTTS with pygame and temp file
def text_to_speech_with_gtts(text):
    filename = f"{uuid.uuid4().hex}.mp3"
    try:
        tts = gTTS(text)
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"❌ gTTS Playback Error: {e}")
    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception:
                pass

# 🎤 Voice Assistant Tick Function
def process_audio_and_chat(chat_history):
    global session_active
    if not session_active:
        return chat_history  # 🔇 Don't do anything if session is over

    try:
        record_audio("audio_question.wav")
        user_input = transcribe_with_groq("audio_question.wav")
        print(f"🗣️ You: {user_input}")

        if "goodbye" in user_input.lower():
            response = "👋 NEON: Goodbye!"
            text_to_speech_with_gtts(response)

            chat_history.append({"role": "user", "content": user_input})
            chat_history.append({"role": "assistant", "content": response})

            session_active = False  # ✅ Stop future ticks
            return chat_history

        response = ask_agent(user_input)
        print(f"🤖 NEON: {response}")
        text_to_speech_with_gtts(response)

        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": response})
        return chat_history

    except Exception as e:
        chat_history.append({"role": "assistant", "content": f"❌ Error: {e}"})
        return chat_history

# 📷 Webcam Functions
def initialize_camera():
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0)
        if camera.isOpened():
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            camera.set(cv2.CAP_PROP_FPS, 30)
            camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    return camera is not None and camera.isOpened()

def start_webcam():
    global is_running, last_frame
    is_running = True
    if not initialize_camera():
        return None
    ret, frame = camera.read()
    if ret and frame is not None:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        last_frame = frame
        return frame
    return last_frame

def stop_webcam():
    global is_running, camera
    is_running = False
    if camera is not None:
        camera.release()
        camera = None
    return None

def get_webcam_frame():
    global camera, is_running, last_frame
    if not is_running or camera is None:
        return last_frame
    if camera.get(cv2.CAP_PROP_BUFFERSIZE) > 1:
        for _ in range(int(camera.get(cv2.CAP_PROP_BUFFERSIZE)) - 1):
            camera.read()
    ret, frame = camera.read()
    if ret and frame is not None:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        last_frame = frame
        return frame
    return last_frame

# 🔁 Reset session when clearing chat
def clear_chat():
    global session_active
    session_active = True
    return []

# 🎛️ Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("<h1 style='color: orange; text-align: center; font-size: 4em;'> 🧑‍🚀 NEON – Your AI Assistant</h1>")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## Webcam Feed")
            with gr.Row():
                start_btn = gr.Button("Start Camera", variant="primary")
                stop_btn = gr.Button("Stop Camera", variant="secondary")
            webcam_output = gr.Image(
                label="Live Feed",
                streaming=True,
                show_label=False,
                width=640,
                height=480
            )
            webcam_timer = gr.Timer(0.033)

        with gr.Column(scale=1):
            gr.Markdown("## Chat Interface")
            chatbot = gr.Chatbot(label="Conversation", height=400, show_label=False, type='messages')
            gr.Markdown("*🎤 Continuous listening mode is active — speak anytime!*")
            with gr.Row():
                clear_btn = gr.Button("Clear Chat", variant="secondary")

    # ⛓️ Bind buttons
    start_btn.click(fn=start_webcam, outputs=webcam_output)
    stop_btn.click(fn=stop_webcam, outputs=webcam_output)
    webcam_timer.tick(fn=get_webcam_frame, outputs=webcam_output, show_progress=False)
    clear_btn.click(fn=clear_chat, outputs=chatbot)

    # ⏱️ Chat loop
    chat_timer = gr.Timer(6)
    chat_timer.tick(fn=process_audio_and_chat, inputs=[chatbot], outputs=[chatbot])

# 🚀 Launch
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        debug=True
    )
