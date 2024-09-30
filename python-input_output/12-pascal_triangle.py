#!/usr/bin/python3


def pascal_triangle(n):
    """ Representing the pascal's triangle of n. """
    if n <= 0:
        return []

    matrix = []

    for x in range(n):
        row = [1] * (x + 1)

        for y in range(1, x):
            row[y] = matrix[x-1][y-1] + matrix[x-1][y]

        matrix.append(row)

    return matrix
