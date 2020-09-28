import numpy as np

def main():
    """image_width = 2
    image_height = 2
    pattern_width = 1
    pattern_height = 1
    image = ['01', '12']
    pattern = ['2']"""

    image_width = 3
    image_height = 3
    pattern_width = 2
    pattern_height = 2
    #image = ['012', '345', '678']
    #pattern = ['34', '67']
    image = ['000', '111', '222']
    pattern = ['11', '22']

    """
    image_width = 4
    image_height = 4
    pattern_width = 3
    pattern_height = 3
    image = ['0123', '4567', '8901']
    pattern = ['123', '567', '901']"""
    print(solve(image_width, image_height, image, pattern_width, pattern_height, pattern))

def solve(image_width, image_height, image, pattern_width, pattern_height, pattern):
    image_matrix = to_matrix(image, image_width)
    pattern_matrix = to_matrix(pattern, pattern_width)

    return get_point(image_matrix, image_width, pattern_matrix, pattern_width)

def to_matrix(list_data, n):
    list1=[]
    new_matrix = []
    for i in range(0, len(list_data)):
        list1[:0]=list_data[i]
        new_matrix.append(list1[0:n])
    
    #print(np.array(new_matrix))
    return np.array(new_matrix)

#Get match
def get_point(image_matrix, image_width, pattern_matrix, pattern_width):
    #start = image_width - pattern_width
    end = image_width - pattern_width + 1
    print(end)
    for row in range(0, end, 1):
        for column in range(0, end, 1):
            actual_matrix = image_matrix[row:row+pattern_width, column:column+pattern_width]
            if same_Matrix(actual_matrix, pattern_matrix, pattern_width):
                return [column, row]
    
    return [-1, -1]


#Compare two matrix
def same_Matrix(A,B,n):
    for i in range(n):
        for j in range(n):
            if (A[i][j] != B[i][j]):
                return False

    return True




if __name__ == "__main__":
    main()











