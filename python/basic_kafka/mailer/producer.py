from confluent_kafka import Producer
import json
import asyncio

producer = Producer({
    'bootstrap.servers': 'localhost:9092',
})

def delivery_callback(future):
    def __delivery_callback(err, msg):
        if err:
            future.set_exception(err)
        elif msg:
            future.set_result(msg)
    return __delivery_callback


async def produce(email: str, subject: str, text: str):
    data = {
        'subject': subject,
        'text': text
    }

    future = asyncio.Future()
    data_json = json.dumps(data)
    producer.produce(
        'send-mail', data_json, key=email, callback=delivery_callback(future)
    )
    await future
