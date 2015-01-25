from controlman import ButtonIO # Use the PCDuino Library for the general controls
from ioman import Pcduinoman
import sys
import datetime
import time


input_pin = 3
output_pin = 2
but = ButtonIO(input_pin,500)
pcd = Pcduinoman()

def doTestInit():
    sys.stdout.write('Start test - ' + str(datetime.datetime.now()) + '\n')
    pcd.setMode(output_pin,pcd.MODE_OP)
    
def doTestMain():
    out_val = 0
    if but.checkState():
        sys.stdout.write('\nChanged in 3 - ' + str(but.getState()))
        sys.stdout.write('\n2 State - ' + str(pcd.digitalRead(output_pin)))
        if (but.getState() == 1): # Raised
            if (pcd.digitalRead(output_pin) == 1):
                out_val = 0
            else:
                out_val = 1
            pcd.digitalWrite(output_pin,out_val)
        
def doGo():
    doTestInit()
    while(True):
        doTestMain()
    
doGo()
