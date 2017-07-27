#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import socket
import threading
import thread

IN1 = 11    
IN2 = 12
IN3 = 13
IN4 = 15

global loop_s
loop_s = "1"

def setStep(w1, w2, w3, w4):
	GPIO.output(IN1, w1)
	GPIO.output(IN2, w2)
	GPIO.output(IN3, w3)
	GPIO.output(IN4, w4)

def stop():
	setStep(0, 0, 0, 0)

def backward(delay, steps):  
	for i in range(0, steps):
		setStep(0, 0, 0, 1)
		time.sleep(delay)
		setStep(0, 0, 1, 0)
		time.sleep(delay)
		setStep(0, 1, 0, 0)
		time.sleep(delay)
		setStep(1, 0, 0, 0)
		time.sleep(delay)

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)       
	GPIO.setup(IN1, GPIO.OUT)      
	GPIO.setup(IN2, GPIO.OUT)
	GPIO.setup(IN3, GPIO.OUT)
	GPIO.setup(IN4, GPIO.OUT)

def loop():
	while True:
                while loop_s == "1":
                        backward(0.005, 64)

def destroy():
	GPIO.cleanup()             


def step_s():
        s = socket.socket()
        host = 'localhost'
        port = 12348 
        s.bind((host, port)) 
        s.listen(5)
        while True:
                c, addr = s.accept()
                global loop_s
                loop_s = c.recv(1024)
                print "loop_s = " + loop_s
                c.close()

class step_server (threading.Thread):  
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                  
        step_s()
 
class loop_t (threading.Thread):   
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                  
        loop()
        

thread1 = step_server(1, "Thread-1", 1)
thread2 = loop_t(2, "Thread-2", 2)


if __name__ == '__main__':     # Program start from here
	setup()
	try:
		thread1.start()
                thread2.start()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
		destroy()

