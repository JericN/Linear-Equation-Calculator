# This method handles all input data to the program
def get_user_input(input_list, message, length):
    input_error = True
    # repeat until a valid input is recorded or unless the user ends the program
    while input_error:
        input_error = False
        # Ask user for the input, and convert the string to an array using whitespaces to split
        input_list = input(message).strip().split()

        # Check if the list is empty
        if not input_list:
            input_error = True
            continue

        # ends the program if user enters "quit"
        if input_list[0] == "quit":
            print("\nThe Program is Ended\nCMSC 116 Quiz 1\n[Jeric Narte]")
            exit()

        # if the input is not on the valid/expected length, repeat the loop
        if len(input_list) != length:
            print("=> ERROR: Invalid Count of Coefficients")
            input_error = True

        # if the input has invalid character/s, repeat the loop
        for k in range(length):
            try:
                input_list[k] = float(input_list[k])
            except ValueError:
                print("=> ERROR: Invalid Coefficient/s Detected")
                input_error = True
                break
            except IndexError:
                break
        if input_error:
            continue

        # if the number of variable is not a positive integer, repeat the loop
        if message == "Enter Number of Variables: ":
            try:
                if int(input_list[0]) < 1:
                    print("=> ERROR: Invalid Number")
                    input_error = True
            except ValueError:
                print("=> ERROR: Invalid Number")
                input_error = True

    # return corresponding values
    if message == "Enter Number of Variables: ":
        return int(input_list[0])
    else:
        return input_list


# solution if there is only 1 variable
def single_variable(matrix, values, size):
    if matrix[0][0] == 0:
        print("=> No Unique Solution Found\n")
    else:
        print("=> Solution: ", values[0] / matrix[0][0], "\n")


# check if the system has a unique solution
# that is if the determinant is not 0
def check_unique_solution(determinant):
    if determinant == 0:
        print("=> No Unique Solution Found\n")
        return False
    else:
        return True


# transform a list into 2 dimension array (matrix)
def get_matrix(input_list, size):
    result_matrix = [[0 for y in range(size)] for x in range(size)]
    # Iterate between each value in the list and
    # save each value to its corresponding cell in the 2d array
    itr = iter(input_list)
    for y in range(size):
        for x in range(size):
            result_matrix[y][x] = next(itr)
    return result_matrix


# this will solve for the determinant of a matrix in any positive integer 'size'
# this method uses recursion since you will need to solve the determinants of
# the secondary matrices in order to solve for the determinant of the target matrix
def get_determinant(matrix, size):
    if size == 1:
        # the recursion will end at size = 1
        # since each subsequent matrix has a size smaller by 1
        return matrix[0][0]
    else:
        # this uses the general method in solving a determinant
        # which is called the expansion of th
        # e first row
        determinant_list = list()
        val = 0
        sign = 1
        for k in range(size):
            determinant_list.clear()
            for y in range(1, size):
                for x in range(size):
                    if x != k:
                        determinant_list.append(matrix[y][x])
            determinant_matrix = get_matrix(determinant_list, size - 1)
            val += (sign * matrix[0][k] * get_determinant(determinant_matrix, size - 1))
            sign *= -1
        return val


# this will solve for the cofactor matrix
def get_cofactor_matrix(matrix, size):
    determinant_list = list()
    cofactor_list = list()
    # this will loop to and get all secondary matrices
    # the cofactor matrix will contain the determinant of all secondary matrices
    for y in range(0, size):
        for x in range(0, size):
            determinant_list.clear()
            for j in range(0, size):
                for i in range(0, size):
                    if i != x and j != y:
                        determinant_list.append(matrix[j][i])
            determinant_matrix = get_matrix(determinant_list, size - 1)
            val = get_determinant(determinant_matrix, size - 1)
            # multiply the matrix with an alternating signs (checkered pattern)
            if x % 2 != y % 2:
                val *= -1
            cofactor_list.append(val)
    return get_matrix(cofactor_list, size)


# this will solve for the adjugate matrix
# the adjugate matrix is the transposed cofactor matrix
def get_adjugate_matrix(matrix, size):
    adjugate = [[0 for y in range(size)] for x in range(size)]
    for y in range(size):
        for x in range(size):
            adjugate[y][x] = matrix[x][y]
    return adjugate


# solve the solutions of the system
# using the Adjoint matrix method
def get_solutions(adjugate, rhs, determinant, size):
    solution = list()
    for y in range(size):
        total = 0
        # get the product of the two matrix
        for k in range(size):
            total += adjugate[y][k] * rhs[k]
        # divide each element of the product by the determinant
        temp = total / determinant
        if temp.is_integer():
            temp = int(temp)
        solution.append(temp)
    return solution


if __name__ == '__main__':
    user_input = list()
    print("\nSystem of Linear Equation Calculator")
    print("[Enter 'quit' to close the program]\n")
    while True:
        # the program will repeat until the user ends the program
        # get the number of variables
        matrix_size = int(get_user_input(user_input, "Enter Number of Variables: ", 1))
        # get the coefficients for each equations
        user_input = get_user_input(user_input, "Enter the {} Coefficient(s): ".format(matrix_size ** 2), matrix_size ** 2)
        # Convert the list to a double array (Matrix)
        coefficient_matrix = get_matrix(user_input, matrix_size)
        # get the values for each equation
        user_input = get_user_input(user_input, "Enter the {} RHS Value(s): ".format(matrix_size), matrix_size)
        rhs_matrix = user_input

        if matrix_size == 1:
            # if there is only 1 variable
            single_variable(coefficient_matrix, rhs_matrix, matrix_size)
        else:
            # warns the user for expected processing time
            if matrix_size > 29:
                print("=> Please stop :(")
            elif matrix_size > 14:
                print("=> This may take days to calculate, please wait")
            elif matrix_size > 9:
                print("=> This may take hours to calculate, please wait")
            # get the determinant
            matrix_determinant = get_determinant(coefficient_matrix, matrix_size)
            # check if the system of linear equation has a unique solution
            if check_unique_solution(matrix_determinant):
                # solve for the cofactor matrix
                cofactor_matrix = get_cofactor_matrix(coefficient_matrix, matrix_size)
                # solve for the adjugate matrix
                adjugate_matrix = get_adjugate_matrix(cofactor_matrix, matrix_size)
                # get the solutions for the system
                final_solution = get_solutions(adjugate_matrix, rhs_matrix, matrix_determinant, matrix_size)
                print("=> Solutions: ", final_solution, "\n")
