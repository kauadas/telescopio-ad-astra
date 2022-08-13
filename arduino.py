import serial

def write(x):
    arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

    print(bytes(x))
    arduino.write(bytes(x))

def read():
    arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
    return arduino.readline()


