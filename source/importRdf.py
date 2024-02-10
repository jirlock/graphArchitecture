import myLib
import myGraphDB as gdb

if __name__ == '__main__':
    rootDir = 'c:/Users/jirlo/graphArchitecture/'
    dataDir = rootDir + 'data/'

    baseUrl = 'http://localhost:7200'
    repoId = 'test'

    turtle_filename = 'utcmdx_resource.ttl'

    gdb.copy_rdf_file_to_import_folder(dataDir + turtle_filename)
    #r = gdb.import_server_files(baseUrl, repoId, [turtle_filename])
    r = gdb.import_server_files_all(baseUrl, repoId)
    print(r.text)


