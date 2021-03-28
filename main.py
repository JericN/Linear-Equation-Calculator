def get_user_input(ret_input, message, length):
    input_error = True
    while input_error:
        input_error = False
        ret_input = input(message).strip().split()
        if ret_input[0] == "quit":
            exit()
        if len(ret_input) != length:
            print("ERROR: Invalid Count of Coefficients")
            input_error = True
        for k in range(length):
            try:
                ret_input[k] = float(ret_input[k])
            except ValueError:
                print("ERROR: Invalid Coefficient/s Detected")
                input_error = True
                break
            except IndexError:
                break
    if message == "Enter Number of Variables: ":
        return int(ret_input[0])
    else:
        return ret_input


def single_variable(matrix, values, size):
    if size == 1:
        print(values[0] / matrix[0][0])
        exit()


def check_unique_solution(determinant):
    if determinant == 0:
        print("No Unique Solution Found")
        exit()


def get_matrix(input_list, size):
    result_matrix = [[0 for y in range(size)] for x in range(size)]
    itr = iter(input_list)
    for y in range(size):
        for x in range(size):
            result_matrix[y][x] = next(itr)
    return result_matrix


def get_determinant(input_matrix, size):
    if size == 1:
        return input_matrix[0][0]
    else:
        determinant_list = list()
        val = 0
        sign = 1
        for k in range(size):
            determinant_list.clear()
            for y in range(1, size):
                for x in range(size):
                    if x != k:
                        determinant_list.append(input_matrix[y][x])
            determinant_matrix = get_matrix(determinant_list, size - 1)
            val += (sign * input_matrix[0][k] * get_determinant(determinant_matrix, size - 1))
            sign *= -1
        return val


def get_cofactor_matrix(input_matrix, size):
    determinant_list = list()
    cofactor_list = list()
    for y in range(0, size):
        for x in range(0, size):
            determinant_list.clear()
            for j in range(0, size):
                for i in range(0, size):
                    if i != x and j != y:
                        determinant_list.append(input_matrix[j][i])
            determinant_matrix = get_matrix(determinant_list, size - 1)
            val = get_determinant(determinant_matrix, size - 1)
            if x % 2 != y % 2:
                val *= -1
            cofactor_list.append(val)
    return get_matrix(cofactor_list, size)


def get_adjugate_matrix(input_matrix, size):
    adjugate = [[0 for y in range(size)] for x in range(size)]
    for y in range(size):
        for x in range(size):
            adjugate[y][x] = input_matrix[x][y]
    return adjugate


def get_solution(adjugate, value, determinant, size):
    solution = list()
    for y in range(size):
        total = 0
        for k in range(size):
            total += adjugate[y][k] * value[k]
        temp = total / determinant
        if temp.is_integer():
            temp = int(temp)
        solution.append(temp)
    return solution


if __name__ == '__main__':
    user_input = list()
    print("Enter 'quit' to close the program")
    matrix_size = int(get_user_input(user_input, "Enter Number of Variables: ", 1))
    user_input = get_user_input(user_input, "Enter the coefficients: ", matrix_size ** 2)
    base_matrix = get_matrix(user_input, matrix_size)
    user_input = get_user_input(user_input, "Enter the values: ", matrix_size)

    single_variable(base_matrix, user_input, matrix_size)
    matrix_determinant = get_determinant(base_matrix, matrix_size)
    check_unique_solution(matrix_determinant)
    cofactor_matrix = get_cofactor_matrix(base_matrix, matrix_size)
    adjugate_matrix = get_adjugate_matrix(cofactor_matrix, matrix_size)
    final_solution = get_solution(adjugate_matrix, user_input, matrix_determinant, matrix_size)
    print("Solutions: ", final_solution)
