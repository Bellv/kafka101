from confluent_kafka import Consumer

def main():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'YiM',
        'default.topic.config': {
            'auto.offset.reset': 'earliest'
        }
    })

    consumer.subscribe(['test-topic'])
    while(True):
        message = consumer.poll(1.0)
        if message is not None:
            print('message {}', message.value())

if __name__ == '__main__':
    main()
