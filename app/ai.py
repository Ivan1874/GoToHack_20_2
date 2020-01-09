import base64
import os
import random
import requests
import string

from PIL import Image

from secure import face_key


def ai(files, load_root, save_root):
    end = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    headers = {'Ocp-Apim-Subscription-Key': face_key}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    returnjson = {}
    for file in files:
        with open(os.path.join(load_root, file), 'rb') as f:
            payload = {
                'key': 'bb5e187707a0da1d1caa826ebe9467ed',
                'image': base64.b64encode(f.read()),
            }
        res = requests.post('https://api.imgbb.com/1/upload', payload)
        response = requests.post(end, params=params,
                                 headers=headers, json={"url": res.json()['data']['url']})
        resp = response.json()[0]
        cropped = Image.open(os.path.join(load_root, file)).crop((resp['faceRectangle']['left'], resp['faceRectangle']['top'],
                                         resp['faceRectangle']['left'] + resp['faceRectangle']['width'],
                                         resp['faceRectangle']['top'] + resp['faceRectangle']['height']))
        new_path = os.path.join(save_root, ''.join(random.choices(string.ascii_lowercase, k=10)) + '.jpg')
        cropped.save(new_path)

        predictedem = max(resp['faceAttributes']['emotion'].items(), key=lambda x: x[1])[0]
        if predictedem not in returnjson:
            returnjson[predictedem] = [os.path.basename(new_path)]
        else:
            returnjson[predictedem].append(os.path.basename(new_path))
    return returnjson
