import myRdf as rdf
import myLib


rootDir = 'c:/Users/jirlo/graphArchitecture/'
dataDir = 'c:/Users/jirlo/graphArchitecture/data/'

sensor_info = myLib.sensor_info

sensorNames = [
    '2e', '2w', '3e2', '3e1', '3c', '3w1', '3w2', '4e2', '4e1', '4c', '4w1', '4w2', '5c'
]

headers = [
    '@prefix cmdx: <http://utcmdx.ac.jp/resource#>.',
    '@prefix voc: <http://utcmdx.ac.jp/vocabulary#>.',
    '@prefix brick: <https://brickschema.org/schema/Brick#>.'
]

roomTriples = [
    'cmdx:room0 rdf:type voc:room.',
    'cmdx:room0 rdfs:label "15号講義室".',
]

triples = []
sensor_num = 0

for i in range(len(sensorNames)):
    roomUri = 'cmdx:room0'
    address = sensor_info[sensorNames[i]]

    illName = 'Illuminance Sensor ' + sensorNames[i]
    sensorUri = 'cmdx:sensor' + str(sensor_num)
    triples.append(rdf.create_ill_sensor_rdf(sensorUri, roomUri, illName, address))
    sensor_num += 1

    shtName = 'Humidity Temperature Sensor ' + sensorNames[i]
    sensorUri = 'cmdx:sensor' + str(sensor_num)
    triples.append(rdf.create_sht_sensor_rdf(sensorUri, roomUri, shtName, address))
    sensor_num += 1

    irName = 'IR Sensor ' + sensorNames[i]
    sensorUri = 'cmdx:sensor' + str(sensor_num)
    triples.append(rdf.create_ir_sensor_rdf(sensorUri, roomUri, irName, address))
    sensor_num += 1

rdf_string = rdf.concatRdf([rdf.concatRdf(headers), rdf.concatRdf(roomTriples), rdf.concatRdf(triples)])

with open(dataDir+'utcmdx_resource.ttl', 'w', encoding='utf-8') as f:
    f.write(rdf_string)

print('done')


