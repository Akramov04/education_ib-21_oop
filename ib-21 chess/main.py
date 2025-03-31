import re
from chess import Board
from chess.Color import WHITE

def convert(point: str) -> tuple[int, int]:
    char, num = list(point)
    return int(num) - 1, ord(char) - 65

def print_board(_board: Board) -> None:
    for y in range(8, 0, -1):
        print('  +' + '----+' * 8)
        print(f'{y} |', end='')
        for x in range(8):
            item = _board.get_item(y - 1, x)
            print(' ', end='')
            if not item:
                print('  ', end='')
            else:
                print(item.char, end='')
            print(' |', end='')
        print()
    print('  +' + '----+' * 8)
    print('  ', end='')
    for x in range(8):
        c = chr(ord('A') + x)
        print(f'   {c} ', end='')
    print()
    print('Команды:')
    print('    exit                - выход')
    print('    move <from> <to>    - ход из клетки <from> в клетку <to>')
    print()
    if _board.player == WHITE:
        print('Ход белых')
    else:
        print('Ход черных')


board = Board()
while True:
    print_board(board)
    try:
        cmd = input('Команда: ').strip()
        if cmd.lower() == 'exit':
            break
        if not cmd.lower().startswith('move'):
            raise Exception(f'Неизвестная команда: {cmd}')
        cmd = cmd.replace('move', '').strip().upper()
        parts = cmd.split()
        if len(parts) != 2:
            raise Exception('Неверный формат ввода!')
        regexp = r'^[A-F]{1}[1-8]{1}$'
        for part in parts:
            if not re.match(regexp, part):
                raise Exception(f'Неверная координата: {part}')
        start, end = list(
            map(
                lambda p: convert(re.match(regexp, p).group(0)),
                parts
            )
        )
        if start == end:
            raise Exception('Мы топчимся на месте')
        player = board.get_item(*start)
        if not player:
            raise Exception('Вы не можете двигать несуществующую фигуру')
        if player.color != board.player:
            raise Exception('Вы не можете двигать чужую фигуру')
        other_player = board.get_item(*end)
        if other_player:
            if other_player.color == player.color:
                raise Exception('Вы не можете аттаковать свои фигуры')
            if not player.can_attack(
                board,
                *start,
                *end
            ):
                raise Exception('Вы не можете аттаковать эту фигуру')
        elif not player.can_move(board, *start, *end):
            raise Exception(f'Фигура {player.char} не можем так двигаться!')
        board.change_player()
        board.move_item(*start, *end)
    except Exception as e:
        print('Ошибка:', e)
        input('Нажмите любую клавишу для продолжения...')
