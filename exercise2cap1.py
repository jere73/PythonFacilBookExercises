def sum_matrix(matrix):
    
    rows_sum = []
    columns_sum = []
    length = len(matrix)
    
    for i in range(len(matrix)):
        
        control_row_sum = 0
        
        for j in range(len(matrix[i])):
            control_row_sum += matrix[i][j]

        rows_sum.append(control_row_sum)
        
    print('{}'.format(rows_sum))

T = [[11, 12, 5, 2], [15, 6, 10, 12], [10, 8, 12, 5], [12, 15, 8, 6]]
sum_matrix(T)