import http.client, urllib.request, urllib.parse, urllib.error, base64
import json


import cognitive_face as CF
import cv2
import os


# Sets our azure subscription key in the headers
headers1 = {
    'Ocp-Apim-Subscription-Key': 'e74bfd759b104d9b8503b05c0f66af1f'
}

# def extractstt(data): # data a string of the json dictionary
#     print("Extractstt start")
#     part = json.loads(data)
#     print(data)
#     print("Extractstt end")
#     pass
#


key = 'e74bfd759b104d9b8503b05c0f66af1f'
CF.Key.set(key)
#prints the key
print(key)

base_url = 'https://westus2.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(base_url)

accountID = "e6dc5dac-de07-48a6-b157-91105accc78a"
accAccessToken = ""



results = []

# need to convert video to frames
# frame to .jpg format (if this isn't done already)
# vidcap = cv2.VideoCapture('emotion.mp4')
# path = '/Users/ishanigos/PycharmProjects/enguage/engauge/frames'
# success,image = vidcap.read()
# count = 0
# while success:
#   cv2.imwrite(os.path.join(path, "frame%d.jpg" % count), image)     # save frame as JPEG file
#   success,image = vidcap.read()
#   print('Read a new frame: ', success)
#   count += 1




path, dirs, files = next(os.walk("frames"))
file_count = len(files)
print(file_count)

for i in range(file_count):
    if (i % 30 == 0):
        result = CF.face.detect(('frames/frame%d.jpg' % i), attributes='emotion')
        results.append(result)

print(results)

