import sys, numpy as np, csv, math, matplotlib.pyplot as plt
from turtle import undo

from rplidar import RPLidar
import a_star

PORT_NAME = 'COM5'
# PORT_NAME = '/dev/tty.usbserial-0001'

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
                if(scan[-1]<1000) and (x>=0):
                    data.append([scan[-2],scan[-1]])
                    dataPos.append([x,y])
            if ( len(data) > 1000 ):
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
        #if len(voisins(data, elm[0], elm[1], 10)) > 10 :
        file.write(str(elm[0])+" , "+str(elm[1]))
        file.write("\n")
    file.close()


def gui(filename):
    x = []
    y = []

    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            xv = float(row[0].strip())
            yv = float(row[1].strip())
            if (len(x) > 0):
                if int(xv) != x[-1]:
                   x.append(int(xv/50))
            else:
                x.append(int(xv/50))
            if (len(y) > 0):
                if int(yv) != y[-1]:
                   y.append(int(yv/50))
            else:
                y.append(int(yv/50))
    ymax = int(max(y))
    xmax = int(max(x))
    ymin = int(min(y))
    xmin = int(min(x))

    matrix = [[0 for y in range(ymin,ymax+1)] for x in range(xmin,xmax+1)]
    print(x)
    print(y)
    for yvalue in y:
        yval = yvalue+abs(ymin)
        for xvalue in x:
            xval = xvalue+abs(xmin)
             #print(int(xvalue),yvalue)
            #print("max matrix " + str(len(matrix)))
            #print("max yvlaue " + str(xmax))
            matrix[xval][yval] = 1

   # print(max(y))
   # print(matrix)
    #matrix.reverse()
    return (x,y,matrix)
   # plt.plot(x, y,".")
   # plt.show()

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return math.sqrt(((x1-x2)**2) + ((y1-y2)**2))

def voisins(points, x, y, seuil):
    return {(a, b) for (a, b) in points if distance((x, y), (a, b)) < seuil}


if __name__ == '__main__':
    fileName1 = "data-lidar.csv"
    fileName2 = "data-position.csv"
    #run([fileName1, fileName2])
    gui(fileName2)
    x,y,matrix = gui(fileName2)
    for m in matrix:
        print(m)
    print(len(matrix))

    start = (0
             , 0)
    end = (10, 4)
"""
    path = a_star.astar(matrix, start, end)
    for step in path:
        matrix[step[0]][step[1]] = 2
    for row in matrix:
        line = []
        for col in row:
            if col == 1:
                line.append("\u2588")
            elif col == 0:
                line.append(" ")
            elif col == 2:
                line.append(".")
        print("".join(line))
        """
plt.plot(x, y,".")
"""unzipped_list = [[i for i, j in path],
                 [j for i, j in path]]
print(len(unzipped_list[0]),len(unzipped_list[1]))
plt.plot(unzipped_list[0],unzipped_list[1])
"""
plt.show()
