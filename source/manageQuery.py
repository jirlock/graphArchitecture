import myGraphDB as gdb
import myLib

baseUrl = myLib.baseUrl
repoId = myLib.repoId

sensorInfo = myLib.sensor_info

#r = gdb.save_query_from_file(baseUrl, query_name_ir, query_path_ir)
#print(r.text)

#r = gdb.save_query_from_file(baseUrl, query_name_sht, query_path_sht)
#print(r.text)

#r = gdb.edit_query_from_file(baseUrl, query_name_ill, query_path_ill)
#sensorInfo = myLib.sensor_info

query_path_ill = myLib.dataDir + 'query_sensor_ill_template.txt'
for k,v in sensorInfo.items():
    queryName = 'query_sensor_ill_' + v
    with open(query_path_ill, 'r', encoding='utf-8') as f:
        s = f.read()
    queryString = s.replace('?mac', '"' + v + '"')

    r = gdb.save_query(baseUrl, queryName, queryString)
    r = gdb.edit_query(baseUrl, queryName, queryString)
    print(r.text)


query_path_sht = myLib.dataDir + 'query_sensor_sht_template.txt'
for k,v in sensorInfo.items():
    queryName = 'query_sensor_sht_' + v
    with open(query_path_sht, 'r', encoding='utf-8') as f:
        s = f.read()
    queryString = s.replace('?mac', '"' + v + '"')

    r = gdb.save_query(baseUrl, queryName, queryString)
    r = gdb.edit_query(baseUrl, queryName, queryString)
    print(r.text)

query_path_ir = myLib.dataDir + 'query_sensor_ir_template.txt'
for k,v in sensorInfo.items():
    queryName = 'query_sensor_ir_' + v
    with open(query_path_ir, 'r', encoding='utf-8') as f:
        s = f.read()
    queryString = s.replace('?mac', '"' + v + '"')

    r = gdb.save_query(baseUrl, queryName, queryString)
    r = gdb.edit_query(baseUrl, queryName, queryString)
    print(r.text)
