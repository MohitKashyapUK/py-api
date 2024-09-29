from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """<b>/frame</b>: Returns a frame from a video URL by given timestamp."""