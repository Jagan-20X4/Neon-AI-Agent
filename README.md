🧑‍🚀 NEON – AI Assistant
NEON is an interactive AI voice assistant built using Python, Gradio, OpenCV, and gTTS, designed to work with voice commands, live webcam feed, and real-time responses via a browser-based interface.

graph TD
A[🎤 User Speaks] --> B[🎙️ record_audio()]
B --> C[🧠 transcribe_with_groq()]
C --> D[📨 ask_agent()]
D --> E[🧾 Response Text]
E --> F[🔊 gTTS / ElevenLabs (TTS)]
F --> G[🎧 Playback with pygame]

🔧 Features
🎤 Real-time speech-to-text transcription using Groq
🤖 Conversational AI responses via Gemini or other language models
🔊 Text-to-speech responses using gTTS (fallback when ElevenLabs fails)
📷 Live webcam feed using OpenCV
🌐 Interactive Gradio-based UI
✅ Real-time status updates synced with backend terminal logs

⚙️ Tech Stack
Python
Gradio
OpenCV
gTTS / pygame
SoundDevice + SoundFile
Groq API (speech-to-text + LLM)
LangGraph 

⚙️ Installation Guide (Using uv)
uv is a superfast Python package manager that builds wheels and installs dependencies in seconds. It’s an alternative to pip and poetry.
Install uv if you haven’t already:

curl -LsSf https://astral.sh/uv/install.sh | sh

✅ Step-by-Step Setup
1. Clone the Repository
git clone https://github.com/yourusername/neon-ai-assistant.git
cd neon-ai-assistant

3. Create a Virtual Environment with uv
uv venv
source .venv/bin/activate  # Use `.venv\Scripts\activate` on Windows

5. Install All Required Packages
uv pip install -r requirements.txt

Or manually install core dependencies:
uv pip install gradio opencv-python gTTS pygame sounddevice soundfile

4. Install Optional Packages
These are used for LLM + agent support (you can skip if only using voice + webcam):
uv pip install langchain langgraph groq openai

6. Set Environment Variables
You can export them or store in a .env file:
export GROQ_API_KEY="your_groq_api_key"
export GOOGLE_API_KEY="your_google_gemini_key"

💡 Verify Installation
uv pip list

Make sure the following packages are listed:
gradio
opencv-python
gTTS
pygame
sounddevice
soundfile
langgraph, openai, groq 

🚀 Run 
