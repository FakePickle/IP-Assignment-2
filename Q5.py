def coordinates():
    coordinates = []
    while True:
        user_input = list(map(int,input('Enter x and y coordinates : ').split()))
        if not(len(user_input)==2):
            break
        else:
            inputs = tuple(user_input)
            coordinates.append(inputs)
    return coordinates

def create_matrix(coordinates):
    shape_matrix = []
    for i in coordinates:
        l = []
        for j in i:
            l.append(j)
        l.append(1)
        shape_matrix.append(l)
    return shape_matrix

def scale_matrix(matrix,cx,cy):
    scaling_matrix = [[cx,0,0],[0,cy,0],[0,0,1]]
    scaled_matrix = [[0 for x in range(len(scaling_matrix[0]))] for y in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(scaling_matrix[0])):
            for k in range(len(scaling_matrix)):
                scaled_matrix[i][j] += matrix[i][k] * scaling_matrix[k][j]
    return scaled_matrix

def new_shape(scaled_matrix):
    print()
    print('x   y')
    for i in scaled_matrix:
        print(str(i[0]),' ',str(i[1]))

if __name__ == '__main__':
    cx = int(input("Enter scaling parameter : "))
    cy = int(input("Enter scaling parameter : "))
    coordinates = coordinates()
    matrix = create_matrix(coordinates)
    scaled_matrix = scale_matrix(matrix,cx,cy)
    new_shape(scaled_matrix)