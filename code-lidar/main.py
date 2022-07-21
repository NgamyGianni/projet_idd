import a_star, subarea, time, datalidar

def tradMove(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    dx = x2 - x1
    dy = y2 - y1
    
    if dx != 0:
        if dx == 1:
            return "d"
        else:
            return "q"
    else:
        if dy == 1:
            return "z"
        else:
            return "s"

moves = [(5, 5), (6, 5), (7, 5), (8, 5)]

commands = [tradMove(moves[i], moves[i+1]) for i in range(len(moves)-1)]

print(commands)

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
    filename1 = "data-lidar.csv"
    filename2 = "data-position.csv"

    # Get from Lidar
    datalidar.run([filename1, filename2])

    # Initiaalize the area subdivision
    width, height, matrix = subarea.init_matrix_subdivision(
        long_rb, larg_rb, gap, larg_table, point_arr)

    
    subarea.update_matrix_subdivision(filename2, width, height, index_rb, matrix)
