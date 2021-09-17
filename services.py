# import libraries
import json
from .app import g

# Each function defines a message that will be sent to the consumer 
def get_red(red_data):
    red_data = {"id" : 1 , "status": "stop"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(red_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)
    
def get_yellow(yellow_data):
    yellow_data = {"id" : 2 , "status": "slow"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(yellow_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)

def get_green(green_data):
    green_data = {"id" : 3 , "status": "go"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(green_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)

def get_min(min_data):
    min_data = {"id" : 1 , "position": "min"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(min_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)

def get_mid(mid_data):
    mid_data = {"id" : 2 , "position": "mid"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(mid_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)
    
def get_max(max_data):
    max_data = {"id" : 3 , "position": "max"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(max_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)

def get_up(up_data):
    up_data = {"id" : 1 , "direction": "up"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(up_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)

def get_down(down_data):
    down_data = {"id" : 2 , "direction": "down"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(down_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)

def get_left(left_data):
    left_data = {"id" : 3 , "direction": "left"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(left_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)

def get_right(left_data):
    right_data = {"id" : 4 , "direction": "right"}
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(right_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("gpio-service", kafka_data)

