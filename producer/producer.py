import socket
import time
from kafka import KafkaProducer
from faker import Faker
import json
import random

def wait_for_kafka(host, port, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((host, port), timeout=2):
                print("Kafka está pronto!")
                return
        except Exception:
            print("Esperando o Kafka ficar disponível...")
            time.sleep(2)
    raise Exception("Kafka não ficou disponível a tempo.")

wait_for_kafka("kafka", 9092)

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_sensor_data():
    return {
        'sensor_id': fake.uuid4(),
        'timestamp': fake.iso8601(),
        'temperature': round(random.uniform(15, 35), 2),
        'humidity': round(random.uniform(30, 90), 2)
    }

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        producer.send('iot_sensors', value=data)
        print(f"Sent: {data}")
        time.sleep(2)