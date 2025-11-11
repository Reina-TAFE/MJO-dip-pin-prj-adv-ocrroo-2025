import requests

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
#NOTE: flask run --port 8001

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-transcript/")
def get_transcript():

    frame_number = request.args.get("video_pos")

    url = f"http://127.0.0.1:8000/video/demo/frame/{frame_number}/ocr"
    response = requests.get(url).content

    response = response.decode(encoding='utf-8')

    print(response)

    #TODO replace with redirect
    return render_template("index.html", transcript=response)


