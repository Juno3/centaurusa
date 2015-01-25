from ioman import Pcduinoman # Use the PCDuino Library for the general controls
import sys
import datetime
import time

pcd = Pcduinoman()
input_pin = 3
output_pin = 2

def doTestInit():
    sys.stdout.write('Start test - ' + str(datetime.datetime.now()) + '\n')
    pcd.setMode(output_pin,pcd.MODE_OP) # out
    pcd.setMode(input_pin,pcd.MODE_IP) # in
      
def doTestMain():
    sys.stdout.write('Write 2 to l Low ' + str(datetime.datetime.now()) + '\n')
    pcd.digitalWrite(output_pin,pcd.STATE_LOW)
    time.sleep(1) # delays for 5 secondssys
    sys.stdout.write('Write 2 to l Hi ' + str(datetime.datetime.now()) + '\n')
    pcd.digitalWrite(output_pin,pcd.STATE_HIGH)
    time.sleep(1) # delays for 5 secondssys
    sys.stdout.write('Get pin 3 - ' + str(pcd.digitalRead(input_pin)) + '\n')
    time.sleep(1) # delays for 5 secondssys

def doGo():
    doTestInit()
    while(True):
        doTestMain()
    
doGo()
