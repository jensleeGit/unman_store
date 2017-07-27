#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import socket
import threading
import time
import thread

global loop_s 
loop_s = "1"

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Press Ctrl-C to stop."


def client_0():
    s = socket.socket()         # 创建 socket 对象
    host = 'localhost'          # 获取本地主机名
    port = 12348                # 设置端口好
    s.connect((host, port))
    s.send("0")
    s.close()


def client_1():
    s = socket.socket()         # 创建 socket 对象
    host = "localhost"          # 获取本地主机名
    port = 12348                # 设置端口好
    s.connect((host, port))
    s.send("1")
    s.close()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    if loop_s == "0":
        client_0()
    elif loop_s == "1":
        client_1()
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    
        if str(uid[0]) == "118" and str(uid[1])== "152" and str(uid[2]) == "106" and str(uid[3]) == "123":
            loop_s = "0"
            print "loop_s = 0"
            client_0()

        elif str(uid[0]) == "182" and str(uid[1])== "173" and str(uid[2]) == "115" and str(uid[3]) == "91":
            loop_s = "1"
            print "loop_s = 1"
            client_1()

