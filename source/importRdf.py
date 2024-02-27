import myLib
import myGraphDB as gdb

if __name__ == '__main__':

    #rootDir = myLib.rootDir
    #dataDir = myLib.dataDir

    rootDir = myLib.rootDir_sv
    dataDir = myLib.dataDir_sv

    #baseUrl = myLib.baseUrl
    #repoId = myLib.repoId

    baseUrl = myLib.baseUrl_sv
    repoId = myLib.repoId_sv

    #turtle_filename = 'utcmdx_resource.ttl'
    turtle_filename = 'en01.ttl'

    gdb.copy_rdf_file_to_import_folder(dataDir + turtle_filename)
    #gdb.copy_rdf_file_to_import_folder(dataDir + 'Brick.ttl')
    #gdb.copy_rdf_file_to_import_folder(dataDir + 'rec.ttl')
    r = gdb.import_server_files(baseUrl, repoId, [turtle_filename])
    #r = gdb.import_server_files_all(baseUrl, repoId)
    print(r.text)


