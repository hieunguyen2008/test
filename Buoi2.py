print("Sensors and Actuators")

import time
import serial.tools.list_ports


try:
    ser = serial.Serial(port="COM5", baudrate = 9600)
    print("Opened the port")
except:
    print("Can not open the port")

def sendCommand(cmd):
	ser.write(cmd.encode())


mess = ""


def processData(data, client):
	print(data)
	data = data.replace("!", "")
	data = data.replace("#", "")
	splitData = data.split(":")
	print(splitData)
	if splitData[1] == "T":
		client.publish("sensor1", splitData[2])
	elif splitData[1] == "H":
		client.publish("sensor2", splitData[2])

def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1], client)
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

# while True:
# 	readSerial()
# 	time.sleep(1)


# while True:
# 	sendCommand("0");
# 	time.sleep(5)
# 	sendCommand("1");
# 	time.sleep(5)
# 	sendCommand("2");
# 	time.sleep(5)
# 	sendCommand("3");
# 	time.sleep(5)