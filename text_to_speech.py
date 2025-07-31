import os
import platform
import subprocess
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath="final.mp3"):
    try:
        # 🎙️ Convert text to speech using gTTS
        tts = gTTS(text=input_text, lang='en')
        tts.save(output_filepath)

        # 🎯 Play audio in blocking mode
        os_name = platform.system()
        if os_name == "Windows":
            subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filepath],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os_name == "Darwin":  # macOS
            subprocess.run(["afplay", output_filepath])
        elif os_name == "Linux":
            subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filepath],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            raise OSError("Unsupported OS for audio playback.")

    except Exception as e:
        print(f"❌ gTTS or Playback Error: {e}")
