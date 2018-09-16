import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

<<<<<<< HEAD
import cognitive_face as CF
import cv2
import os


key = '9f23d33e86a24404b089d5a02ed69090'
CF.Key.set(key)

#prints the key
print(key)

accountID = "e6dc5dac-de07-48a6-b157-91105accc78a"
accAccessToken = ""

# Sets our azure subscription key in the headers
headers1 = {
    'Ocp-Apim-Subscription-Key': '8dbcfd113c304bb4a6a31b8dcb715385'
}

def extractstt(data): # data a string of the json dictionary
    print("Extractstt start")


    part = json.loads(data)
    print(data)

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

    print("Extractstt end")
    pass


path, dirs, files = next(os.walk("frames"))
file_count = len(files)
print(file_count)

for i in range(file_count):
    if (i % 30 == 0):
        result = CF.face.detect(('frames/frame%d.jpg' % i), attributes='emotion')
        results.append(result)

print(results)


try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    conn.request("GET", "/auth/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/AccessToken?%s" % params, "{body}",
                 headers1)
    response = conn.getresponse()
    string = response.read().decode('utf-8') # want function to extract data from string
    speechtotext = extractstt(string)
    # json_obj = json.loads(string) # literally all our data is in string, json_obj loads prettily, supposedly
    # print(json_obj)
    # accAccessToken = json_obj
    # print data is the access token
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

# step 2 video access token using part 1

# CF.face.detect(<image_file>, attributes='emotion')


# will return array of "face" objects with faceAttributes property that contains emotion property

# https://github.com/Microsoft/Cognitive-Face-Python/blob/master/cognitive_face/face.py

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    conn.request("GET",
                 "/auth/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/Videos/b32f841588/AccessToken?%s" % params,
                 "{body}", headers2)
    response = conn.getresponse()
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    # print(json_obj)
    videoAccessToken = json_obj
    # print data is the access token
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

# step 3
headers3 = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '8dbcfd113c304bb4a6a31b8dcb715385',
}

params = urllib.parse.urlencode({
    # Request parameters
    'accessToken': accAccessToken,
    'language': 'English',
})


def parser(data):
    '''
    data is json obj
    '''
    data = json.loads(data)
    # data seems to be able to be keyed into twice as dictionary, then holds lists
    # data['summarizedInsights']['faces'] is a list of more dictionaries that hold all of the face information (id, appearances, etc)
    print(data['summarizedInsights']['faces'])


try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    conn.request("GET", "/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/Videos/b32f841588/Index?%s" % params,
                 "{body}", headers3)
    response = conn.getresponse()
    data = response.read()
    # thing that needs to be parsed 
    print('\n', data, '\n')
    # other possibility for parsing
    # data = str(data)
    parser(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))








    # headers2 = {
    #     # Request headers
    #     'Content-Type': 'multipart/form-data',
    #     'Ocp-Apim-Subscription-Key': '8dbcfd113c304bb4a6a31b8dcb715385'
    #
    # }
    #
    # params = urllib.parse.urlencode({
    #     # Request parameters
    #     # 'description': '{string}',
    #     # 'partition': '{string}',
    #     # 'externalId': '{string}',
    #     # 'callbackUrl': '{string}',
    #     # 'metadata': '{string}',
    #     # 'language': '{string}',
    #     # 'videoUrl': '{string}',
    #     # 'fileName': '{string}',
    #     # 'indexingPreset': '{string}',
    #     # 'streamingPreset': 'Default',
    #     # 'linguisticModelId': '{string}',
    #     # 'privacy': '{string}',
    #     'videoUrl': 'https://andrew.fi/timelapse.mp4',
    # })
    #
    #
    # try:
    #     conn = http.client.HTTPSConnection('api.videoindexer.ai')
    #     conn.request("POST", "/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/Videos?accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJBY2NvdW50SWQiOiJlNmRjNWRhYy1kZTA3LTQ4YTYtYjE1Ny05MTEwNWFjY2M3OGEiLCJBbGxvd0VkaXQiOiJUcnVlIiwiRXh0ZXJuYWxVc2VySWQiOiI0NjE0Q0IwODczNDI0NDRFQjQ0QTk5NTI1MTlDN0M4RSIsIlVzZXJUeXBlIjoiTWljcm9zb2Z0Q29ycEFhZCIsImlzcyI6Imh0dHBzOi8vd3VzMi52aWRlb2luZGV4ZXIuYWkvIiwiYXVkIjoiaHR0cHM6Ly93dXMyLnZpZGVvaW5kZXhlci5haS8iLCJleHAiOjE1MzcwNDQzOTcsIm5iZiI6MTUzNzA0MDQ5N30.9bRrGOqiv-vqDTHwkrTYYJ92ETc0MfKtaQt43JSaJik&name=hello&%s" % params, "{body}", headers)
    #     response = conn.getresponse()
    #     data = response.read()
    #     print(data)
    #     conn.close()
    # except Exception as e:
    #     print("[Errno {0}] {1}".format(e.errno, e.strerror))
    #
    # #ask azure what it wants
    #
    # params2 = urllib.parse.urlencode({
    #     'accessToken' = {}
    #     '' =
    # })
