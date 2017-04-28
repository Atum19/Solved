import numpy as np


def main():
    n = 10

    # create matrix
    matrix = np.zeros((n, n), dtype=np.int)
    matrix[0][0] = 0
    # we have only 1 possible path straight to the right
    # through the first raw
    matrix[0][1] = 1
    # and only 1 possible path straight down
    # through the first column
    matrix[1][0] = 1

    for i, elem in enumerate(matrix):
        for j, el in enumerate(elem):
            # total paths, which we can get to a square
            # is the sum of previous total paths for a square on top
            # and previous total paths for a square on the left
            matrix[i][j] = matrix[i][j] + matrix[i - 1][j]
            matrix[i][j] = matrix[i][j] + matrix[i][j-1]

    print(matrix[n-1][n-1])  # number of paths


if __name__ == '__main__':
    main()
