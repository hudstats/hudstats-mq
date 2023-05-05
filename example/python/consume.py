import os, signal
from kafka import KafkaProducer, KafkaConsumer

BOOTSTRAP_SERVERS=os.getenv("KAFKA_BOOTSTRAP_SERVERS").split(",")
TOPIC_NAME=os.getenv("KAFKA_TOPIC")
SASL_USERNAME=os.getenv("KAFKA_SASL_USERNAME")
SASL_PASSWORD=os.getenv("KAFKA_SASL_PASSWORD")

consumer = KafkaConsumer(TOPIC_NAME, security_protocol="SASL_SSL",  sasl_mechanism="SCRAM-SHA-512", sasl_plain_username=SASL_USERNAME, sasl_plain_password=SASL_PASSWORD, bootstrap_servers=BOOTSTRAP_SERVERS, auto_offset_reset='earliest')

def consume():
 for msg in consumer:
    print (msg)

def int_handler(signum, frame):
    try:
        consumer.unsubscribe()
        consumer.close()
    except Exception as e:
        LOGGER.error(traceback.format_exc())
        print(e)
        exit(1)
    exit(0)

signal.signal(signal.SIGINT, int_handler)

if __name__ == '__main__':
    consume()
