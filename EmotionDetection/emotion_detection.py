import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    InputJSON= { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, headers=headers, json = InputJSON)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    #converting response text to dictionary
    response_dict = json.loads(response.text)
    #emotion scores:
    emotions = response_dict['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    #dominant emotion
    emotion_scores = {'anger':anger,
        'disgust':disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness    }  
    dominant_emotion = max(emotion_scores, key = emotion_scores.get)

    return {
        'angers': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }