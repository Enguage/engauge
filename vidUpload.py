########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
}

params = urllib.parse.urlencode({
    # Request parameters
    # 'description': '{string}',
    # 'partition': '{string}',
    # 'externalId': '{string}',
    # 'callbackUrl': '{string}',
    # 'metadata': '{string}',
    # 'language': '{string}',
    # 'videoUrl': '{string}',
    # 'fileName': '{string}',
    # 'indexingPreset': '{string}',
    # 'streamingPreset': 'Default',
    # 'linguisticModelId': '{string}',
    # 'privacy': '{string}',
    'videoUrl': 'https://andrew.fi/timelapse.mp4',
})

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    conn.request("POST", "/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/Videos?accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJBY2NvdW50SWQiOiJlNmRjNWRhYy1kZTA3LTQ4YTYtYjE1Ny05MTEwNWFjY2M3OGEiLCJBbGxvd0VkaXQiOiJUcnVlIiwiRXh0ZXJuYWxVc2VySWQiOiI0NjE0Q0IwODczNDI0NDRFQjQ0QTk5NTI1MTlDN0M4RSIsIlVzZXJUeXBlIjoiTWljcm9zb2Z0Q29ycEFhZCIsImlzcyI6Imh0dHBzOi8vd3VzMi52aWRlb2luZGV4ZXIuYWkvIiwiYXVkIjoiaHR0cHM6Ly93dXMyLnZpZGVvaW5kZXhlci5haS8iLCJleHAiOjE1MzcwNDQzOTcsIm5iZiI6MTUzNzA0MDQ5N30.9bRrGOqiv-vqDTHwkrTYYJ92ETc0MfKtaQt43JSaJik&name=finland&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

