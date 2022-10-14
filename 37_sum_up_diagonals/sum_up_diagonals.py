def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        [1,   2],
        [30, 40],
        ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
         ]
        >>> sum_up_diagonals(m2)
        30
    """
    # length = len(matrix)
    TL_to_BR_sum = 0

    for row in matrix:
        for item in row:
            if matrix.index(row) == row.index(item):
                TL_to_BR_sum += item

    BL_to_TR_sum = 0

    # Reverse matrix rows
    matrix.reverse()

    for row in matrix:
        for item in row:
            if matrix.index(row) == row.index(item):
                BL_to_TR_sum += item

    return TL_to_BR_sum + BL_to_TR_sum


m1 = [
    [1, 2],
    [30, 40],
]

m2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
         ]