#!/usr/bin/python
#-*- coding: utf-8 -*-
# Name: ioman.py
# Description: PCDuino IO Management module. Utility module to translate pcduino specific library to general library
# Author: S. Ajodha
# - 2015-01-11: Created

import gpio # pcdiuno Library

class Pcduinoman:

    MODE_IP = 0
    MODE_OP = 1
    STATE_LOW = 0
    STATE_HIGH = 1

    def __init__(self):
        return     
        
    def setMode(self,pin_no,pin_mode):
        gpio.pinMode(self.getPin(pin_no),self.getPinMode(pin_mode))

    def getPin(self,pin_no):
        return 'gpio' + str(pin_no)

    def getPinMode(self,pin_mode):
        return pin_mode

    def getPinValue(self,pin_value):
        return pin_value

    def digitalWrite(self,pin_no,pin_value):
        gpio.digitalWrite(self.getPin(pin_no),self.getPinValue(pin_value))

    def digitalRead(self,pin_no):
        return gpio.digitalRead(self.getPin(pin_no))
