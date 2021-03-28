from typing import List


def get_user_input(ret_input, message, length):
    input_error = True
    while input_error:
        try:
            ret_input = list(map(int, input(message).strip().split()))[:length + 1]
        except ValueError:
            print("ERROR: Invalid Coefficient/s Detected")
            continue
        if len(ret_input) != length:
            print("ERROR: Invalid Count of Coefficients")
            input_error = True
        else:
            input_error = False
    return ret_input


def get_matrix(user_input):
    itr = iter(user_input)
    for y in range(0, 3):
        for x in range(0, 3):
            matrix[y][x] = next(itr)
    return matrix


def get_new_matrix(matrix):
    temp_matrix_a = [[0 for i in range(3)] for j in range(3)]
    temp_matrix_b = [[0 for i in range(3)] for j in range(3)]
    negation = 0
    for y in range(0, 3):
        for x in range(0, 3):
            temp_matrix_a[y][x] = get_partial_determinant(matrix, x, y)
    for y in range(0, 3):
        for x in range(0, 3):
            if negation % 2 == 1:
                temp_matrix_a[y][x] = -temp_matrix_a[y][x]
            temp_matrix_b[x][y] = temp_matrix_a[y][x]
            negation += 1
    return temp_matrix_b


def get_partial_determinant(matrix, x, y):
    small_matrix = [[0 for i in range(2)] for j in range(2)]
    row = 0
    for j in range(0, 3):
        if j != y:
            col = 0
            for i in range(0, 3):
                if i != x:
                    small_matrix[row][col] = matrix[j][i]
                    col += 1
            row += 1
    return (small_matrix[0][0] * small_matrix[1][1]) - (small_matrix[0][1] * small_matrix[1][0])


def get_determinant(matrix):
    for y in range(0, 3):
        matrix[y].append(matrix[y][0])
        matrix[y].append(matrix[y][1])
    determinant = 0
    itr = [[0, 1, 2], [2, 1, 0]]
    for arr in itr:
        sum = 0
        for k in arr:
            temp = 1
            for x, y in zip(arr, range(3)):
                temp *= matrix[y][x + k]
            sum += temp
        determinant += sum
    for y in range(0, 3):
        for k in range(2):
            matrix[y].pop(len(matrix[y]) - 1)
    return determinant


def get_solution(solution, determinant):
    for y in range(0, 3):
        new_matrix[y] = solution[y] / determinant
    return new_matrix


def multiply_matrix(new_matrix, user_input, solution):
    for y in range(3):
        sum = 0
        for k in range(3):
            sum += new_matrix[y][k] * user_input[k]
        solution[y] = sum
    return solution


def unique_solution(matrix, user_input, determinant):
    for y in range(0, 3):
        matrix[y].append(user_input[y])
    for y in range(2):
        for x in range(y + 1, 3):
            dependent = False
            for m, n in zip(matrix[y], matrix[x]):
                if m != n:
                    dependent = True
            if not dependent:
                return False
    if determinant == 0:
        return False
    return True


if __name__ == '__main__':
    user_input = list()
    solution = [1 for i in range(3)]
    matrix = [[1 for i in range(3)] for j in range(3)]

    user_input = get_user_input(user_input, "Please enter the 9 coefficient: ", 9)
    matrix = get_matrix(user_input)
    user_input = get_user_input(user_input, "Please enter the 3 values: ", 3)

    determinant = get_determinant(matrix)
    if not unique_solution(matrix, user_input, determinant):
        print("Has No Unique Solution")
    new_matrix = get_new_matrix(matrix)
    solution = multiply_matrix(new_matrix, user_input, solution)
    solution = get_solution(solution, determinant)
    print(solution)
