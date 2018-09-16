########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

import cognitive_face as CF

key = '8dbcfd113c304bb4a6a31b8dcb715385'
CF.Key.set(key)

print(key)

base_url = 'https://westus2.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(base_url)

# need to convert video to frames
# frame to .jpg format (if this isn't done already)
# face.detect method can take image files of .jpg, .png, or .bmp


# CF.face.detect(<image_file>, attributes='emotion')

# will return array of "face" objects with faceAttributes property that contains emotion property

# https://github.com/Microsoft/Cognitive-Face-Python/blob/master/cognitive_face/face.py
