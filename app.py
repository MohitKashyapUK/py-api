from flask import Flask
from html import escape

app = Flask(__name__)

@app.route("/")
def index():
    return """<b>/frame</b>: Returns a frame from a video URL by given timestamp."""

@app.route("/frame")
def frame():
    return f"<h1>/ frame / {escape('<ISO timestamp (DD:HH:MM:SS)>')} / {escape('<video URL>')}</h1>"