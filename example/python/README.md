# Prerequisites

1. You will need Kafka bootstrap server list and bind it to the environment variable `KAFKA_BOOTSTRAP_SERVERS`
2. You will need Kafka username and password and bind them accordingly to `KAFKA_SASL_USERNAME` and `KAFKA_SASL_PASSWORD`
3. You will need Kafka topic to read/write bind it to `KAFKA_TOPIC`
4. The access to the message queue is done via network ACL so you will need to contact HUDstats and ask them to whitelist your IP(s).
5. Python3 and `pip` installed.

# Examples

Make sure the dependencies are installed with `pip install -r requirements.txt`.

## Consumer
Start the consumer with the following command:
```
# KAFKA_BOOTSTRAP_SERVERS=b-1.example.com:1234,b-2.example.com:1234 KAFKA_SASL_USERNAME=`foo-user` KAFKA_SASL_PASSWORD='secret-password' KAFKA_TOPIC=outbound-messages python -m consume
```
In the reference implementation it'll read **ALL** messages in the specified topic. Exit with `Ctrl+C`.

## Producer
To produce single `Hello, world!` message use the following command:
```
# KAFKA_BOOTSTRAP_SERVERS=b-1.example.com:1234,b-2.example.com:1234 KAFKA_SASL_USERNAME=`foo-user` KAFKA_SASL_PASSWORD='secret-password' KAFKA_TOPIC=outbound-messages python -m produce
```

