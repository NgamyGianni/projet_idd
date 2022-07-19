import sys, numpy as np, os, time, math, mathplotlib
from rplidar import RPLidar


PORT_NAME = 'COM5'
#PORT_NAME = '/dev/tty.usbserial-0001'

def run(fileNames):
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    data = []
    dataPos = []
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for scan in lidar.iter_measurments():
            if(scan[1]==15):
                teta = math.radians(scan[-2])
                x = scan[-1] * math.cos(teta)
                y = scan[-1] * math.sin(teta)
                data.append([scan[-2],scan[-1]])
                dataPos.append([x,y])
            if ( len(data) > 300 ):
                break
            #create(fileName, data)
            #print(data)

    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()
    print(data)
    #np.save(path, np.array(data))
    create(fileNames[0], data)
    create(fileNames[1], dataPos)

def create(fileName, data):
    file = open(fileName, 'w')
    print("I save my data ")
    for elm in data:
        file.write(str(elm[0])+" , "+str(elm[1]))
        file.write("\n")
    file.close()


if __name__ == '__main__':
    fileName1 = "data-lidar.csv"
    fileName2 = "data-position.csv"
    run([fileName1,fileName2])
