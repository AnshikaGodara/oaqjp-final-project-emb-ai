"""
Flask server for Emotion Detection application.

This module deploys the emotion detection functionality as a web
application using Flask. It provides routes for rendering the homepage
and analyzing emotions from user-provided text.
"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the homepage of the Emotion Detection application.

    Returns:
        HTML template for the main page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Analyze the emotion of the provided text.

    Returns:
        JSON response containing emotion scores and dominant emotion,
        or an error message if the input text is invalid.
    """
    text_to_analyse = request.form["text"]
    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
