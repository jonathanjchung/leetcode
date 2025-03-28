# attempt one, first medium problem took around 90 min
# right down left up
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    result = []
    while matrix:
        if not matrix:  # check
            return result
        top_row = matrix.pop(0)  # right
        for val in top_row:
            result.append(val)
        for row in matrix:  # down
            if not row:  # check
                return result
            result.append(row.pop())
        if not matrix:  # check
            return result
        bot_row = matrix.pop()  # left
        for val in bot_row[::-1]:
            result.append(val)
        for row in matrix[::-1]:  # up
            if not row:  # check
                return result
            result.append(row.pop(0))
    return result


# O(n) solution
def attempt_two(matrix: list[list[int]]) -> list[int]:
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result
