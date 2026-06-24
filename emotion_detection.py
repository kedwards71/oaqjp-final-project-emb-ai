"""
The following module provides a function that reads a string
and Outputs the likelihood of an emotion based off the string
"""

# Import of the json library to help with formatting
import json
# Import of the requests library to handle HTTP requests
import requests


def emotion_detector(text_to_analyze):
    """
    Takes a string as input
    Outputs a responsed predicting likelihood of an emmotion
    """
    # Url of Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Header required for API service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Dictionary with the text_to_analyze
    myobj = {"raw_document":{"text":text_to_analyze}}
    # Post request to the API using heads and text
    response = requests.post(url=url,json=myobj,headers=header)
    # Response text from the URL
    return json.loads(response.text)
