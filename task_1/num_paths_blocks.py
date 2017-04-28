import numpy as np


def count_paths(n, obstacles_list):
    """
    function takes matrix dimension - n,
    list of blocked squares - obstacles_list
    and return the sum of possible paths
    to the bottom right corner square
    """

    # let we have the matrix with the n×n dimensions
    matrix = np.zeros((n, n), dtype=np.int)
    # let we have the firs square never blocked
    matrix[0][0] = 0
    # we have only 1 possible path straight to the right
    # through the first raw
    matrix[0][1] = 1
    # and only 1 possible path straight down
    # through the first column
    matrix[1][0] = 1

    # check and set obstacles
    if len(obstacles_list) > 0:
        for item in obstacles_list:
            matrix[item[0]][item[1]] = -1

    # counting process
    for i, elem in enumerate(matrix):
        for j, el in enumerate(elem):
            if matrix[i][j] == -1:
                if i == 0:
                    # we can't move through
                    # the first raw after blocked square
                    for k in range(j, len(matrix[i]) - 1):
                        matrix[i][k] = 0

                if j == 0:
                    # also we can't move through
                    # the first column after blocked square
                    for k in range(i, len(matrix) - 1):
                        matrix[k][0] = 0

                # because the square is blocked
                # the number of paths through it equals to 0
                matrix[i][j] = 0
                continue

            # total paths, which we can get to a square
            # is the sum of previous total paths for a square on top
            # and previous total paths for a square on the left
            if i > 0:
                matrix[i][j] = matrix[i][j] + matrix[i - 1][j]
            if j > 0:
                matrix[i][j] = matrix[i][j] + matrix[i][j - 1]

    return matrix[n - 1][n - 1]  # number of paths


def main():
    obs_lst = []

    # simple interface
    print('please enter the matrix dimension (n)')
    n = int(input())
    while True:
        count = 0
        print('do you want to enter blocked squares? (y/n)')
        st = input()
        if st == 'n':
            break
        elif st not in ('y', 'n'):
            print('please enter the correct answer')
            continue
        else:
            print('please enter coordinates')
            print('please enter x (<={0}):'.format(n-1))
            x = int(input())
            print('please enter y (<={0}):'.format(n-1))
            y = int(input())
            count += 1
            print('you entered \"{0}\" and \"{1}\"'.format(x, y))
            print('and have {0} blocked square(s)'.format(count))
            obs_lst.append((x, y))
            continue

    print(count_paths(n, obs_lst))


if __name__ == '__main__':
    main()
