import serial
import time

def tradMove(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    dx = x2 - x1
    dy = y2 - y1
    
    if dx != 0:
        if dx == 1:
            return "d"
        else:
            return "q"
    else:
        if dy == 1:
            return "z"
        else:
            return "s"
        
moves = [(0, j) for j in range(10)]
        
commands = [tradMove(moves[i], moves[i+1]) for i in range(len(moves)-1)]

ser = serial.Serial('/dev/ttyACM0')

for i in range(len(commands)):
    time.sleep(0.2)
    ser.write(commands[i].encode())