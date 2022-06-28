import logging
import requests

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag=True
        logging.info(client.name + " connected successfully")
    else:
        client.bad_connection_flag=True
        logging.error(client.name + " connection failed with code {rc}")

def on_publish(client, userdata, mid):
    logging.info("mid: "+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    logging.info("Subscribed: " + str(mid)+ " " + str(granted_qos))

def on_message(client, userdata, message):
    print("Message received: " , message.payload.decode("utf-8"))
    logging.info("Sending data to the database...")
    post = requests.post('http://127.0.0.1:8000/assets/', data=message, headers='Content-Type: application/json')
    post.json()