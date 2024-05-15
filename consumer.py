import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

def receive_messages(user_queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare exchange and queue
    channel.exchange_declare(exchange='chat_exchange', exchange_type='direct')
    channel.queue_declare(queue=user_queue)

    # Bind the queue to the exchange with a routing key
    channel.queue_bind(exchange='chat_exchange', queue=user_queue, routing_key=user_queue)

    channel.basic_consume(queue=user_queue, on_message_callback=callback, auto_ack=True)

    print(f" [*] Waiting for messages in {user_queue}. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    user_queue = 'user1'
    receive_messages(user_queue)
