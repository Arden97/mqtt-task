from multiprocessing.connection import wait
from classes import *
import time

API_URL = "https://api.coincap.io/v2/"
BROKER_URL = "127.0.0.1"
CERT_PATH="/etc/mosquitto/ca_certificates/ca.crt"
TOPICS = ["assets/bitcoin", "assets/ethereum", "assets/dogecoin"]

def main():

    logging.basicConfig(filename='logs.log', level=logging.INFO)
    logging.info('Started')

    publisher = Publisher("PUB")
    subscriber = Subscriber("SUB")

    subscriber.set_cert(CERT_PATH)
    subscriber.run(BROKER_URL)
    subscriber.subscribe(TOPICS[1])

    data = publisher.query_coincap(API_URL, TOPICS[1])
    publisher.set_cert(CERT_PATH)
    publisher.run(BROKER_URL)
    publisher.publish(TOPICS[1], data)

    time.sleep(5)
    
    subscriber.update(data,'rank',10)

    publisher.stop()
    subscriber.stop()

    logging.info('Finished')

if __name__ == "__main__":
    main() # pylint: disable=no-value-for-parameter