import json
import utils
import requests
import paho.mqtt.client as mqtt

class Publisher(mqtt.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_connect = utils.on_connect
        self.on_publish = utils.on_publish

    def query_coincap(self, api_addr, topic):
        response = requests.get(api_addr + topic)
        if response.status_code != 200:
            raise Exception('The server has responded with an error')
        return str(json.loads(response.text))

    def run(self, addr):
        self.connect(addr,1883, 60)
        self.loop_start()

    def stop(self):
        self.loop_stop()


class Subscriber(mqtt.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_connect = utils.on_connect
        self.on_message = utils.on_message

    def run(self, addr):
        self.connect(addr,1883, 60)
        self.loop_start()

    def stop(self):
        self.loop_stop()