import myAzure
import myMqtt
import myRdf as rdf
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

    turtle_filename = 'utcmdx_resource.ttl'

    r = gdb.copy_rdf_file_to_import_folder(dataDir + turtle_filename)
    r = gdb.import_server_files(baseUrl, repoId, [turtle_filename])
    print(r.text)

'''
    with open(dataDir+'query_tmp.txt', 'r') as f:
        query_string = f.read()
    r = gdb.execute_query_simple(baseUrl, repoId, query_string)
    print(r.text)
'''




