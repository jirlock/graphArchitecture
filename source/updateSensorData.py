import myMqtt as mqtt
import myLib

if __name__ == '__main__':

    #this is temporal
    #rootDir = myLib.rootDir
    #dataDir = myLib.dataDir

    #baseUrl = myLib.baseUrl
    #repoId = myLib.repoId

    rootDir = myLib.rootDir_sv
    dataDir = myLib.dataDir_sv

    baseUrl = myLib.baseUrl_sv
    repoId = myLib.repoId_sv

    mqtt_broker = myLib.mqtt_broker
    mqtt_port = myLib.mqtt_port
    mqtt_client_id = myLib.mqtt_client_id
    sensor_info = myLib.sensor_info

    mqtt_client = mqtt.connect_mqtt(mqtt_client_id, mqtt_broker, mqtt_port)


    #======================================

    for sensorName, macAddress in sensor_info.items():
        myLib.set_subscription_ill_sensor(mqtt_client, baseUrl, repoId, macAddress)
        myLib.set_subscription_sht_sensor(mqtt_client, baseUrl, repoId, macAddress)
        myLib.set_subscription_ir_sensor(mqtt_client, baseUrl, repoId, macAddress)

    mqtt_client.loop_forever()


