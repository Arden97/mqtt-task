import sys
import json
import logging
import requests

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag=True
        logging.info(client.name + " connected successfully")
    else:
        client.bad_connection_flag=True
        logging.error(client.name + " connection failed")

def on_publish(client, userdata, mid):
    logging.info(client.name + " published")

def on_subscribe(client, userdata, mid, granted_qos):
    logging.info(client.name + " subscribed")

def on_message(client, userdata, message):
    msg = json.loads(message.payload)
    print("Message received: " , msg)
    logging.info("Sending data to the database...")
    post = requests.post('http://127.0.0.1:8000/assets/', json=msg)
    print(f"{post.json()['message']}")