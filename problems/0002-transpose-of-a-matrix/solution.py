def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.

    Args:
        a: A 2D matrix of shape (m, n)

    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    result = []
    length = len(a[0])
    for i in range(length):
        t = []
        for j in range(len(a)):
            t.append(a[j][i])
        result.append(t)
    return result