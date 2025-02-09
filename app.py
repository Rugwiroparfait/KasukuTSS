from flask import Flask, request, send_file, render_template
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/app')
def index():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def text_to_speech():
    text = request.form.get('text')
    if not text:
        return "No text provided", 400

    # Convert text to speech
    tts = gTTS(text, lang="en")
    filename = "output.mp3"
    tts.save(filename)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

