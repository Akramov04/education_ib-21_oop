from chess import Board

class Figure:
    def __init__(self, color: int):
        self.__color = color


    @property
    def char(self) -> str:
        return '  '

    @property
    def color(self) -> int:
        return self.__color

    def can_move(self,
                 board: Board,
                 row_start: int,
                 col_start: int,
                 row_end: int,
                 col_end: int
                 ) -> bool:
        return False

    def can_attack(self,
                 board: Board,
                 row_start: int,
                 col_start: int,
                 row_end: int,
                 col_end: int
                 ) -> bool:
        return self.can_move(
            board,
            row_start,
            col_start,
            row_end,
            col_end
        )