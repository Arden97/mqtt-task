import json
from utils import *
import paho.mqtt.client as mqtt

class Publisher(mqtt.Client):

    def __init__(self, *args, **kwargs):
        logging.info('Creating publisher instance')
        super().__init__(*args, **kwargs)
        self.name = self._client_id.decode("utf-8")
        self.on_connect = on_connect
        self.on_publish = on_publish
        self.username_pw_set(self.name, "password")

    def query_coincap(self, api_addr, topic):
        response = requests.get(api_addr + topic)
        if response.status_code != 200:
            logging.error('CoinCAP has responded with an error')
            raise Exception()
        logging.info(self.name + ' receives data from CoinCAP')
        return json.loads(response.text)
    
    def set_cert(self, path):
        self.tls_set(path,tls_version=2)
        self.tls_insecure_set(True)

    def run(self, addr):
        logging.info('Connecting ' + self.name + ' publisher to broker')
        self.connect(addr,8883, 60)
        logging.info('Running ' + self.name + ' publisher')
        self.loop_start()

    def stop(self):
        logging.info('Stoping ' + self.name + ' publisher')
        self.loop_stop()


class Subscriber(mqtt.Client):

    def __init__(self, *args, **kwargs):
        logging.info('Creating subscriber instance')
        super().__init__(*args, **kwargs)
        self.name = self._client_id.decode("utf-8")
        self.on_connect = on_connect
        self.on_message = on_message
        self.username_pw_set(self.name, "password")

    def update(data, value, new_value):
        asset = data['id']
        logging.info('Updating '+asset)
        data[value] = new_value
        post = requests.post('http://127.0.0.1:8000/update/'+asset, data=data, headers='Content-Type: application/json')
        post.json()

    def set_cert(self, path):
        self.tls_set(path,tls_version=2)
        self.tls_insecure_set(True)

    def run(self, addr):
        logging.info('Connecting ' + self.name + ' subscriber to broker')
        self.connect(addr,8883, 60)
        logging.info('Running ' + self.name + ' subscriber')
        self.loop_start()

    def stop(self):
        logging.info('Stoping ' + self.name + ' subscriber')
        self.loop_stop()