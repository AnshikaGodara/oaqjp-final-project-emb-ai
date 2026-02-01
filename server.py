from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotionDetector():
    text_to_analyse = request.form["text"]
    result = emotion_detector(text_to_analyse)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)