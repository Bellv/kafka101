import json

from confluent_kafka import Consumer
from . import send_mail


def main():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'send-mail',
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
            send_mail.send_mail(
                email,
                data['subject'],
                data['text']
            )

if __name__ == '__main__':
    main()
