# import libraries
from flask import Flask, request, render_template, json, g
from .services import get_red, get_yellow, get_green, get_min, get_mid, get_max, get_up, get_down, get_left, get_right
from kafka import KafkaProducer
from gpiozero import LEDBoard, Servo, OutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory

# Define pin factories, LEDs, servo and robot motor pins
factory = PiGPIOFactory(host='192.168.0.10')
factory2 = PiGPIOFactory(host='192.168.0.23')
traffic_light = LEDBoard(17, 27, 23, pin_factory=factory)
servo = Servo(22, pin_factory=factory)
pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

# Define directions for the robot
def north():
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()

def south():
    pin1.off()
    pin2.on()
    pin3.off()
    pin4.on()

def east():
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()

def west():
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()

def stop_two():
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()

app = Flask(__name__)

# This creates the kafka producer
@app.before_request
def before_request():
    # Set up a Kafka producer
    TOPIC_NAME = 'gpio-service'
    KAFKA_SERVER = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    # Setting Kafka to g enables us to use this
    # in other parts of our application
    g.kafka_producer = producer

# This gracefully shuts down the app
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug server')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown_server():
    shutdown()
    return 'Server shutting down'

# This creates a message to confirm the app is working
@app.route('/status')
def health():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    return response

# This calculates metrics
@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":1,"UserCountActive":1}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')
    return response

# Main home page
@app.route('/')
def index():
    return render_template('gpio.html')

# Each function here will either control the device in GET or post the message in POST
@app.route('/red', methods=['GET', 'POST'])
def red():
    if request.method == 'GET':
        traffic_light.value = (1, 0, 0)
        return render_template('gpio.html')
    if request.method == 'POST':
        request_body = request.json
        result = get_red(request_body)
        return render_template('gpio.html', result=result), 202

@app.route('/yellow', methods=['GET', 'POST'])
def yellow():
    if request.method == 'GET':
        traffic_light.value = (0, 1, 0)
        return render_template('gpio.html')
    if request.method == 'POST':
        request_body = request.json
        result = get_yellow(request_body)
        return render_template('gpio.html', result=result), 202

@app.route('/green', methods=['GET', 'POST'])
def green():
    if request.method == 'GET':
        traffic_light.value = (0, 0, 1)
        return render_template('gpio.html')
    if request.method == 'POST':
        request_body = request.json
        result = get_green(request_body)
        return render_template('gpio.html', result=result), 202

@app.route('/min', methods=['GET', 'POST'])
def servo_min():
    if request.method == 'GET':
        servo.min()
        return render_template('gpio.html')
    if request.method == 'POST':
        request_body = request.json
        result = get_min(request_body)
        return render_template('gpio.html', result=result), 202

@app.route('/mid', methods=['GET', 'POST'])
def servo_mid():
    if request.method == 'GET':
        servo.mid()
        return render_template('gpio.html')
    if request.method == 'POST':
        request_body = request.json
        result = get_mid(request_body)
        return render_template('gpio.html', result=result), 202

@app.route('/max', methods=['GET', 'POST'])
def servo_max():
    if request.method == 'GET':
        servo.max()
        return render_template('gpio.html')
    if request.method == 'POST':
        request_body = request.json
        result = get_max(request_body)
        return render_template('gpio.html', result=result), 202

@app.route('/up', methods=['GET', 'POST'])
def forward():
    if request.method == 'GET':
        north()
        return render_template('gpio.html')
    if request.method == 'POST':
        stop_two()
        request_body = request.json
        result = get_up(request_body)
        return render_template('gpio.html', result=result), 202

@app.route('/down', methods=['GET', 'POST'])
def backward():
    if request.method == 'GET':
        south()
        return render_template('gpio.html')
    if request.method == 'POST':
        stop_two()
        request_body = request.json
        result = get_down(request_body)
        return render_template('gpio.html', result=result), 202

@app.route('/left', methods=['GET', 'POST'])
def left():
    if request.method == 'GET':
        west()
        return render_template('gpio.html')
    if request.method == 'POST':
        stop_two()
        request_body = request.json
        result = get_left(request_body)
        return render_template('gpio.html', result=result), 202

@app.route('/right', methods=['GET', 'POST'])
def right():
    if request.method == 'GET':
        east()
        return render_template('gpio.html')
    if request.method == 'POST':
        stop_two()
        request_body = request.json
        result = get_right(request_body)
        return render_template('gpio.html', result=result), 202


if __name__=='__main__':
    app.run(debug=True)
