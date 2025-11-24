import serial
import time

arduino = serial.Serial('COM4', 115200, timeout=1)
time.sleep(2)   # wait for Arduino to reset

while True:
    msg = input("Enter a number: ")
    if msg.strip() == "":
        continue

    arduino.write((msg + "\n").encode())

    time.sleep(0.2)  # give Arduino time to reply

    data = arduino.readline().decode('utf-8').strip()
    print("Arduino replied:", data)
