import requests

from flask import Flask
from flask import render_template, redirect
from flask import request, url_for

app = Flask(__name__)

# NOTE: flask run --port 8001 --debug

@app.route("/")
def index():
    transcript = request.args.get("transcript")

    print(transcript)

    if transcript:
        return render_template("index.html", transcript=transcript)
    else:
        return render_template("index.html")


@app.route("/generate-transcript", methods=["POST"])
def get_transcript():
    video_position = request.form['video_pos']

    url = f"http://127.0.0.1:8000/video/demo/frame/{video_position}/ocr"
    response = requests.get(url).content

    response = response.decode(encoding='utf-8')

    return redirect(url_for('index', transcript=response))
