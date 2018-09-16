########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

accountID = "e6dc5dac-de07-48a6-b157-91105accc78a"
accAccessToken = ""
videoAccessToken = ""

#account token
headers1 = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '8dbcfd113c304bb4a6a31b8dcb715385'

}

params = urllib.parse.urlencode({
    # Request parameters
    'allowEdit': 'false',
})

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    conn.request("GET", "/auth/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/AccessToken?%s" % params, "{body}", headers1)
    response = conn.getresponse()
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    # print(json_obj)
    accAccessToken = json_obj
    #print data is the access token
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

#step 2 video access token using part 1

headers2 = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '8dbcfd113c304bb4a6a31b8dcb715385'

}

params = urllib.parse.urlencode({
    # Request parameters
    'allowEdit': 'false',
})

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    conn.request("GET", "/auth/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/Videos/b32f841588/AccessToken?%s" % params, "{body}", headers2)
    response = conn.getresponse()
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    # print(json_obj)
    videoAccessToken = json_obj
    #print data is the access token
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))





#step 3
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
    #data seems to be able to be keyed into twice as dictionary, then holds lists
    # data['summarizedInsights']['faces'] is a list of more dictionaries that hold all of the face information (id, appearances, etc)
    print (data['summarizedInsights']['faces'])

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    conn.request("GET", "/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/Videos/b32f841588/Index?%s" % params, "{body}", headers3)
    response = conn.getresponse()
    data = response.read()
    # thing that needs to be parsed
    # print('\n', data, '\n')   # !!!!! what we need to parse
    j = json.loads(data.decode()) # apparently data is bytes. need to convert bytes to string
    size = len(j['summarizedInsights']['keywords'])
    timestampdict = {}
    graphtimes = {}
    for i in range(0, size):
        keyword = j['summarizedInsights']['keywords'][i]
        timestampdict[keyword['name']] = keyword['appearances']
    for key in timestampdict:
        graphtimes[key] = []
        for dict in timestampdict[key]:
            graphtimes[key].append([dict['startSeconds'], dict['endSeconds']])
    print(timestampdict)
    print(graphtimes)
    # data = str(data)
    # parser(data)  # gave error so we commented out
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