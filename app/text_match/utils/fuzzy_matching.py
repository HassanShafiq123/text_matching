def levenshtein_distance(s1: str, s2: str) -> int:
    # Convert strings to lists of characters
    s1 = list(s1)
    s2 = list(s2)

    # Create a 2D matrix of zeroes with dimensions (len(s1) + 1) x (len(s2) + 1)
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Fill in the first row and first column
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j

    # Iterate through the matrix and fill in the rest of the cells
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1

    # Return the last element of the matrix
    return matrix[len(s1)][len(s2)]