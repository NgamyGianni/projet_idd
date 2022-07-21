import a_star, subarea, time

"""ser = serial.Serial('/dev/ttyACM0')

for i in range(len(commands)):
    time.sleep(0.2)
    ser.write(commands[i].encode())"""

if __name__ == "__main__":
    #call datalidar
    
    long_rb = 1
    larg_rb = 1
    gap = 0.
    larg_table = 10
    point_arr = [6, 5]
    ind_rb_i = int(larg_table / ( 2 * (larg_rb + 2. * gap) ) )
    index_rb = [ind_rb_i,0]
    #points = read_file("data-position.csv")
    filename = "data-position.csv"
    width, height, matrix = subarea.init_matrix_subdivision(
        long_rb, larg_rb, gap, larg_table, point_arr)
    subarea.update_matrix_subdivision(filename, width, height, index_rb, matrix)