#Project Brover @2020
#Simon Stoll
from Sonic_sensor import *
import RPi.GPIO as GPIO
import time
import sqlite3
conn = sqlite3.connect('Sensordata.db')
GPIO.setmode(GPIO.BCM)

#
TRIG1 = 14
ECHO1 = 15
ANG1 = 'front'


TRIG2 = 18
ECHO2 = 23
ANG2 = 180

setup(TRIG1,ECHO1)
pulse_duration = trigger(TRIG1,ECHO1)
dist = distance(pulse_duration)

#Add server for database
conn.execute("INSERT INTO Sonic ('distance') \
    VALUES (" + dist + ")");
conn.commit()

setup(TRIG2,ECHO2)
pulse_dur = trigger(TRIG2,ECHO2)
dist = distance(pulse_duration)

conn.execute("INSERT INTO Sonic ('distance') \
     VALUES (" + dist + ")");
conn.commit()
conn.close()