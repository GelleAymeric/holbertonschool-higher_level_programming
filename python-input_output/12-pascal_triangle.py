#!/usr/bin/python3
"""Module for generating Pascal's triangle."""



def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    matrix = []

    for x in range(n):
        row = [1] * (x + 1)

        for y in range(1, x):
            row[y] = matrix[x-1][y-1] + matrix[x-1][y]

        matrix.append(row)

    return matrix
