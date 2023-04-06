import http.client
import json
import constants

def getBoardStrings(gameId):
    board = []
    conn = http.client.HTTPSConnection("www.notexponential.com")
    payload = ''
    headers = {
        'x-api-key': constants.xapikey,
        'userid': constants.userId,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    api = "/aip2pgaming/api/index.php?type=boardString&gameId=" + str(gameId)
    conn.request("GET", api, payload, headers)
    res = conn.getresponse()
    data = res.read()
    jsonInput = json.loads(data.decode("utf-8"))["output"]
    row = []
    for x in jsonInput:
        if x != "\n":
            row.append(x)
        else:
            board.append(row)
            row = []
    return board


def makeMove(gameId, move):
    conn = http.client.HTTPSConnection("www.notexponential.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=type;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append("move")
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=gameId;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append(str(gameId))
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=teamId;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append(constants.teamId)
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=move;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append(move)
    dataList.append('--' + boundary + '--')
    dataList.append('')
    body = '\r\n'.join(dataList)
    payload = body
    headers = {
        'x-api-key': constants.xapikey,
        'userId': constants.userId,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/aip2pgaming/api/index.php", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))


def getMoves(gameId, count):
    conn = http.client.HTTPSConnection("www.notexponential.com")
    boundary = ''
    payload = ''
    headers = {
        'x-api-key': constants.xapikey,
        'userId': constants.userId,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("GET", "/aip2pgaming/api/index.php?type=moves&gameId={}&count={}".format(gameId, count), payload,
                 headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))["moves"][0]["moveId"]
