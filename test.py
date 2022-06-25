from classes import *

API_URL = "https://api.coincap.io/v2/"
BROKER_URL = "127.0.0.1"
CERT_PATH="/etc/mosquitto/ca_certificates/ca.crt"
TOPICS = ["assets/bitcoin", "assets/ethereum", "assets/dogecoin"]

logging.basicConfig(filename='logs.log', level=logging.INFO)
logging.info('Started')

publisher = Publisher("PUB")
subscriber = Subscriber("SUB")

subscriber.run(BROKER_URL)
subscriber.subscribe(TOPICS[1])
publisher.set_cert(CERT_PATH)
publisher.run(BROKER_URL)
publisher.publish(TOPICS[1], publisher.query_coincap(API_URL, TOPICS[1]))

publisher.stop()
subscriber.stop()

logging.info('Finished')