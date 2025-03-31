from .Color import WHITE
from .Figure import Figure
from chess import Board

class Pawn(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wP'
        return 'bP'

    def can_move(
            self,
            board: Board,
            row_start: int,
            col_start: int,
            row_end: int,
            col_end: int) -> bool:
        if col_start != col_end:
            return False
        is_white = self.color == WHITE
        if is_white and row_end < row_start or not is_white and row_end > row_start:
            return False
        step = 1 if is_white else -1
        max_count = 1
        if is_white and row_start == 1 or not is_white and row_start == 6:
            max_count = 2
        diff = abs(row_end - row_start)
        if diff > max_count:
            return False
        for ix in range(row_start + step, row_end, step):
            figure = board.get_item(
                ix, col_start
            )
            if figure:
                return False
        return True

    # def can_attack(
    #         self,
    #         board: Board,
    #         row_start: int,
    #         col_start: int,
    #         row_end: int,
    #         col_end: int) -> bool:
    #     return False

