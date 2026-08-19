import ssl
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Resultado de conexion:", rc)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set("savia_user", "SAVIA1234")
client.tls_set(ca_certs="certs/ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.on_connect = on_connect

client.connect("zephyr.proxy.rlwy.net", 38715, 60)
client.loop_start()

import time
time.sleep(3)
client.publish("savia/test", "hola mundo desde python")
time.sleep(2)
client.loop_stop()
