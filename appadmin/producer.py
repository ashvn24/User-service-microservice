import pika


params = pika.URLParameters('amqps://hjbmtads:qOh03ewMbJOTgf_g2osT6DpZp7UFVqcj@puffin.rmq2.cloudamqp.com/hjbmtads')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='appadmin', body='helo')