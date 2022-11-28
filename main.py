# Student placement
# This program takes in n students and n schools, each with their
# ranked preferences for each other
import numpy as np

global cross_out_count
cross_out_count = 0

global max_cross_out
max_cross_out = 0

# reduce matrix
# subtract the minimum value from each row
# run time of O(n)
def reduce_rows(matrix):
    for i in range(0, array_size):
        row = matrix[i]
        minimum = min(row)
        row = [x - minimum for x in row]
        matrix[i] = row

# run time of O(n)
def reduce_columns(matrix):
    # remove the minimum from each column if it doesn't contain a 0
    for i in range(0, array_size):
        column = matrix[:, i]
        # if there are no zeroes in the column
        if np.any(matrix[:, i] != 0):
            minimum = min(column)
            column = [x - minimum for x in column]
            matrix[:, i] = column

# run time of O(n^2)
def cross_out_zeroes(matrix):
    for i in range(0, array_size):
        zero_count_row = 0
        row = matrix[i]
        for j in row:
            if j == 0:
                zero_count_row += 1

    for i in range(0, array_size):
        zero_count_col = 0
        col = matrix[:, i]
        for j in col:
            print(j)

    # take the absolute value of the max. If horizontal, negate it and replace it in the array

# run time of O(n)
# function that gets count of zeros in a row based on index
def zero_counting(matrix, row_index, column_index):
    global max_cross_out
    zero_count_row = 0
    zero_count_col = 0

    row = matrix[row_index]
    for j in row:
        if j == 0:
            zero_count_row += 1
    zero_count_row = -zero_count_row

    col = matrix[:, column_index]
    for j in col:
        if j == 0:
            zero_count_col += 1

    if abs(zero_count_row) > zero_count_col:
        zero_matrix_value = zero_count_row
        if max_cross_out < abs(zero_count_row):
            max_cross_out = abs(zero_count_row)
    else:
        zero_matrix_value = zero_count_col
        if max_cross_out < zero_count_col:
            max_cross_out = zero_count_col

    cross_matrix[row_index, column_index] = zero_matrix_value
    # zero_cross_out(cross_matrix, row_index, column_index)


def zero_cross_out(cross_out_matrix, row_index, col_index):
    global cross_out_count
    if(cross_out_matrix[row_index, col_index] < 0):
        # if its negative that means its a row
        replacement_row = [1]*array_size
        cross_out_matrix[row_index] = replacement_row
        cross_out_count += 1
    else:
        # if it's a column to be crossed out
        replacement_col = [1]*array_size
        cross_out_matrix[:, col_index] = replacement_col
        cross_out_count += 1

    return cross_out_count

# run time of O(n^3)
def strike_through(cross_out_matrix, max_cross_out):
    global cross_out_count
    for q in range(max_cross_out, 0, -1):
        for i in range(0,array_size):
            row = cross_out_matrix[i]
            for j in row:
                if j < 0 and j == -q and crossed_out_matrix[i,j] != 1:
                    crossed_out_matrix[i] = '1'
                    cross_out_count += 1
                if j > 0 and j == q and crossed_out_matrix[i,j] != 1:
                    crossed_out_matrix[::, i] = '1'
                    cross_out_count += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array_size = 10

    cross_matrix = [[0]*array_size]*array_size
    cross_matrix = np.array(cross_matrix)

    crossed_out_matrix = [[0]*array_size]*array_size
    crossed_out_matrix = np.array(crossed_out_matrix)

    arr = [[5,4,15,15,4,15,10,7,3,18],
           [13,15,12,7,14,11,15,2,7,3],
           [11,9,13,5,11,9,17,15,9,7],
           [10,13,6,10,8,4,4,15,14,14],
           [13,3,2,8,13,8,4,9,8,14],
           [6,18,16,9,11,7,11,10,13,7],
           [13,3,4,10,8,12,11,7,14,5],
           [7,13,7,16,7,10,11,14,7,17],
           [9,15,7,11,12,13,3,11,14,7],
           [13,7,16,9,12,11,14,10,11,8]]
    a = np.array(arr)
    print(a)
    reduce_rows(a)
    reduce_columns(a)
    for j in range(0, array_size):
        for i in range(0, array_size):
            if a[i, j] == 0:
                zero_counting(a, i,j)

    strike_through(cross_matrix, max_cross_out)
    print(crossed_out_matrix)

    # from this crossed out matrix, we find the solution pairings

