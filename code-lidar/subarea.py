#from os import read
import re
import numpy as np


def read_file(filename):
    file = open(filename, "r")
    data = re.split("\n", file.read())
    #print(data)
    points = []
    val = []
    for elt in data:
        val = re.split(",", elt)
        ###print(val)
        points.append([float(val[0]), float(val[1])])
    file.close()
    # print(points)
    return points

def cell_size(long_rb, larg_rb, gap):  # long and larg in mm
    #return width, height
    return long_rb+2.*gap, larg_rb+2.*gap 

# Initialize the area subdivision
# sub_arr takes two values:  0 (i.e no obstacle) or  1 (i.e obstacle)
def init_matrix_subdivision(long_rb, larg_rb, gap, larg_table, point_arr):
    long, larg = cell_size(long_rb, larg_rb, gap)
    # print("each square width " + str(long) )
    # print("each square height " + str(larg))
    long_route = point_arr[0] + long
    nbre_ligne = int(larg_table/larg)
    nbre_colonne = int(long_route/long)
    # print("nbre ligne " + str(nbre_ligne) + " de type " + str(type(nbre_ligne)))
    # print("nbre colonne " + str(nbre_colonne) +
    #       " de type " + str(type(nbre_colonne)))
    sub_area = list(np.zeros((nbre_ligne, nbre_colonne)))
    # print(np.shape(sub_area))
    #sub_area[int(larg_tb/larg)][0] = 0
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
    #     if ind[0][1] == 0:
    #         is_checked = True
    # if is_checked:
    #     return [indice, 0]
    # return [indice]
    return indice_column


def update_matrix_subdivision(filename,width, height, index_rb, matrix):
    points = read_file(filename)
    indices_obs = abscisse_obstacles(points, width, height)
    #print(indices_obs)
    #indice_min = min_indices_column(index_obs)
    # for i in range(len(matrix)):
    #     for j in range(indice_min + 1):
    #         if [i, j] in index_obs:
    #             matrix[i][index_rb[1] - j] = 1

    #         # if len(indice_min) == 1 and not [i, j] in index_obs:
    #         #     matrix[i][index_rb[1] - j] = 0
            
    #         # if len(indice_min) == 2 and not [i, j] in index_obs:
    #         #     matrix[i][index_rb[1] - j] = 0
    for ind_obs in indices_obs:
        row = index_rb[0] - ind_obs[0]
        column = index_rb[1] + ind_obs[1]
        # print("obs local" + str(ind_obs))
        # print("row " + str(row) + " "+"column " + str(column))
        if row < np.shape(matrix)[0] and column < np.shape(matrix)[1]:
            matrix[row][column] = 1


if __name__ == "__main__":

    long_rb = 1
    larg_rb = 1
    gap = 0.
    larg_table = 10
    point_arr = [6, 5]
    ind_rb_i = int(larg_table / ( 2 * (larg_rb + 2. * gap) ) )
    index_rb = [ind_rb_i,0]
    print(" inddex du robot "+ str(index_rb))
    #points = read_file("data-position.csv")
    filename = "data-position.csv"
    width, height, matrix = init_matrix_subdivision(
        long_rb, larg_rb, gap, larg_table, point_arr)
    print(np.shape(matrix))
    update_matrix_subdivision(filename, width, height, index_rb, matrix)
    #print(matrix)
    
    
    
