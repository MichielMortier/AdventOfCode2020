import copy


def solve(file_name):
    cards = open(file_name).read().split("\n\n")
    players = {}
    for index, player in enumerate(cards):
        players[index] = [int(card.strip()) for card in player.split("\n")[1:]]
    turn = 1
    while players[0] and players[1]:
        print(turn)
        print(players[0], players[1])
        card1 = (players[0].pop(0), 0)
        card2 = (players[1].pop(0), 1)
        players[max(card1, card2, key=lambda c: c[0])[1]].extend(sorted([card1[0], card2[0]], reverse=True))
        turn += 1
    winner = players[0] if players[0] else players[1]
    total = 0
    for index, card in enumerate(reversed(winner)):
        total += (index + 1) * card
    print(total)



def play_recursive_game(player1, player2):
    double_checker = []
    players = {0: player1, 1: player2}
    while players[0] and players[1]:
        if players in double_checker:
            player_win = 0
            break
        else:
            double_checker.append(copy.deepcopy(players))
        # print("Recursive: ", players[0], players[1])
        value1 = players[0].pop(0)
        value2 = players[1].pop(0)
        card1 = (value1, 0)
        card2 = (value2, 1)
        if value1 <= len(players[0]) and value2 <= len(players[1]):
            player_win = play_recursive_game(copy.deepcopy(players[0][:value1]), copy.deepcopy(players[1][:value2]))
        else:
            player_win = max(card1, card2, key=lambda c: c[0])[1]
        players[player_win].extend([value1, value2] if player_win == 0 else [value2, value1])
    return player_win


def solve2(file_name):
    double_checker = []
    cards = open(file_name).read().split("\n\n")
    players = {}
    for index, player in enumerate(cards):
        players[index] = [int(card.strip()) for card in player.split("\n")[1:]]
    turn = 1
    player_win = 0
    while players[0] and players[1]:
        if players in double_checker:
            player_win = 0
            break
        else:
            double_checker.append(copy.deepcopy(players))
        print(turn)
        print(players[0], players[1])
        value1 = players[0].pop(0)
        value2 = players[1].pop(0)
        card1 = (value1, 0)
        card2 = (value2, 1)
        if value1 <= len(players[0]) and value2 <= len(players[1]):
            player_win = play_recursive_game(copy.deepcopy(players[0][:value1]), copy.deepcopy(players[1][:value2]))
        else:
            player_win = max(card1, card2, key=lambda c: c[0])[1]
        players[player_win].extend([value1, value2] if player_win == 0 else [value2, value1])
        turn += 1
    total = 0
    for index, card in enumerate(reversed(players[player_win])):
        total += (index + 1) * card
    print(total)
