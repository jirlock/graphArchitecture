import myRdf as rdf


rootDir = 'c:/Users/jirlo/graphArchitecture/'
dataDir = 'c:/Users/jirlo/graphArchitecture/data/'

sensorNames = [
    '2w', '2e', '3w1', '3w2', '3c', '3e1', '3e2', '4w1', '4w2', '4c', '4e1', '4e2', '5c'
]

sensorMacAddresses = [
    '08:3a:f2:23:cc:80',
    '08:3a:f2:22:d1:40',
    '8c:4b:14:15:94:10',
    '08:3a:f2:2b:70:ec',
    '08:3a:f2:2d:47:d0',
    '08:3a:f2:2c:58:14',
    '8c:4b:14:15:7e:84',
    '08:4b:14:15:bf:b8',
    '8c:4b:14:14:91:bc',
    '08:3a:f2:2d:47:80',
    '78:e3:6d:11:3d:20',
    '94:b9:7e:65:fc:00',
    '8c:4b:14:15:9f:dc'
]

headers = [
    '@prefix cmdx: <http://utcmdx.ac.jp/resource#>.',
    '@prefix voc: <http://utcmdx.ac.jp/vocabulary#>.',
    '@prefix brick: <https://brickschema.org/schema/Brick#>.'
]

triples = []

for i in range(len(sensorNames)):
    name = 'Illuminance Sensor ' + sensorNames[i]
    address = sensorMacAddresses[i]
    sensorUri = 'cmdx:sensor' + str(i)
    roomUri = 'cmdx:0'
    typeUri = 'brick:Illuminance_Sensor'

    triples.append(rdf.create_sensor_rdf(sensorUri, roomUri, typeUri, name, address))

rdf_string = rdf.concatRdf([rdf.concatRdf(headers), rdf.concatRdf(triples)])
print(rdf_string)
