import logging

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag=True
        logging.info(client._client_id.decode("utf-8")+" connected successfully")
    else:
        client.bad_connection_flag=True
        logging.error(client._client_id.decode("utf-8")+" connection failed with code {rc}")

def on_publish(client, userdata, mid):
    logging.info("mid: "+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    logging.info("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

