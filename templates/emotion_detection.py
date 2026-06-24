"""
The following module provides a function that grades speech
"""

# Import of the json library to help with formatting
import json
# Import of the requests library to handle HTTP requests
import requests 

def emotion_detector(text_to_analyze):
    """
    Takes a string as input
    """
    # Url of Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Header required for API service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Dictionary with the text_to_analyze
    myobj = {"raw_document":{"text":text_to_analyze}}
    # Post request to the API using heads and text
    response = requests.post(url=url,json=myobj,headers=header)
# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyze } }
