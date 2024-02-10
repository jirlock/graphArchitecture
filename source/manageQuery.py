import myGraphDB as gdb
import myLib

baseUrl = myLib.baseUrl
repoId = myLib.repoId

query_name_ill = 'query_sensor_ill'
query_path_ill = myLib.dataDir + 'query_sensor_ill.txt'

query_name_sht = 'query_sensor_sht'
query_path_sht = myLib.dataDir + 'query_sensor_sht.txt'

query_name_ir = 'query_sensor_ir'
query_path_ir = myLib.dataDir + 'query_sensor_ir.txt'

#r = gdb.save_query_from_file(baseUrl, query_name_ir, query_path_ir)
#print(r.text)

#r = gdb.save_query_from_file(baseUrl, query_name_sht, query_path_sht)
#print(r.text)

#r = gdb.edit_query_from_file(baseUrl, query_name_ill, query_path_ill)
#print(r.text)