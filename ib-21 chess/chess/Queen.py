from .Color import WHITE
from .Figure import Figure
from . import Board


class Queen(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wQ'
        return 'bQ'

    def can_move(
            self,
            board: Board,
            row_start: int,
            col_start: int,
            row_end: int,
            col_end: int) -> bool:
        # Проверка, может ли ферзь двигаться как слон
        col_diff = abs(col_end - col_start)
        row_diff = abs(row_end - row_start)

        if col_diff == row_diff:
            # Движение по диагонали
            row = row_start
            col = col_start
            row_step = 1 if row_start < row_end else -1
            col_step = 1 if col_start < col_end else -1
            for i in range(col_diff - 1):
                other_player = board.get_item(row + row_step, col + col_step)
                if other_player:
                    return False
                row += row_step
                col += col_step
            return True

        # Проверка, может ли ферзь двигаться как ладья
        if row_start == row_end or col_start == col_end:
            # Движение по горизонтали или вертикали
            step = 1 if row_start < row_end else -1
            if row_start == row_end:
                for i in range(min(col_start, col_end) + 1, max(col_start, col_end)):
                    if board.get_item(row_start, i):
                        return False
            else:
                for i in range(min(row_start, row_end) + 1, max(row_start, row_end)):
                    if board.get_item(i, col_start):
                        return False
            return True

        return False