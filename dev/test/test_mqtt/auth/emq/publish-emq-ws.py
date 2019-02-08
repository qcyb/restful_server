import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

hostname = "127.0.0.1"
transport, port = 'websockets', 8083
topic = 'emqtt'
payload = 'Hello, EMQ!'
# client_id = 'client_id2'
client_id = ''
username = 'user2'
password = 'password'


# client = mqtt.Client(client_id='test-client')
# client.username_pw_set(username=username, password=password)
# client.connect(hostname, 1883, 60)
# client.publish(topic, payload=payload, qos=0)

auth = {'username': username, 'password': password}
publish.single(topic, payload=payload, qos=0, client_id=client_id, hostname=hostname, auth=auth)
