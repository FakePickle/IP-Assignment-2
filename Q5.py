#user input of coordinates of x and y
def coordinates():
    coordinates = []
    while True:
        user_input = list(map(int,input('Enter x and y coordinates : ').split()))
        if not(len(user_input)==2):
            break
        else:
            #making the coordinates in the form of a tuple
            inputs = tuple(user_input)
            #appneding those coordinates in a list
            coordinates.append(inputs)
    return coordinates

#creating a Nx3 matrix using those coordinates
def create_matrix(coordinates):
    #shaping matrix
    shape_matrix = []
    for i in coordinates:
        temp_list = []
        for j in i:
            temp_list.append(j)
        #according to question the third column is supposed to be 1 so we are appending 1
        temp_list.append(1)
        shape_matrix.append(temp_list)
    return shape_matrix

#scaling matrix or multiplying matrix A and matrix B
def scale_matrix(matrix,cx,cy):
    #matrix that will be multiplied by matrix A
    scaling_matrix = [[cx,0,0],[0,cy,0],[0,0,1]]
    #0 matrix
    scaled_matrix = [[0 for x in range(len(scaling_matrix[0]))] for y in range(len(matrix))]
    #multiplication of matrix
    for i in range(len(matrix)):
        for j in range(len(scaling_matrix[0])):
            for k in range(len(scaling_matrix)):
                scaled_matrix[i][j] += matrix[i][k] * scaling_matrix[k][j]
    return scaled_matrix

#printing x and y coordinates
def new_shape(scaled_matrix):
    print()
    print('x    y')
    for i in scaled_matrix:
        print(str(i[0]),'  ',str(i[1]))

#drivers code
if __name__ == '__main__':
    cx = int(input("Enter scaling parameter : "))
    cy = int(input("Enter scaling parameter : "))
    coordinates = coordinates()
    matrix = create_matrix(coordinates)
    scaled_matrix = scale_matrix(matrix,cx,cy)
    new_shape(scaled_matrix)