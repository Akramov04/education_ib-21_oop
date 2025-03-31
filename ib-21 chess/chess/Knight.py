from .Color import WHITE
from .Figure import Figure
from chess import Board

class Knight(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wN'
        return 'bN'

    def can_move(
            self,
            board: Board,
            row_start: int,
            col_start: int,
            row_end: int,
            col_end: int) -> bool:
        col_diff = abs(col_end - col_start)
        row_diff = abs(row_end - row_start)
        return col_diff == 2 and row_diff == 1 or col_diff == 1 and row_diff == 2



