import myGraphDB as gdb
import myMqtt as mqtt

rootDir = 'c:/Users/jirlo/graphArchitecture/'
dataDir = 'c:/Users/jirlo/graphArchitecture/data/'

baseUrl = 'http://localhost:7200'
repoId = 'test'

mqtt_broker = '133.11.95.82'
mqtt_port = 18884
mqtt_client_id = 'sv_utcmdx'

sensor_info = {
    '2e': '08:3a:f2:23:cc:80',
    '2w': '08:3a:f2:22:d1:40',
    '3e2': '8c:4b:14:15:94:10',
    '3e1': '08:3a:f2:2b:70:ec',
    '3c': '08:3a:f2:2d:47:d0',
    '3w1': '08:3a:f2:2c:58:14',
    '3w2': '8c:4b:14:15:7e:84',
    '4e2': '08:4b:14:15:bf:b8',
    '4e1': '8c:4b:14:14:91:bc',
    '4c': '08:3a:f2:2d:47:80',
    '4w1': '78:e3:6d:11:3d:20',
    '4w2': '94:b9:7e:65:fc:00',
    '5c': '8c:4b:14:15:9f:dc'
}


#====================
# Subscription
#====================

def update_illuminance_sensor(base_url, repo_id, mac_address, value, time):
    json_data = {
        "mac": mac_address,
        "newValue": value,
        "newTime": time
    }
    templateId = 'http://utcmdx.ac.jp/templates/updateIlluminanceSensor'
    return gdb.execute_sparql_template(base_url, repo_id, templateId, json_data)

def set_subscription_ill_sensor(mqtt_client, base_url, repo_id, mac_address):
    def on_message_ill_sensor(client, userdata, msg):
        topic, time, illumination = mqtt.parse_ill_sensor(msg)
        #print(mqtt.convertTopic2Id(topic))
        #print(time)
        #print(illumination)
        r = update_illuminance_sensor(base_url, repo_id, mac_address, illumination, time)
        print(r.text)
    topic = mac_address + '/01/ill01'
    mqtt_client.message_callback_add(topic, on_message_ill_sensor)
    mqtt_client.subscribe(topic)

def update_sht_sensor(base_url, repo_id, mac_address, humidity, temperature, time):
    json_data = {
        "mac": mac_address,
        "newHumidity": humidity,
        "newTemperature": temperature,
        "newTime": time
    }
    templateId = 'http://utcmdx.ac.jp/templates/updateShtSensor'
    return gdb.execute_sparql_template(base_url, repo_id, templateId, json_data)

def set_subscription_sht_sensor(mqtt_client, base_url, repo_id, mac_address):
    def on_message_sht_sensor(client, userdata, msg):
        topic, time, temperature, humidity = mqtt.parse_sht_sensor(msg)
        #print(topic[:17])
        #print(time)
        #print(temperature)
        #print(humidity)
        r = update_sht_sensor(base_url, repo_id, mac_address, humidity, temperature, time)
        print(r.text)
    topic = mac_address + '/01/sht31'
    mqtt_client.message_callback_add(topic, on_message_sht_sensor)
    mqtt_client.subscribe(topic)

def update_ir_sensor(base_url, repo_id, mac_address, temperature, temperature_array, time):
    json_data = {
        "mac": mac_address,
        "newTemperature": temperature,
        "newTemperatureArray": temperature_array,
        "newTime": time
    }
    templateId = 'http://utcmdx.ac.jp/templates/updateIRSensor'
    return gdb.execute_sparql_template(base_url, repo_id, templateId, json_data)

def set_subscription_ir_sensor(mqtt_client, base_url, repo_id, mac_address):
    def on_message_ir_sensor(client, userdata, msg):
        topic, time, temperature, temperature_array = mqtt.parse_ir_sensor(msg)
        r = update_ir_sensor(base_url, repo_id, mac_address, temperature, temperature_array, time)
        print(r.text)
    topic = mac_address + '/01/array02'
    mqtt_client.message_callback_add(topic, on_message_ir_sensor)
    mqtt_client.subscribe(topic)

#====================
# Get Sensor Data
#====================

class ill_sensor:
    def __init__(self, name, mac_address, illuminance, time):
        self.name = name
        self.mac_address = mac_address
        self.illuminance = illuminance
        self.time = time


def parse_ill_sensor_data(data_string):
    data = []
    for line in data_string.split('\r\n'):
        data = [str(x) for x in line.split(',')]



def get_ill_sensor_data(base_url, repo_id):
    r = gdb.execute_saved_query(base_url, repo_id, 'query_sensor_ill')
    parse_ill_sensor_data(r.text)
    return r

def get_sht_sensor_data(base_url, repo_id):
    return gdb.execute_saved_query(base_url, repo_id, 'query_sensor_sht')

def get_ir_sensor_data(base_url, repo_id):
    return gdb.execute_saved_query(base_url, repo_id, 'query_sensor_ir')
