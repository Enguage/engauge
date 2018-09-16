########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
}

params = urllib.parse.urlencode({
    # Request parameters
    'description': '{string}',
    'partition': '{string}',
    'externalId': '{string}',
    'callbackUrl': '{string}',
    'metadata': '{string}',
    'language': '{string}',
    'videoUrl': '{string}',
    'fileName': '{string}',
    'indexingPreset': '{string}',
    'streamingPreset': 'Default',
    'linguisticModelId': '{string}',
    'privacy': '{string}',
    'externalUrl': '{string}',
})

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    conn.request("POST", "/{location}/Accounts/{accountId}/Videos?accessToken={accessToken}&name={name}&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
