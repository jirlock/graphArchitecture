import myAzure
import myMqtt
import myRdf
import myGraphDB as gdb

import requests
import os

if __name__ == '__main__':

    #this is temporal
    rootDir = 'c:/Users/jirlo/graphArchitecture/'
    dataDir = 'c:/Users/jirlo/graphArchitecture/data/'

    #
    baseUrl = 'http://localhost:7200'
    repoId = 'test'

    r = gdb.execute_saved_query(baseUrl, repoId, 'showRooms2')
    print(r.content.decode('utf-8'))





