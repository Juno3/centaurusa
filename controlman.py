#!/usr/bin/python
#-*- coding: utf-8 -*-
# Name: controlman.py
# Description: General Control Manager
# Author: S. Ajodha
# - 2015-01-12: Created
from ioman import Pcduinoman # Use the PCDuino Library for the general controls
import datetime
import sys
# Switch types are defined in the database, codes as follows:
# - 3 Toggle
# - 4 Momentary
# - 
class ButtonIO:

    io_controller = Pcduinoman()
    inputPin=0
    switchType=0
    debounceDelay = 50 #ms
    currentState = 0
    checkTime = datetime.datetime.now()

    # Call each time to check the state, if the check state is True, the state has changed
    def checkState(self):
        # Check if state changed
        elapsed_msecs = (datetime.datetime.now() - self.checkTime).microseconds
        #sys.stdout.write('Elapsed - ' + str(elapsed_msecs) + '\n\n')
        current_ip_state = self.io_controller.digitalRead(self.inputPin)
        if(current_ip_state != self.currentState): # State changed
            self.checkTime = datetime.datetime.now() # Register change time
            if(elapsed_msecs > self.debounceDelay): # bigger than debounce, use
                self.currentState = current_ip_state
                return True # statechanged
        return False # if here state has not changed according to required delay

    def getState(self):
        return self.currentState
    
    #Setup the state
    def __init__(self,input_pin,debounce_interval):
        self.debounceDelay = debounce_interval
        self.inputPin = input_pin
        self.io_controller.setMode(self.inputPin,self.io_controller.MODE_IP) # Set input pin mode
        self.currentState = self.io_controller.digitalRead(self.inputPin)
        self.checkTime = datetime.datetime.now()

    
