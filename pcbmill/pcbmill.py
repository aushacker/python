import json
import serial
import thread
import time

def dumpOut(ser):
    while True:
        print ser.readline()

def initInputs(intList):
    cmds = []
    for i in intList:
        pid = 'di' + str(i)
        cmds.append({pid + 'mo' : 0})
        cmds.append({pid + 'ac' : 2})
        cmds.append({pid + 'fn' : 1})
    return cmds

ser = serial.Serial('/dev/tty.usbmodem1411', 115200)

thread.start_new_thread(dumpOut, (ser, ))
 
time.sleep(5)

cmds = initInputs(range(1, 5))

#for c in cmds:
#    ser.write(json.dumps(c))
#    print json.dumps(c)
#
ser.write(b"$$")

while True:
    pass

