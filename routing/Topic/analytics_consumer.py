import pika
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, body):
    print(f"analytics consumer recive received message {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mytopicex', exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='mytopicex', queue=queue.method.queue, routing_key='*.user.*')

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)


print("Start consuming messages")

channel.start_consuming()