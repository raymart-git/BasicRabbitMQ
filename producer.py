import pika

def send_message(chat_message, user_queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare exchange and queue
    channel.exchange_declare(exchange='chat_exchange', exchange_type='direct')
    channel.queue_declare(queue=user_queue)

    # Publish message to the exchange with a routing key
    channel.basic_publish(exchange='chat_exchange', routing_key=user_queue, body=chat_message)
    print(f" [x] Sent {chat_message} to {user_queue}")

    connection.close()

if __name__ == "__main__":
    user_queue = 'user1'
    chat_message = 'Hello, this is a test message!'
    send_message(chat_message, user_queue)
