import myGraphDB as gdb
import myMqtt as mqtt


#For Windows
#rootDir = 'c:/Users/jirlo/graphArchitecture/'
#dataDir = 'c:/Users/jirlo/graphArchitecture/data/'

#baseUrl = 'http://localhost:7200'
#repoId = 'test'

#For Linux
rootDir = '/home/keijiro/graphArchitecture/'
dataDir = '/home/keijiro/graphArchitecture/data/'

baseUrl = 'http://localhost:7200'
repoId = 'repo_utcmdx'

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
    '4e2': '8c:4b:14:15:bf:b8',
    '4e1': '8c:4b:14:14:91:dc',
    '4c': '08:3a:f2:2d:47:80',
    '4w1': '78:e3:6d:11:3d:20',
    '4w2': '94:b9:7e:65:fc:00',
    '5c': '8c:4b:14:15:9f:dc',
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
        #print(r.text)
        print('Updated Ill Sensor ' + mac_address + '\n')
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
        #print(r.text)
        print('Updated Sht Sensor ' + mac_address + '\n')
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
        #print(r.text)
        print('Updated IR Sensor ' + mac_address + '\n')
    topic = mac_address + '/01/array02'
    mqtt_client.message_callback_add(topic, on_message_ir_sensor)
    mqtt_client.subscribe(topic)

#====================
# Get Sensor Data
#====================

class Sensor_ill:
    def __init__(self, name, mac_address, illuminance, time):
        self.name = name
        self.mac_address = mac_address
        self.illuminance = illuminance
        self.time = time
    
    def print_info(self):
        print('====================')
        print('name: ' + self.name)
        print('mac address: ' + self.mac_address)
        print('illuminance:' + str(self.illuminance))
        print('time: ' + str(self.time))
        print('====================')
    
    def get_info(self):
        return self.name, self.mac_address, self.illuminance, self.time

    def update(self):
        r = gdb.execute_saved_query(baseUrl, repoId, 'query_sensor_ill_' + self.mac_address)
        for i, line in enumerate(r.text.split('\r\n')):
            if i == 1:
                try:
                    name, illuminance, time = parse_ill_sensor_data(line)
                    self.illuminance = illuminance
                    self.time = time
                    return True
                except:
                    break
        return False

class Sensor_sht:
    def __init__(self, name, mac_address, humidity, temperature, time):
        self.name = name
        self.mac_address = mac_address
        self.humidity = humidity
        self.temperature = temperature
        self.time = time

    def print_info(self):
        print('====================')
        print('name: ' + self.name)
        print('mac address: ' + self.mac_address)
        print('humidity:' + str(self.humidity))
        print('temperature: ' + str(self.temperature))
        print('time: ' + str(self.time))
        print('====================')

    def get_info(self):
        return self.name, self.mac_address, self.humidity, self.temperature, self.time

    def update(self):
        r = gdb.execute_saved_query(baseUrl, repoId, 'query_sensor_sht_' + self.mac_address)
        for i, line in enumerate(r.text.split('\r\n')):
            if i == 1:
                try:
                    name, humidity, temperature, time = parse_sht_sensor_data(line)
                    self.humidity = humidity
                    self.temperature = temperature
                    self.time = time
                    return True
                except:
                    break
        return False

class Sensor_ir:
    def __init__(self, name, mac_address, temperature, arrayTemperature, time):
        self.name = name
        self.mac_address = mac_address
        self.temperature = temperature
        self.arrayTemperature = arrayTemperature
        self.time = time

    def print_info(self):
        print('====================')
        print('name: ' + self.name)
        print('mac address: ' + self.mac_address)
        print('temperature:' + str(self.temperature))
        print('arrayTemperature: ' + str(self.arrayTemperature))
        print('time: ' + str(self.time))
        print('====================')

    def get_info(self):
        return self.name, self.mac_address, self.temperature, self.arrayTemperature, self.time

    def update(self):
        r = gdb.execute_saved_query(baseUrl, repoId, 'query_sensor_ir_' + self.mac_address)
        for i, line in enumerate(r.text.split('\r\n')):
            if i == 1:
                name, temperature, arrayTemperature, time = parse_ir_sensor_data(line)
                self.temperature = temperature
                self.arrayTemperature = arrayTemperature
                self.time = time
                return True
        return False

def parse_ill_sensor_data(data_string):
    data = [str(x) for x in data_string.split(',')]
    name = data[0]
    illuminance = int(data[1])
    time = int(data[2])
    return name, illuminance, time

def parse_sht_sensor_data(data_string):
    data = [str(x) for x in data_string.split(',')]
    name = data[0]
    humidity = float(data[1])
    temperature = float(data[2])
    time = int(data[3])
    return name, humidity, temperature, time

def parse_ir_sensor_data(data_string):
    data = [str(x).replace('"[', "").replace(']"', "") for x in data_string.split(',')]
    name = data[0]
    temperature = float(data[1])
    #arrayTemperature = list(data[2])
    arrayTemperature = [float(x) for x in data[2:66]]
    time = data[66]
    return name, temperature, arrayTemperature, time

def get_ill_sensor_data_all(base_url, repo_id):
    r = gdb.execute_saved_query(base_url, repo_id, 'query_sensor_ill')
    print(r.status_code)
    return r.text

def get_sht_sensor_data_all(base_url, repo_id):
    r = gdb.execute_saved_query(base_url, repo_id, 'query_sensor_sht')
    print(r.status_code)
    return r.text

def get_ir_sensor_data_all(base_url, repo_id):
    r = gdb.execute_saved_query(base_url, repo_id, 'query_sensor_ir')
    print(r.status_code)
    return r.text
