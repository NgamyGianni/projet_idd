import a_star
import subarea
import time
import datalidar
import serial
import numpy as np

"""ser = serial.Serial('/dev/ttyACM0')

for i in range(len(commands)):
    time.sleep(0.2)
    ser.write(commands[i].encode())"""

if __name__ == "__main__":
    # robot size adn gap from robot to cell
    long_rb = 400.  # 40 cm
    larg_rb = 400.  # 40 cm
    gap = 0.  # 10 cm

    # length of the table
    length_tb = 3000

    # width of the table
    width_tb = 2000  # 2 m

    # cell_size of the area
    size_of_cell = subarea.cell_size(long_rb, larg_rb, gap)

    # matrix shape
    matrix_shape = subarea.size_table_to_matrix(
        length_tb, width_tb, size_of_cell)

    # source point
    ind_dep = int((matrix_shape[0] - 1)/2)
    point_dep = (ind_dep, 0)

    # target point
    point_arr = (ind_dep, matrix_shape[1] - 1)

    filename1 = "data-lidar.csv"
    filename2 = "data-position.csv"

    # Get from Lidar
    datalidar.run([filename1, filename2])

    # # Initialize the area subdivision
    # matrix = subarea.init_matrix_subdivision(matrix_shape)

    # Get from the file
    points = subarea.read_file("data-position.csv")

    current = point_dep

    while current != point_arr:
        
        # Initialize the area subdivision
        matrix = subarea.init_matrix_subdivision(matrix_shape)

        subarea.update_matrix_subdivision(
            filename2, size_of_cell, current, matrix)

        path = a_star.astar(matrix, current, point_arr)

        commands = a_star.commands(path)

        #a_star.affiche_matrix(matrix, path)

        # ser = serial.Serial('/dev/ttyACM0')

        # if commands[0] == "z" or commands[0] == 's':
        #     for i in range(100):
        #         time.sleep(0.01)
        #         ser.write(commands[0].encode())
        # else:
        #     for i in range(100):
        #         time.sleep(0.01)
        #         ser.write(commands[0].encode())
        if path is not None:
            current = path[1]
        datalidar.run([filename1, filename2])
        

# 3 coups lat
# 2 coups avancer/reculer
