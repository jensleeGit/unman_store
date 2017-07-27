#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import mysql.connector
from sqlalchemy import Column, Integer,String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#############################################################################################
#sql

# 创建对象的基类:
Base = declarative_base()


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/epay')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

class Detail(Base):
    __tablename__ = 'commodity_detail'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20))
    price =  Column(Integer)
    uid =  Column(String(20))

class Commo(Base):
    __tablename__ = 'commodity'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20))
    price =  Column(Integer)
    uid =  Column(String(20))

def if_uid_in_commodity():
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(Commo).filter(Commo.uid==uid_str).first()
    # 打印类型和对象的name属性:
    if user:
        pass
    else:
        user = session.query(Detail).fliter(Detail.uid==uid_str).first()
        global name
        global price

        #g_name = user.name
        #g_price = user.price
    
        new_user = Commo( name=user.name,price=user.price,uid=uid_str)
        # 添加到session:
        session.add(new_user)
        # 提交即保存到数据库:
        session.commit()

    # 关闭Session:
    session.close()

def if_uid_in_commodity(uid_str):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(Commo).filter(Commo.uid==uid_str).first()
    # 打印类型和对象的name属性:
    if user:
        session.close()
    else:
        session.close()
        insert_commodity()
        
def insert_commodity():
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    user = session.query(Detail).filter(Detail.uid==uid_str).first()
    global g_name
    global g_price
    
    new_user = Commo( name=user.name,price=user.price,uid=uid_str)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close() 

def delete_commodity():
    conn = mysql.connector.connect(user='root', password='root', database='epay', use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('TRUNCATE TABLE commodity')
    cursor.close()
    conn.close()
###########################################################################################
#rfid

global card_detected
card_detected = 0

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
print "欢迎来到E-pay无人售货店"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    card_detected = 0
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
        card_detected = 1
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

        uid_str = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])

    if card_detected == 1:
        if_uid_in_commodity(uid_str)
    elif card_detetcted ==0 :    
        delete_commodity()
    
    
        
 
