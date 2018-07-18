from confluent_kafka import Producer


def main():
    producer = Producer({
        'bootstrap.servers': 'localhost:9092'
    })

    producer.produce('test-topic', b'Hello, Kafka.')
    # producer.poll(0)
    producer.flush()

if __name__ == '__main__':
    main()
    print('Complated ja.')
