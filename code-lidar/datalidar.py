import sys, numpy as np, csv, math, matplotlib.pyplot as plt
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
    #np.save(path, np.array(data))
    create(fileNames[0], data)
    create(fileNames[1], dataPos)
    gui(fileNames[1])

def create(fileName, data):
    file = open(fileName, 'w')
    print("I save my data ")
    for elm in data:
        file.write(str(elm[0])+" , "+str(elm[1]))
        file.write("\n")
    file.close()

def gui(filename):
    x = []
    y = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            x.append(float( (row[0].strip()) ))
            y.append(float((row[1].strip())))
    print(x)
    print(y)
    plt.plot(x, y,".")
    plt.show()
if __name__ == '__main__':
    fileName1 = "data-lidar.csv"
    fileName2 = "data-position.csv"
    run([fileName1, fileName2])
