# KasukuTSS
# KasukuTSS 🎙️

KasukuTSS is a simple web-based Text-to-Speech (TTS) application that converts text input into an audio file (MP3). It uses Flask for the backend and gTTS (Google Text-to-Speech) to generate speech from text. The frontend allows users to enter text and play the generated audio.

## 🚀 Features
- Convert text into an MP3 file
- Simple and lightweight UI
- Free and open-source
- Deployable on free platforms like Render, Railway, and GitHub Pages

## 📌 Tech Stack
- **Backend:** Flask, gTTS
- **Frontend:** HTML, CSS, JavaScript
- **Hosting:** Render / Railway (Backend), GitHub Pages / Vercel (Frontend)

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/KasukuTSS.git
cd KasukuTSS
```

### 2️⃣ Install Dependencies
Make sure you have Python installed.
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Server
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`

## 🖥️ Usage
### API Endpoint: `POST /tts`
#### Request:
- **Form Data:** `text` (string) - The text to convert

#### Example (Using `curl`):
```bash
curl -X POST -F "text=Hello, KasukuTSS!" http://127.0.0.1:5000/tts --output output.mp3
```

#### Response:
- Returns an MP3 audio file.

## 🌍 Deployment
### Deploy Flask API (Backend)
#### Option 1: Deploy on Render
1. Push your code to GitHub
2. Go to [Render](https://render.com/)
3. Click **New Web Service** → Connect GitHub Repository
4. Set the **start command**:
   ```bash
   gunicorn app:app
   ```
5. Deploy 🎉

#### Option 2: Deploy on Railway
1. Go to [Railway](https://railway.app/)
2. Click **New Project** → Deploy from GitHub
3. Set **Start Command**: `gunicorn app:app`
4. Deploy 🎉

### Deploy Frontend (HTML, JS)
#### Option 1: GitHub Pages
1. Upload `index.html` to a GitHub repo
2. Enable **GitHub Pages** in repo settings
3. Your frontend will be live 🎉

#### Option 2: Vercel / Netlify
1. Push your frontend code to GitHub
2. Deploy using [Vercel](https://vercel.com/) or [Netlify](https://www.netlify.com/)

## 📜 License
KasukuTSS is open-source and available under the **MIT License**.

## 🙌 Contributing
Feel free to submit issues, feature requests, or pull requests to improve KasukuTSS!

## ⭐ Acknowledgments
- Powered by **Flask** & **gTTS**
- Inspired by the need for free and simple TTS tools

---
💡 **KasukuTSS** - Bringing text to life with speech! 🎤

