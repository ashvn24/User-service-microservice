import pika


params = pika.URLParameters('amqps://hjbmtads:qOh03ewMbJOTgf_g2osT6DpZp7UFVqcj@puffin.rmq2.cloudamqp.com/hjbmtads')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='appadmin')

def callback(ch, method, properties, body):
    print('Recieved in admin')
    print(body)

channel.basic_consume(queue='appadmin', on_message_callback=callback)

print('started')

channel.start_consuming()

channel.close()