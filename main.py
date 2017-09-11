output_transfer = {0: ' ',
                   1: 'O',
                   2: 'X',}
def print_game_status(game_set):
    print("   |   |   ")
    print(" {} | {} | {} ".format(output_transfer[game_set[1]],
                                  output_transfer[game_set[2]],
                                  output_transfer[game_set[3]]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(output_transfer[game_set[4]],
                                  output_transfer[game_set[5]],
                                  output_transfer[game_set[6]]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(output_transfer[game_set[7]],
                                  output_transfer[game_set[8]],
                                  output_transfer[game_set[9]]))
    print("   |   |   ")

def check_same(alliance, compare1, compare2):
    if alliance == compare1 == compare2:
        print("Bingo! We got winner: {}".format(output_transfer[alliance]))
        return True
    return False

def change_role(current_role):
    return (current_role % 2) + 1

GAME_CONTINUE = True
GAME_END = False
TIC_TAC_NUM = 9
ROLE = 0

def game_logic(game_record):
    # 1. We got winner
    print_game_status(game_record)
    zero_flag = False
    for i in range(1, 10):
        alliance = game_record[i]
        if alliance == 0:
            zero_flag = True
            continue
        if i == 1:
            if check_same(alliance, game_record[2], game_record[3]):
                return GAME_END
            if check_same(alliance, game_record[5], game_record[9]):
                return GAME_END
            if check_same(alliance, game_record[4], game_record[7]):
                return GAME_END
        elif i == 2:
            if check_same(alliance, game_record[5], game_record[8]):
                return GAME_END
        elif i == 3:
            if check_same(alliance, game_record[5], game_record[7]):
                return GAME_END
            if check_same(alliance, game_record[6], game_record[9]):
                return GAME_END
        elif i == 4:
            if check_same(alliance, game_record[5], game_record[6]):
                return GAME_END
        elif i == 7:
            if check_same(alliance, game_record[8], game_record[9]):
                return GAME_END
        else:
            continue
    if zero_flag == False:
        print("I'm sorry. We don't have winner for this round")
        return GAME_END
    else:
        return GAME_CONTINUE

if __name__ == "__main__":
    print("Welcome to joseph's tic tac toe!")
    print("This is a dual player game")
    print("Please enter your move with following position")
    print("   |   |   ")
    print(" 1 | 2 | 3 ")
    print("___|___|___")
    print("   |   |   ")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print("   |   |   ")
    print(" 7 | 8 | 9 ")
    print("   |   |   \n\n")
    game_set = [0] * (TIC_TAC_NUM + 1)
    game_set[ROLE] = 1
    while (game_logic(game_set)):
        print("\nIt's {}'s turn".format(output_transfer[game_set[0]]))
        player_input = raw_input("Please enter your decision(1~9): ")
        if not player_input:
            print("No input. Please enter your decision!")
            continue
        position = int(player_input)
        if position not in range(1, 10):
            print("you entered one illegal input: {}".format(position))
            continue
        elif game_set[position] != 0:
            print("This position is already filled by: player {}".format(output_transfer[game_set[position]]))
            continue
        else:
            game_set[position] = game_set[ROLE]
            game_set[ROLE] = change_role(game_set[ROLE])
    print("Thanks for playing joseph's tic tac toe")
    raw_input("Please enter any key to end this game!")
