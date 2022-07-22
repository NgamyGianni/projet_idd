#from os import read
import re
import numpy as np


def read_file(filename):
    file = open(filename, "r")
    data = re.split("\n", file.read())
    points = []
    val = []
    for i, elt in enumerate(data):
        val = re.split(",", elt)
        points.append([float(val[0]), float(val[1])])

    file.close()
    return points

def cell_size(long_rb, larg_rb, gap):  # long and larg in mm
    #return lenght, width
    #return (long_rb + gap, larg_rb + gap)
    return (long_rb/2 + gap, larg_rb/2 + gap)


def size_table_to_matrix(length_tb, width_tb, size_of_cell):

    # width_tb = largeur de la table
    nb_rows = int(width_tb/size_of_cell[1])  

    # length_tb = longueur de la table
    nb_columns = int(length_tb/size_of_cell[0]) 

    
    return (nb_rows, nb_columns)



# Initialize the area subdivision
# sub_arr takes two values:  0 (i.e no obstacle) or  1 (i.e obstacle)
def init_matrix_subdivision(matrix_shape):
    return list(np.zeros(matrix_shape))
    


def point_to_indices(point, size_of_cell):
    width = size_of_cell[0]
    height = size_of_cell[1]
    #height and width resp (row and column)
    if point[1] >= 0:
        return [int((point[1] + height/2.)/height), int((point[0] + width/2.)/width)]
    else:
        return [int((point[1] - height/2.)/height), int((point[0] + width/2.)/width)]


def abscisse_obstacles(points, size_of_cell):
    indices_obs = []
    for point in points:
        indices_obs.append(point_to_indices(point, size_of_cell))
    return indices_obs

def min_indices_column(indices):
    indice_column = indices[0][1]
    #is_checked = False
    for ind in indices:
        if 0 < indice_column < ind[0][1]:
            indice_column = ind
    return indice_column


def update_matrix_subdivision(filename, size_of_cell, index_rb, matrix):
    points = read_file(filename)
    indices_obs = abscisse_obstacles(points, size_of_cell)

    print(np.shape(matrix))
    for ind_obs in indices_obs:
        row = index_rb[0] - ind_obs[0]
        column = index_rb[1] + ind_obs[1]
        if -1< row < np.shape(matrix)[0] and -1< column < np.shape(matrix)[1] :
            #print("row " + str(row) + " "+ str(column) )
            matrix[row][column] = 1
        # else:
        #     mat
    # print("nouvelle matrice")
    # print(np.shape(matrix))
    # print(np.array(matrix))


if __name__ == "__main__":
    # robot size adn gap from robot to cell
    long_rb = 400. # 40 cm
    larg_rb = 400. # 40 cm
    gap = 4. # 10 cm

    # length of the table
    length_tb = 3000

    # width of the table
    width_tb = 2000  # 2 m

    # cell_size of the area
    size_of_cell = cell_size(long_rb, larg_rb, gap)

    # matrix shape
    matrix_shape = size_table_to_matrix(length_tb, width_tb, size_of_cell)

    # source point
    ind_dep = int( (matrix_shape[0] - 1)/2 )
    point_dep = (ind_dep, 0)

    # target point
    point_arr = (ind_dep, matrix_shape[1] - 1)

    # All obstacle points from the lidar
    filename = "data-position.csv"

    matrix = init_matrix_subdivision(matrix_shape)

    update_matrix_subdivision(filename, size_of_cell, point_dep, matrix)
    # cell_length, cell_width = cell_size(long_rb, larg_rb, gap)
    # print(cell_length, cell_width )
    # print(np.shape(matrix))
    # print(matrix)
    
    
    
