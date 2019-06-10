#!/usr/bin/env python3
# import cognitive_face as CF

# KEY = '3bc276f0180f4bb1865f448f767fdc72'  # Replace with a valid subscription key (keeping the quotes in place).
# CF.Key.set(KEY)

# BASE_URL = 'https://westus2.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
# CF.BaseUrl.set(BASE_URL)
# # You can use this example JPG or replace the URL below with your own URL to a JPEG image.
# img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
# faces = CF.face.detect(img_url)
# print(faces)
import requests
import json as simplejson
from picamera import PiCamera
from time import sleep
import operator
#import cognitive_face as cf
#import httplib, urllib



def get_current_mood():
    while(1):
        startCamera()
        image_url = 'image.jpg'
        subscription_key = '3bc276f0180f4bb1865f448f767fdc72'
        assert subscription_key
        
        face_api_url = 'https://westus2.api.cognitive.microsoft.com/face/v1.0/detect'
     
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'smile,glasses,emotion,occlusion,accessories,exposure,noise'
        }
        
        if "https" in image_url:
            headers = { 'Ocp-Apim-Subscription-Key': subscription_key}
            response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
        else:
            image_data = open(image_url, "rb").read()
            headers = {'Ocp-Apim-Subscription-Key': subscription_key,
                                    'Content-Type': 'application/octet-stream'}
      
            response = requests.post(face_api_url, params=params, headers=headers, data = image_data)
            
        response = response.json()
        mood = open("mood.txt", "w")
        if len(response) == 0:
            current_mood = 'neutral'
            mood.write(current_mood)
            # return "neutral"
        else:
            emotions = response[0]['faceAttributes']['emotion']
            current_mood = max(emotions.items(), key=operator.itemgetter(1))[0]
                
            print(current_mood)
            
            mood.write(current_mood)
        mood.close()
    #return current_mood

def startCamera():
    
    camera = PiCamera()
    camera.start_preview()
    sleep(1)
    camera.capture('image.jpg')
    camera.stop_preview()
    camera.close()
    print("Done!")
        

get_current_mood()




