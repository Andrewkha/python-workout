"""
Python emulation of the famous card game drunkman
"""

from random import shuffle
from collections import deque
import csv

deck = ['6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8',
        '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J',
        'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']


def beats(card1, card2):
    """
    Checks which card is bigger
    Returns True if card1 is bigger, False is card2 is bigger
    """

    cards = ('6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    if card1 == '6' and card2 == 'A':
        return True
    if card1 == 'A' and card2 == '6':
        return False
    if cards.index(card1) > cards.index(card2):
        return True

    return False


def main(game):
    """
    implements main logic, returns number of steps taken
    filename - the file to record the game progress 
    """
    shuffle(deck)
    player1 = deque(deck[:18])
    player2 = deque(deck[18:])

    log = []

    step = 0

    while player1 and player2:
        step += 1
        cards1 = [player1.popleft()]
        cards2 = [player2.popleft()]

        while cards1[-1] == cards2[-1]:
            log.append(f'Spor on {cards1[-1]} and {cards2[-1]}')
            try:
                hidden1 = player1.popleft()
            except IndexError:
                log.append('Player 1 out of cards')
                break
            cards1.append(hidden1)
            log.append(f'Player 1 has put {hidden1} as hidden card')
            try:
                hidden2 = player2.popleft()
            except IndexError:
                log.append('Player 2 out of cards')
                break
            cards2.append(hidden2)
            log.append(f'Player 2 has put {hidden2} as hidden card')

            try:
                open1 = player1.popleft()
                open2 = player2.popleft()
            except IndexError:
                log.append(f'Using hidden cards for argue')
                print(f'Game {game}: Using hidden cards for argue')
            else:
                cards1.append(open1)
                log.append(f'Player 1 has put {open1} as open card')
                cards2.append(open2)
                log.append(f'Player 2 has put {open2} as open card')

        if beats(cards1[-1], cards2[-1]):
            player1.extend(cards1)
            player1.extend(cards2)
            log.append(f'One the step {step} Player 1 got {cards2[-1]} with {cards1[-1]}, '
                         f'the bank taken {cards1, cards2}')
            log.append(f'Players 1 cards: {player1}')
            log.append(f'Players 2 cards: {player2}')
        else:
            player2.extend(cards1)
            player2.extend(cards2)
            log.append(f'On the step {step} Player 2 got {cards1[-1]} with {cards2[-1]}, '
                         f'the bank taken {cards1, cards2}')
            log.append(f'Players 1 cards: {player1}')
            log.append(f'Players 2 cards: {player2}')

        if step > 10000:
            print(f'Game {game}: Looped')
            log.append(f'Game {game}: Looped')
            with open(f'drunk/game_{game}.txt', 'w') as file:
                file.write('\n'.join(log))
            return step

    if player1:
        print(f'Game {game}: Player 1 wins! Number of steps {step}')
    else:
        print(f'Game {game}: Player 2 wins! Number of steps {step}')

    with open(f'drunk/game_{game}.txt', 'w') as file:
        file.write('\n'.join(log))

    return step


if __name__ == '__main__':
    steps = []
    for i in range(1000000):
        steps.append(main(i))

    count_cycled = len([x for x in steps if x == 10001])
    not_cycled = [x for x in steps if x != 10001]
    steps = [(str(x),) for x in steps]
    print(steps)
    print(f"number of looped  games {count_cycled}")
    print(f"avarage length of the game {sum(not_cycled) / len(not_cycled)}")
    print(f"minimal steps count: {min(not_cycled)}")
    print(f"maximum steps count: {max(not_cycled)}")
    with open('drunker.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(steps)