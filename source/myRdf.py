import urllib.request
import json

def GET(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = json.loads(response.read())
            headers = response.getheaders()
            status = response.getcode()

            print(headers)
            print(status)
            print(body)
    
    except urllib.error.URLError as e:
        print(e.reason)


def POST(url, req_data, req_headers):
    req = urllib.request.Request(url, data=req_data.encode(), method='POST', headers=req_headers)
    try:
        with urllib.request.urlopen(req) as response:
            body = json.loads(response.read())
            headers = response.getheaders()
            status = response.getcode()

            print(headers)
            print(status)
            print(body)

    except urllib.error.URLError as e:
        print(e.reason)

def concatRdf(triples):
    rdf = ''
    for triple in triples:
        rdf += triple + '\n'
    return rdf

def createLabelTriple(uri, label):
    return uri + ' rdfs:label ' + '"' + label + '"' + '.'

def createBuildingUri(baseUri, campus, faculty, bldg):
    return '<' + baseUri + '/building/' + campus + '/' + faculty + '/' + bldg + '>' 

def createLevelUri(baseUri, campus, faculty, bldg, level):
    return '<' + baseUri + '/level/' + campus + '/' + faculty + '/' + bldg + '/' + level + '>'

def createRoomUri(baseUri, campus, faculty, bldg, level, room):
    return '<' + baseUri + '/room/' + campus + '/' + faculty + '/' + bldg + '/' + level + '/' + room + '>'

#return String
def createBuildingRdf(baseUri, campus, faculty, bldg, label):
    bldgUri = createBuildingUri(baseUri, campus, faculty, bldg)
    classTriple = bldgUri + ' a rec:Building.'
    labelTriple = createLabelTriple(bldgUri, label)
    return concatRdf([classTriple, labelTriple])

def createLevelRdf(baseUri, campus, faculty, bldg, level, label):
    lvlUri = createLevelUri(baseUri, campus, faculty, bldg, level)
    bldgUri = createBuildingUri(baseUri, campus, faculty, bldg)
    classTriple = lvlUri + ' a rec:Level.'
    labelTriple = createLabelTriple(lvlUri, label)
    buildingTriple = lvlUri + ' rec:isPartOf ' + bldgUri + '.'
    levelTriple = bldgUri + ' rec:hasPart ' + lvlUri + '.'
    return concatRdf([classTriple, labelTriple, buildingTriple, levelTriple])

def createRoomRdf(baseUri, campus, faculty, bldg, level, room, label):
    uri = createRoomUri(baseUri, campus, faculty, bldg, level, room)
    lvlUri = createLevelUri(baseUri, campus, faculty, bldg, level)
    classTriple = uri + ' a rec:Room.'
    labelTriple = createLabelTriple(uri, label)
    levelTriple = uri + ' rec:isPartOf ' + lvlUri + '.'
    roomTriple = lvlUri + ' rec:hasPart ' + uri + '.'
    return concatRdf([classTriple, labelTriple, levelTriple, roomTriple])

def createRoomRelationRdf(roomUri1, roomUri2):
    rel1 = roomUri1 + ' rec:accessibleFrom ' + roomUri2 + '.'
    rel2 = roomUri2 + ' rec:accessibleFrom ' + roomUri1 + '.'
    return concatRdf([rel1, rel2])

def executeSparqlTemplate():
    return 0

