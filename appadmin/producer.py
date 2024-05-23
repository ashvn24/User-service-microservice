import json
import pika
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up connection parameters
params = pika.URLParameters('amqps://hjbmtads:qOh03ewMbJOTgf_g2osT6DpZp7UFVqcj@puffin.rmq2.cloudamqp.com/hjbmtads')

class RabbitMQProducer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RabbitMQProducer, cls).__new__(cls, *args, **kwargs)
            cls._instance.connect()
        return cls._instance

    def connect(self):
        try:
            self.connection = pika.BlockingConnection(params)
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='main')
            logger.info("Connected to RabbitMQ")
        except pika.exceptions.AMQPConnectionError as e:
            logger.error(f"Connection failed: {e}")
            time.sleep(5)
            self.connect()

    def publish(self,method, body):
        if not self.channel.is_open:
            self.connect()
        try:
            properties = pika.BasicProperties(method)
            self.channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
            logger.info(f"body published: {body}")
        except pika.exceptions.AMQPError as e:
            logger.error(f"Failed to publish body: {e}")
            self.connect()
            self.channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body))

    def close(self):
        if self.channel.is_open:
            self.channel.close()
        if self.connection.is_open:
            self.connection.close()
        logger.info("Connection closed")
