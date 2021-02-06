import itertools
game = [[1, 0, 1],
        [0, 1, 0],
        [1, 1, 0]]

def init_game(game_map, player=0, row =0, column=0, just_display= False):
    try:
        if game_map[row][column] != 0:
            print('this place is occupied , Try again.....')
            return game_map, False
        print('   0, 1, 2')
        if not just_display:
            game_map[row][column] = player
        for count, raw in enumerate(game_map):
            print(count,raw)
        return game_map, True
    except IndexError as e:
        print(str(e))
        return game_map, False
    except Exception as er:
        print(str(er))
        return game_map, False



def choose_winner(current_game):

    def all_win(index_nun):
        if index_nun.count(index_nun[0]) == len(index_nun) and index_nun[0] != 0:
            return True
        else:
            return False

    # horizontal
    for row in current_game:
        if all_win(row):
            print(f"player {row[0]} is a winner (-)")
            return True
    # vertical
    for col in range(len(current_game)):
        vertical_row = []
        for row in current_game:
            vertical_row.append(row[col])
        if all_win(vertical_row):
            print(f"player {vertical_row[0]} is a winner (|)")
            return True
    # diagonal
    diag = []
    rediag = []

    for ix in range(len(current_game)):
        diag.append(current_game[ix][ix])
    if all_win(diag):
        print(f"player {diag[0]} is a winner(\\)")
        return True

    cols = reversed(range(len(current_game)))
    raws = range(len(current_game))

    for col, raw in zip(cols, raws):
        rediag.append(current_game[col][raw])
    if all_win(rediag):
        print(f"player {rediag[0]} is a winner (/)")
        return True

    return False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game, _ = init_game(game, just_display=True)
    player_choice = itertools.cycle(players)
    while not game_won:
        current_player = next(player_choice)
        print(f'current player is {current_player}')
        played = False
        while not played:
            column_choice = int(input('What column do you like to play (0,1,2) : '))
            row_choice = int(input('What row do you like to play (0,1,2) : '))
            game, played = init_game(game, current_player, row_choice, column_choice)
        if choose_winner(game):
            game_won = True
            again = input('Do you want a play again ? (y/n) ')
            if again.lower() == 'y':
                print('restarting .....')
            elif again.lower() == 'n':
                print('bye.........')
                play = False
            else:
                print('invalid input, ')
                play = False










