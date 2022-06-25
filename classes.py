import json
from utils import *
import logging
import requests
import paho.mqtt.client as mqtt

class Publisher(mqtt.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.info('Creating publisher instance')
        self.on_connect = on_connect
        self.on_publish = on_publish
        self.username_pw_set(self._client_id.decode("utf-8"), "password")

    def query_coincap(self, api_addr, topic):
        response = requests.get(api_addr + topic)
        if response.status_code != 200:
            logging.error('CoinCAP has responded with an error')
            raise Exception()
        logging.info('Receiving data from CoinCAP')
        return str(json.loads(response.text))
    
    def set_cert(self, path):
        self.tls_set(path,tls_version=2)

    def run(self, addr):
        logging.info('Connecting publisher to broker')
        self.connect(addr,8883, 60)
        logging.info('Running publisher')
        self.loop_start()

    def stop(self):
        logging.info('Stoping publisher')
        self.loop_stop()


class Subscriber(mqtt.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.info('Creating subscriber instance')
        self.on_connect = on_connect
        self.on_message = on_message
        self.username_pw_set(self._client_id.decode("utf-8"), "password")

    def run(self, addr):
        logging.info('Connecting subscriber to broker')
        self.connect(addr,8883, 60)
        logging.info('Running subscriber')
        self.loop_start()

    def stop(self):
        logging.info('Stoping subscriber')
        self.loop_stop()