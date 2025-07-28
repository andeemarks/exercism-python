from itertools import cycle

UNPOPULATED = -1

def spiral_matrix(size: int):
    if (size == 0):
        return []
    
    RIGHT_TURN_OFFSETS = cycle(iter([(0, 1), (1, 0), (0, -1), (-1, 0)]))

    result = [ [UNPOPULATED] * size for i in range(size)]
    row = 0
    col = 0
    result[row][col] = 1
    row_col_offsets = next(RIGHT_TURN_OFFSETS)
    next_num = 2

    while (next_num <= size ** 2):
        possible_row = row + row_col_offsets[0]
        possible_col = col + row_col_offsets[1]
        if (possible_row in range(size) and possible_col in range(size) and result[possible_row][possible_col] == UNPOPULATED):
            result[possible_row][possible_col] = next_num
            next_num += 1
            row = possible_row
            col = possible_col
        else:
            row_col_offsets = next(RIGHT_TURN_OFFSETS)

    return result
