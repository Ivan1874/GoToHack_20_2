import requests
from secure import face_key
import base64
import os

def ai(name):

    files = os.listdir(f'C:\\Users\\Александр\\PycharmProjects\\GoToHack_20_2\\tmp\\{name}')

    # set to your own subscription key value
    subscription_key = None

    # replace <My Endpoint String> with the string from your endpoint URL
    urls = []

    for file in files:
        with open(file, 'rb') as file:
            url = 'https://api.imgbb.com/1/upload'
            payload = {
                'key': 'bb5e187707a0da1d1caa826ebe9467ed',
                'image': base64.b64encode(file.read()),
            }
            res = requests.post(url, payload)

        urls.append(res['data']['url'])

    end = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    headers = {'Ocp-Apim-Subscription-Key': face_key}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    def givejson(photos):
        returnjson = {}
        for ph in photos:
            response = requests.post(end, params=params,
                                     headers=headers, json={"url": ph})
            resp = response.json()[0]
            predictedem = max(resp['faceAttributes']['emotion'].items(), key=lambda x: x[1])[0]
            if predictedem not in returnjson:
                returnjson[predictedem] = [predictedem]
            else:
                returnjson[predictedem].append(predictedem)
        return returnjson

    def crop_photo():
        pass

    givejson(urls)

