import myMqtt as mqtt

mqtt_broker = '133.11.95.82'
mqtt_port = 18884
mqtt_client_id = 'sv_utcmdx'

client = mqtt.connect_mqtt(mqtt_client_id, mqtt_broker, mqtt_port)

def callback(client, userdata, msg):
    print(msg.topic)
    print('==========')

topic = '78:e3:6d:11:3d:20/01/array02'
topic2 = '08:3a:f2:23:cc:80/01/array02'
client.message_callback_add(topic, callback)
#client.message_callback_add(topic2, callback)
client.subscribe(topic)
#client.subscribe(topic2)

#client.loop_forever()