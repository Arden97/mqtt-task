from classes import *

API_URL = "https://api.coincap.io/v2/"
BROKER_URL = "127.0.0.1"
TOPICS = ["assets", "assets/bitcoin", "assets/ethereum", "assets/dogecoin"]

publisher = Publisher("PUB")
subscriber = Subscriber("SUB")

subscriber.run(BROKER_URL)
subscriber.subscribe(TOPICS[1])

publisher.run(BROKER_URL)
publisher.publish(TOPICS[1], publisher.query_coincap(API_URL, TOPICS[1]))

publisher.stop()
subscriber.stop()
