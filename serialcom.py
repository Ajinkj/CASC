import serial
import time

serialcomm = serial.Serial('COM4',9600)
serialcomm.timeout= 1

while True:
    i = input("input").strip()
    if i == 'done':
        print("finished programe")
        break
    serialcomm.write(i.encode())
    time.sleeep(0.5)
    print(serialcomm.readline().decode('ascii'))
serialcomm.close()