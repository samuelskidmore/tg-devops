from kafka import KafkaProducer
import json
import time

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'
TOPIC = 'my_topic'

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_data():
    # Example data structure matching TigerGraph loading job schema
    return {
        'person_id': '123',
        'name': 'Alice',
        'age': 30,
        'friend_id': '456'
    }

def monitor_kafka_size(topic):
    # Placeholder function for monitoring Kafka size
    return False  # Implement actual logic for checking size

while True:
    if not monitor_kafka_size(TOPIC):
        data = get_data()
        producer.send(TOPIC, value=data)
        print(f'Sent: {data}')
    else:
        print('Kafka topic size limit reached, waiting...')
        time.sleep(10)

    time.sleep(1)  # Adjust rate of sending messages as needed
