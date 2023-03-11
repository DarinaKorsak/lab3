if __name__ == '__main__':
    def transpose(matrix):
        n = len(matrix)
        m = len(matrix[0])

        nw_list = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                nw_list[i][j] = matrix[j][i]

        return nw_list


    matrix = []
    while True:
        variable = input()
        if variable == '0':
            break
        else:
            matrix.append(variable.split())

    print(transpose(matrix))