from .Color import WHITE
from .Figure import Figure
from . import Board


class Bishop(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wB'
        return 'bB'

    def can_move(
            self,
            board: Board,
            row_start: int,
            col_start: int,
            row_end: int,
            col_end: int) -> bool:
        col_diff = abs(col_end - col_start)
        row_diff = abs(row_end - row_start)
        if col_diff != row_diff:
            return False
        row = row_start
        col = col_start
        row_step = 1 if row_start < row_end else -1
        col_step = 1 if col_start < col_end else -1
        for i in range(col_diff - 1):
            other_player = board.get_item(row, col)
            if other_player:
                return False
            row += row_step
            col += col_step
        return True


