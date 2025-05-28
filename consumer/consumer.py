from kafka import KafkaConsumer, errors
import json
import psycopg2
import time

def wait_for_kafka(bootstrap_servers, retries=10, delay=5):
    for i in range(retries):
        try:
            consumer = KafkaConsumer(
                bootstrap_servers=bootstrap_servers,
                api_version_auto_timeout_ms=3000
            )
            consumer.close()
            print("Kafka está disponível!")
            return True
        except errors.NoBrokersAvailable:
            print(f"Kafka não disponível, tentativa {i+1} de {retries}. Esperando {delay} segundos...")
            time.sleep(delay)
    return False

if not wait_for_kafka(['kafka:9092']):
    print("Kafka não ficou disponível após várias tentativas. Abortando.")
    exit(1)

print("Esperando o banco de dados...")
time.sleep(15)

conn = psycopg2.connect(
    dbname="sensores",
    user="user",
    password="password",
    host="db"
)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensores (
        id SERIAL PRIMARY KEY,
        sensor_id TEXT,
        timestamp TEXT,
        temperature REAL,
        humidity REAL
    )
''')
conn.commit()

consumer = KafkaConsumer(
    'iot_sensors',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    data = message.value
    print(f"Received: {data}")
    cursor.execute('''
        INSERT INTO sensores (sensor_id, timestamp, temperature, humidity)
        VALUES (%s, %s, %s, %s)
    ''', (data['sensor_id'], data['timestamp'], data['temperature'], data['humidity']))
    conn.commit()