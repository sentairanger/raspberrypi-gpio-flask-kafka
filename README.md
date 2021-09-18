# raspberrypi-gpio-flask-kafka

## Introduction

This application is based on what I learned from the Message Passing Course of the Cloud Native Architecture Nanodegree from Udacity. The app uses Kafka and flask. Here, the application works as follows:  

* The flask app which also acts as the producer in which it sends information to the kafka consumer. 
* The kafka service acts as the consumer listening to any messages it will get. The messages it receives are in JSON format. The flask app will send a message every time a GPIO device is activated such as and LED, servo or motor. This is helpful if you're troubleshooting any electronics. 

## Getting Started

To replicate this yourself, here are some requirements you will need, but you can always substitute if you wish.

### Hardware

* Raspberry Pi 3B+ or any other Raspberry Pi.
* 3 LEDs of any color (you can add more if you wish)
* 3 220 Ohm resistors (or more if you need and you can also substitute a higher value)
* 9G Servo motor (you can add more or use any servo motor you wish)
* A robot(Or you can skip this part if you want just make sure to update the code)

### Software

* Raspberry Pi OS or OS Lite
* Python 3, for Mac and Windows users install from the main website
* `requirements.txt` file to install the needed modules
* Kafka, Download from the main site. If you are a Windows user the documentation to install is very different since Windows uses Powershell rather than the typical bash shell.

## Running the Code

To run the code first clone the repo and then open several terminals from the directory where the repo was cloned or Powershells. If on Windows use PuTTy to SSH into your Raspberry Pis. On Mac and Linux just be sure to SSH using the terminal. I have provided the `kafka-process.txt` file to show you how to run the Kafka service. First run the zookeeper in one termina, the Kafka service in the other terminal, set up the gpio-service topic and then create the consumer on another terminal. Then open another terminal to run the flask app. Then go to `http://127.0.0.1:5000` on any browser. There you should be able to run the app. When you turn on any GPIO device, the Kafka consumer will print a JSON statement showing that the device has been pressed. 

## Screenshot

* ![app](https://github.com/sentairanger/raspberrypi-gpio-flask-kafka/blob/main/Screenshot%20from%202021-09-16%2015-36-48.png)
