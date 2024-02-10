import myLib
import myGraphDB as gdb
import pandas as pd

rootDir = myLib.rootDir
dataDir = myLib.dataDir

baseUrl = myLib.baseUrl
repoId = myLib.repoId

r = myLib.get_ill_sensor_data(baseUrl, repoId)


#r = myLib.get_ir_sensor_data(baseUrl, repoId)
#print(r.text)