def annotate(garden):
    validate_garden(garden)

    new_garden = []

    for (y, row) in enumerate(garden):
        new_row = annotate_row(garden, row, y)
        new_garden.append("".join(new_row))

    return new_garden


def annotate_row(garden: list[str], row: str, y: int) -> list:
    new_row = []
    for (x, _) in enumerate(row):
        new_row.append(annotate_flower(garden, y, x))

    return new_row


def annotate_flower(garden: list[str], y: int, x: int) -> str:
    flower = garden[y][x]
    if flower not in ["*", " "]:
        raise ValueError("The board is invalid with current input.")

    if (flower == "*"):
        return flower
    else:
        count = count_adjacent_flowers(garden, y, x)
        if (count > 0):
            return f"{count}"
        else:
            return flower
            


def count_adjacent_flowers(garden: list[str], row: int, column: int) -> int:
    adjacent_flowers = 0

    adjacent_flowers += count_flower_at_location(garden, row - 1, column)
    adjacent_flowers += count_flower_at_location(garden, row - 1, column - 1)
    adjacent_flowers += count_flower_at_location(garden, row - 1, column + 1)
    adjacent_flowers += count_flower_at_location(garden, row, column - 1)
    adjacent_flowers += count_flower_at_location(garden, row, column + 1)
    adjacent_flowers += count_flower_at_location(garden, row + 1, column - 1)
    adjacent_flowers += count_flower_at_location(garden, row + 1, column)
    adjacent_flowers += count_flower_at_location(garden, row + 1, column + 1)

    return adjacent_flowers
        
def count_flower_at_location(garden: list[str], row: int, column: int) -> int:
    return 1 if is_flower_at_location(garden, row, column) else 0

def is_flower_at_location(garden: list[str], row: int, column: int) -> bool:
    if (row < 0 or column < 0):
        return False

    try:
        return garden[row][column] == "*"
    except IndexError:
        return False

def validate_garden(garden: list[str]) -> None:
    row_lengths = list(map(lambda row: len(row), garden))
    unique_row_lengths = set(row_lengths)
    if (len(garden) > 0 and len(unique_row_lengths) != 1):
        raise ValueError("The board is invalid with current input.")
