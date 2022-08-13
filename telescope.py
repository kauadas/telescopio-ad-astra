import arduino
import os
import cv2
import weather

def shotNormal():
    camera = cv2.VideoCapture(0)

    i = 34
    while True:
        retval, img = camera.read()
        if not "NoneType" in str(type(img)):
            break

        else:
            
            i -= 1

        if i == 0:
            
            return "sem sinal de imagem :("
        
    
    file = "image"
    oldfile = file
    i = 0
    while True:
        if os.path.isfile(file+".png"):
            i+=1
            file = oldfile+f"{i}"

        else:
            break

    

    cv2.imwrite(file+".png",img)
    camera.release()
    return "pronto :D"

def shotIr():
    camera = cv2.VideoCapture(1)
    i = 34

    while True:
        retval, img = camera.read()
        if not "NoneType" in str(type(img)):
            break

        else:
            i -= 1

        if i == 0:
            
            return "sem sinal de imagem :("

    file = "imageIr"
    oldfile = file
    i = 0
    while True:
        if os.path.isfile(file+".png"):
            i+=1
            file = oldfile+f"{i}"

        else:
            break

    cv2.imwrite(file+".png",img)
    camera.release()
    return "pronto :D"



shots = 32
shotsIr = 16
def move(x: float,y: float):
    x = (x/10**6)*360
    y = (y/10**6)*360

    movecmd = f"move {x} {y}"
    arduino.write(movecmd)

    while True:
        text = arduino.read()

        if text == bytes("movement complete"):
            for i in range(shots):
                shotNormal()

            for i in range(shotsIr):
                shotIr()

            break

print(shotNormal())
print(shotIr())