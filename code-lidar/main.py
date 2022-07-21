import a_star, subarea, time, datalidar

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
    point_arr = (6, 5)
    ind_rb_i = int(larg_table / ( 2 * (larg_rb + 2. * gap) ) )
    index_rb = (ind_rb_i,0)

    points = subarea.read_file("data-position.csv")
    filename1 = "data-lidar.csv"
    filename2 = "data-position.csv"

    # Get from Lidar
    datalidar.run([filename1, filename2])

    # Initiaalize the area subdivision
    width, height, matrix = subarea.init_matrix_subdivision(
        long_rb, larg_rb, gap, larg_table, point_arr)
    
    current = index_rb

    while current != point_arr :
        
        datalidar.run([filename1, filename2])
        
        subarea.update_matrix_subdivision(filename2, width, height, index_rb, matrix)
        
        path = a_star.astar(matrix, index_rb, point_arr)
        
        commands = a_star.commands(path)
            
        a_star.affiche_matrix(matrix, path)
        
        ser = serial.Serial('/dev/ttyACM0')

        if commands[0] == "z" or commands[0] == 's':
            for i in range(2):
                time.sleep(0.2)
                ser.write(commands[0].encode())
        else:
            for i in range(3):
                time.sleep(0.2)
                ser.write(commands[0].encode())
        
        current = path[1]
        
        
        
        
# 3 coups lat
# 2 coups avancer/reculer
