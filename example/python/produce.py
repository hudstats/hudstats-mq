import os
from kafka import KafkaProducer, KafkaConsumer

BOOTSTRAP_SERVERS=os.getenv("KAFKA_BOOTSTRAP_SERVERS").split(",")
TOPIC_NAME=os.getenv("KAFKA_TOPIC")
SASL_USERNAME=os.getenv("KAFKA_SASL_USERNAME")
SASL_PASSWORD=os.getenv("KAFKA_SASL_PASSWORD")

def produce():
    producer = KafkaProducer(security_protocol="SASL_SSL",  sasl_mechanism="SCRAM-SHA-512", sasl_plain_username=SASL_USERNAME, sasl_plain_password=SASL_PASSWORD, bootstrap_servers=BOOTSTRAP_SERVERS)
    producer.send(TOPIC_NAME, b'Hello, world!')

if __name__ == '__main__':
    produce()
