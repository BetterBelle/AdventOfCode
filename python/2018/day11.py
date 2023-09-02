# Q1
input = 7315
cells = [[0 for x in range(300)] for y in range(300)]

# Creating the cells
for i in range(300):
    for j in range(300):
        rack_id = (i+1) + 10
        power_level = (int( (((( rack_id * (j+1) ) + input ) * rack_id ) / 100) ) % 10 ) - 5
        cells[i][j] = power_level

# Going through to find the largest power 3x3 cell
cell = (1,1)
max = 0
for i in range(297):
    for j in range(297):
        power = cells[i][j] + cells[i+1][j] + cells[i+2][j] + cells[i][j+1] + cells[i+1][j+1] + cells[i+2][j+1] + cells[i][j+2] + cells[i+1][j+2] + cells[i+2][j+2]
        if (power > max):
            max = power
            cell = (i+1,j+1)

print (cell)

# Q2
cell = (1,1,1)
max = 0
for i in range(300):
    for j in range(300):
        power = 0
        for size in range(1,300):
            if (i + size < 300 and j + size < 300):
                for outside in range(size):
                    power += cells[i+size][j+outside]
                    power += cells[i+outside][j+size]
                
                power += cells[i+size][j+size]
                if (power > max):
                    cell = (i+1,j+1,size+1)
                    max = power

print (cell)

