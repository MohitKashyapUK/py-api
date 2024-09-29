from flask import Flask, request, Response
from html import escape
from urllib.parse import urlencode
# import cv2

app = Flask(__name__)

def isoFormatToMS(duration):
    """
    Yah function ISO date ko milliseconds mein convert karta hai.

    Returns:
    - int:
        miliseconds
    """
    parts = duration.split(":")
    obj = [1, 60, 3600, 86400]
    seconds = 0

    parts.reverse()
    for index, value in enumerate(parts): seconds += int(value) * obj[index]
    return seconds * 1000

'''def get_frame(video_url, timestamp_ms):
    # Open the video stream
    cap = cv2.VideoCapture(video_url)

    # Check if the video stream is opened successfully
    if not cap.isOpened():
        print("Error: Could not open video stream")
        return

    # Set the video's position in milliseconds
    cap.set(cv2.CAP_PROP_POS_MSEC, timestamp_ms)

    # Read the frame at the specified timestamp
    ret, frame = cap.read()

    # Check if frame is read successfully
    if not ret:
        print("Error: Could not read frame at specified timestamp")
        return
    
    # Save the frame as an image file
    # cv2.imwrite(r"C:\Users\mohit\Desktop\yt_image.png", frame)
    _, buffer = cv2.imencode('.png', frame)
    image_data = buffer.tobytes()

    # Display the frame in a window
    # cv2.imshow("Frame at Timestamp", frame)
    # cv2.waitKey(0)

    # Release video stream and close OpenCV windows
    cap.release()
    # cv2.destroyAllWindows()

    return image_data'''

@app.route("/")
def index():
    return """<b>/frame</b>: Returns a frame from a video URL by given timestamp."""

@app.route("/frame")
def frame():
    return f"<h1>/ frame / {escape('<ISO timestamp (DD:HH:MM:SS)>')} / {escape('<video URL>')}</h1>"

'''@app.get("/frame/<timestamp>/<path:url>")
def get_frame(timestamp, url):
    args = urlencode(request.args)
    if args: url += "?" + args
    timestamp = isoFormatToMS(timestamp)
    image = get_frame(url, timestamp)
    return Response(image, mimetype='image/png')'''