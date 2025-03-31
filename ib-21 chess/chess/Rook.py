from .Color import WHITE
from .Figure import Figure
from chess import Board

class Rook(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wR'
        return 'bR'

    def can_move(self,
                 board: Board,
                 row_start: int,
                 col_start: int,
                 row_end: int,
                 col_end: int
                 ) -> bool:
        row_diff = abs(row_end - row_start)
        col_diff = abs(col_end - col_start)
        if row_diff and col_diff:
            return False
        if row_diff:
            col_step = 0
            row_step = 1 if row_end > row_start else -1
        else:
            row_step = 0
            col_step = 1 if col_end > col_start else -1
        for row in range(row_start + row_step, row_end, row_diff):
            for col in range(col_start + col_step, col_end, col_diff):
                figure = board.get_item(row, col)
                if figure:
                    return False
        return True
