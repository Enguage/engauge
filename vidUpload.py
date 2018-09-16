########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

import cognitive_face as CF
import cv2
import os


key = '9f23d33e86a24404b089d5a02ed69090'
CF.Key.set(key)

#prints the key
print(key)

base_url = 'https://westus2.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(base_url)

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


# face.detect method can take image files of .jpg, .png, or .bmp

path, dirs, files = next(os.walk("frames"))
file_count = len(files)
print(file_count)

for i in range(file_count):
    if (i % 30 == 0):
        result = CF.face.detect(('frames/frame%d.jpg' % i), attributes='emotion')
        results.append(result)

print(results)


# will return array of "face" objects with faceAttributes property that contains emotion property

# https://github.com/Microsoft/Cognitive-Face-Python/blob/master/cognitive_face/face.py




