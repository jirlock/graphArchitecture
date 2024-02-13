import myLib
import myGraphDB as gdb
import pandas as pd

rootDir = myLib.rootDir
dataDir = myLib.dataDir

baseUrl = myLib.baseUrl
repoId = myLib.repoId

ill_data = myLib.get_ill_sensor_data_all(baseUrl, repoId)

#print(ill_data)

sht_data = myLib.get_sht_sensor_data_all(baseUrl, repoId)
ir_data = myLib.get_ir_sensor_data_all(baseUrl, repoId)

temp_ill_sensor = myLib.Sensor_ill('Illuminance Sensor 2e', '08:3a:f2:23:cc:80', 0, 1700000000000)
if (temp_ill_sensor.update(baseUrl, repoId)):
    print(temp_ill_sensor.illuminance)
    print(temp_ill_sensor.time)

#r = myLib.get_ir_sensor_data(baseUrl, repoId)
#print(r.text)