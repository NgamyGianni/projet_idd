import sys
import numpy as np
import os
from rplidar import RPLidar


#PORT_NAME = '/dev/ttyUSB0'
PORT_NAME = '/dev/tty.usbserial-0001'

def run(fileName):
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    data = []
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for scan in lidar.iter_scans():
            data.append(np.array(scan))
            #create(fileName, data)
            #print(data)
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()
    #np.save(path, np.array(data))
    create(fileName, data)

def create(fileName, data):
    file = open(fileName, 'w')
    print("I save my data ")
    file.write(str(data))
    file.close()


if __name__ == '__main__':
    fileName ="data-lidar.txt"
    run('lidar_data.txt')
