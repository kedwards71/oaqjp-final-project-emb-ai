"""
Executing this function initiates the Emotion Detection application
on the Flask Channel and deployed on localhost:5000
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route('/emotionDetector')
def sent_emotion():
    """
    This method receives text from the HTML page
    runs it over the emotion_detector() method.
    The output is a series of scores associated with
    an emotion, and the dominant emotion based off those
    scores
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze and text_to_analyze!= '':
        analyzed_text = emotion_detector(text_to_analyze)
        response =(
            "For the given statement, the system response is "
            + f"'anger': {analyzed_text['anger']}, "
            + f"'disgust': {analyzed_text['disgust']}, "
            + f"'fear': {analyzed_text['fear']}, "
            + f"'joy': {analyzed_text['joy']}, "
            + f"'sadness': {analyzed_text['sadness']}. "
            + f"The dominant emotion is <b>{analyzed_text['dominant_emotion']}</b>.")
        return response
    else:
        return "Please enter a valid input!"



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)