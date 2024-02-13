import myLib

if __name__ == '__main__':

    #this is temporal
    rootDir = myLib.rootDir
    dataDir = myLib.dataDir

    baseUrl = myLib.baseUrl
    repoId = myLib.repoId

    sensorInfo = myLib.sensor_info

    #Create Objects
    illSensors = []
    shtSensors = []
    irSensors = []

    for k,v in sensorInfo.items():
        ill_name = "Illuminance Sensor " + k
        illSensors.append(myLib.Sensor_ill(ill_name, v, 0, 1700000000000))

        sht_name = "Humidity Temperature Sensor " + k
        shtSensors.append(myLib.Sensor_sht(sht_name, v, 0.0, 0.0, 1700000000000))

        ir_name = "IR Sensor " + k
        irSensors.append((myLib.Sensor_ir(ir_name, v, 0.0, [0.0 for _ in range(64)], 1700000000000)))
    
    for sensor in shtSensors:
        sensor.update()
        sensor.print_info()