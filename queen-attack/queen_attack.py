from __future__ import annotations

class Queen:
    def __init__(self, row: int, column: int):
        check(row < 0, "row not positive")
        check(row > 7, "row not on board")
        check(column < 0, "column not positive")
        check(column > 7, "column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen: Queen) -> bool:
        is_same_column = self.column == another_queen.column
        is_same_row = self.row == another_queen.row

        if (is_same_row & is_same_column):
            raise ValueError("Invalid queen position: both queens in the same square")

        if (is_same_row | is_same_column):
            return True

        column_delta = abs(self.column - another_queen.column)
        row_delta = abs(self.row - another_queen.row)

        return (column_delta == row_delta)

@staticmethod
def check(condition: bool, messsage: str) -> [ValueError | None]:
    if condition:
        raise ValueError(messsage)
