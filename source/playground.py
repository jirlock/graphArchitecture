#import myAzure
import myMqtt as mqtt
import myRdf as rdf
import myGraphDB as gdb
import myLib

if __name__ == '__main__':

    #this is temporal
    rootDir = myLib.rootDir
    dataDir = myLib.dataDir

    baseUrl = myLib.baseUrl
    repoId = myLib.repoId

    sensorInfo = myLib.sensor_info

    client = mqtt.connect
