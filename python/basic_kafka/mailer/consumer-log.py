import json

from confluent_kafka import Consumer
from . import send_mail


def main():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'send-log',
        'default.topic.config': {
            'auto.offset.reset': 'earliest'
        }
    })

    consumer.subscribe(['send-mail'])
    while(True):
        message = consumer.poll(1.0)
        if message:
            data = json.loads(message.value())
            email = message.key().decode('utf-8')
            print ('email: ' + email)
            print (data)

if __name__ == '__main__':
    main()
