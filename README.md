# 🧑‍🚀 NEON – AI Agent

**NEON** is your intelligent voice-based assistant built using **Python**, **Gradio**, **OpenCV**, and **gTTS**, enabling interactive conversations via microphone and webcam right in your browser.

> 🚀 Speak ➔ Understand ➔ Respond ➔ Speak back — all live!

---

## 🧠 System Architecture

```
flowchart TD
  A[User Speaks 🎤] --> B[record_audio() 🎙️]
  B --> C[transcribe_with_groq() 🧠]
  C --> D[ask_agent() 📨]
  D --> E[Generate Response 🔢]
  E --> F[gTTS 🔊]
  F --> G[Playback with pygame 🎧]
```

---

## 🔧 Features

* 🎤 **Real-time** speech-to-text transcription with **Groq**
* 🧠 AI conversation via **Gemini**, **Groq**, or other LLMs
* 🔊 Text-to-speech with **gTTS** 
* 📷 Live webcam video feed via **OpenCV**
* 🌐 Clean browser UI powered by **Gradio**
* 🧹 Real-time status synced with terminal logs (e.g., recording state)

---

## ⚙️ Tech Stack

| Layer           | Tools                                           |
| --------------- | ----------------------------------------------- |
| 🎤 Speech       | `gTTS`,  `pygame`                               |
| 🧠 Intelligence | `Groq`, `LangGraph`, `OpenAI`, `Gemini`         |
| 🖥 Interface    | `Gradio`, `OpenCV`, `Timer`, `Image`, `Chatbot` |
| 🎧 Audio I/O    | `sounddevice`, `soundfile`                      |
| ♻️ Management   | `uv` (package manager), `.env` config           |

---

## 📦 Installation (with `uv`)

> `uv` is a blazing fast Python package manager from Astral. It installs dependencies 8x faster than pip!

### 🔽️ 1. Install `uv` (if not already)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### 🛠️ 2. Setup NEON Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/neon-ai-assistant.git
cd neon-ai-assistant

# Create & activate virtual environment
uv venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

Or install manually:

```bash
uv pip install gradio opencv-python gTTS pygame sounddevice soundfile
```

---

### 📚 3. Optional: For AI Agent Support

```bash
uv pip install langchain langgraph groq openai
```

---

### 🔐 4. Environment Variables

You can set these in a `.env` file or in your terminal session:

```bash
export GROQ_API_KEY="your_groq_key"
export GOOGLE_API_KEY="your_google_gemini_key"
export ELEVENLABS_API_KEY="your_elevenlabs_key"
```

---

### ✅ 5. Verify Installation

```bash
uv pip list
```

Ensure the following packages are installed:

```
gradio
opencv-python
gTTS
pygame
sounddevice
soundfile
langgraph
groq
openai
```

---

## 🚀 Launch the App

```bash
python app.py
```

> The assistant will launch on: [http://localhost:7860](http://localhost:7860)<br>
> Speak to NEON. Get answers. Hear them out.

---

## 💬 Example Terminal Output

```
2025-07-31 01:41:30,833 - INFO - Adjusting for ambient noise...
2025-07-31 01:41:31,615 - INFO - Start speaking now...
2025-07-31 01:41:34,225 - INFO - Recording complete.
2025-07-31 01:41:34,752 - INFO - Audio saved to audio_question.wav
```


## 💪 Troubleshooting Tips

| Problem              | Solution                                       |
| -------------------- | ---------------------------------------------- |
| gTTS 503 error       | Retry after some time (Google TTS rate-limits) |
| Mic not detected     | Ensure microphone access is enabled            |
| Webcam not showing   | Restart the app or browser permission issue    |
| Audio playback fails | Try installing `ffmpeg` or use `pygame` TTS    |

---

## 🏋️ Contributing

Pull requests and feedback are welcome! Let’s make NEON better together ✨

