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
    return long_rb + gap, larg_rb + gap 

# Initialize the area subdivision
# sub_arr takes two values:  0 (i.e no obstacle) or  1 (i.e obstacle)
def init_matrix_subdivision(long_rb, larg_rb, gap, larg_table, point_arr):
    long, larg = cell_size(long_rb, larg_rb, gap)
    long_route = point_arr[0] + long

    # row and column
    nbre_ligne = int(larg_table/larg)
    nbre_colonne = int(long_route/long)

    # matrix of subdivision area
    sub_area = list(np.zeros((nbre_ligne, nbre_colonne)))
    return long, larg, sub_area


def point_to_indices(point, width, height):
    #height and width resp (row and column)
    if point[1] >= 0:
        return [int((point[1] + height/2.)/height), int((point[0] + width/2.)/width)]
    else:
        return [int((point[1] - height/2.)/height), int((point[0] + width/2.)/width)]

def abscisse_obstacles(points, width, height):
    indices_obs = []
    for point in points:
        indices_obs.append(point_to_indices(point, width, height))
    return indices_obs

def min_indices_column(indices):
    indice_column = indices[0][1]
    #is_checked = False
    for ind in indices:
        if 0 < indice_column < ind[0][1]:
            indice_column = ind
    return indice_column


def update_matrix_subdivision(filename, width, height, index_rb, matrix):
    points = read_file(filename)
    indices_obs = abscisse_obstacles(points, width, height)
    print(np.shape(matrix))
    for ind_obs in indices_obs:
        row = index_rb[0] - ind_obs[0]
        column = index_rb[1] + ind_obs[1]
        if row < np.shape(matrix)[0] and column < np.shape(matrix)[1] :
            #print("row " + str(row) + " "+ str(column) )
            matrix[row][column] = 1
    print("nouvelle matrice")
    print(np.array(matrix))


if __name__ == "__main__":
    # robot size adn gap from robot to cell
    long_rb = 400. # 40 cm
    larg_rb = 400. # 40 cm
    gap = 4. # 10 cm

    # width of the table
    larg_table = 2000  # 2 m

    # coordinaate of the aim point
    # lenght table 3m
    point_arr = [3000, 5] 

    # index p the source point
    ind_rb_i = int(larg_table / ( 2. * (larg_rb + 2. * gap) ) )
    index_rb = [ind_rb_i,0]

    # All obstacle points from the lidar
    filename = "data-position.csv"

    width, height, matrix = init_matrix_subdivision(
        long_rb, larg_rb, gap, larg_table, point_arr)

    update_matrix_subdivision(filename, width, height, index_rb, matrix)
    cell_length, cell_width = cell_size(long_rb, larg_rb, gap)
    print(cell_length, cell_width )
    print(np.shape(matrix))
    print(matrix)
    
    
    
