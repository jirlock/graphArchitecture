import myLib
import myGraphDB as gdb

if __name__ == '__main__':

    rootDir = myLib.rootDir
    dataDir = myLib.dataDir

    baseUrl = myLib.baseUrl
    repoId = myLib.repoId

    turtle_filename = 'lec15sensor.ttl'
    #turtle_filename = 'en01_new.ttl'
    #turtle_filename = 'en01.ttl'
    #turtle_filename = 'en10.ttl'

    gdb.copy_rdf_file_to_import_folder(dataDir + turtle_filename)
    #gdb.copy_rdf_file_to_import_folder(dataDir + 'Brick.ttl')
    #gdb.copy_rdf_file_to_import_folder(dataDir + 'rec.ttl')
    r = gdb.import_server_files(baseUrl, repoId, [turtle_filename])
    #r = gdb.import_server_files_all(baseUrl, repoId)
    print(r.text)


