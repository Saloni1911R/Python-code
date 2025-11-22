import serial
import time

arduino = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)  

while True:
    msg = input("Enter a number: ")   
    arduino.write((msg + "\n").encode()) 
    
    time.sleep(0.1)
    data = arduino.readline().decode().strip()  

    print("Arduino replied:", data)
