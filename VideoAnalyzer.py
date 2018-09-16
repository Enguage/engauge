import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

accountID = "e6dc5dac-de07-48a6-b157-91105accc78a"
accAccessToken = ""
subscriptionKey = '8dbcfd113c304bb4a6a31b8dcb715385'
videoAccessToken = "b32f841588"




def getVideoData():
    global videoAccessToken

    # account token
    headers1 = {
        # Request headers
        'Ocp-Apim-Subscription-Key': subscriptionKey

    }

    params = urllib.parse.urlencode({
        # Request parameters
        'allowEdit': 'false',
    })

    try:
        conn = http.client.HTTPSConnection('api.videoindexer.ai')
        conn.request("GET", "/auth/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/AccessToken?%s" % params,
                     "{body}",
                     headers1)
        response = conn.getresponse()
        string = response.read().decode('utf-8')
        json_obj = json.loads(string)
        # print(json_obj)
        accAccessToken = json_obj
        # print data is the access token
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # step 2 video access token using part 1

    headers2 = {
        # Request headers
        'Ocp-Apim-Subscription-Key': subscriptionKey

    }

    params = urllib.parse.urlencode({
        # Request parameters
        'allowEdit': 'false',
    })

    try:
        conn = http.client.HTTPSConnection('api.videoindexer.ai')
        conn.request("GET",
                     "/auth/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/Videos/b32f841588/AccessToken?%s" % (params),
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
        'Ocp-Apim-Subscription-Key': subscriptionKey,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'accessToken': accAccessToken,
        'language': 'English',
    })

    try:
        conn = http.client.HTTPSConnection('api.videoindexer.ai')
        conn.request("GET",
                     "/westus2/Accounts/e6dc5dac-de07-48a6-b157-91105accc78a/Videos/b32f841588/Index?%s" % (params),
                     "{body}", headers3)
        response = conn.getresponse()
        data = response.read()
        # thing that needs to be parsed
        # print('startdata\n', data, '\nenddata')   # !!!!! what we need to parse
        j = json.loads(data.decode())  # apparently data is bytes. need to convert bytes to string
        conn.close()

        return j

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

