import myAzure
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

    r = myLib.get_ill_sensor_data(baseUrl, repoId, '8c:4b:14:15:94:10')
    print(r.text)
