"""
Python emulation of the famous card game drunkman
"""

from random import shuffle
from collections import deque
import logging

deck = ['6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8',
        '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J',
        'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']


"""
Checks which card is bigger
Returns True if card1 is bigger, False is card2 is bigger
"""
def beats(card1, card2):
    cards = ('6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    if card1 == '6' and card2 == 'A':
        return True
    if card1 == 'A' and card2 == '6':
        return False
    if cards.index(card1) > cards.index(card2):
        return True

    return False


if __name__ == '__main__':
    logging.basicConfig(filename='drunkman.log', level=logging.INFO)
    shuffle(deck)
    player1 = deque(deck[:18])
    player2 = deque(deck[18:])

    step = 0

    while player1 and player2:
        step += 1
        cards1 = [player1.popleft()]
        cards2 = [player2.popleft()]

        while cards1[-1] == cards2[-1]:
            logging.info(f'Spor on {cards1[-1]} and {cards2[-1]}')
            hidden1 = player1.popleft()
            cards1.append(hidden1)
            logging.info(f'Player 1 has put {hidden1} as hidden card')
            hidden2 = player2.popleft()
            cards2.append(hidden2)
            logging.info(f'Player 2 has put {hidden2} as hidden card')
            open1 = player1.popleft()
            cards1.append(open1)
            logging.info(f'Player 1 has put {open1} as open card')
            open2 = player2.popleft()
            cards2.append(open2)
            logging.info(f'Player 2 has put {open2} as open card')

        if beats(cards1[-1], cards2[-1]):
            player1.extend(cards1)
            player1.extend(cards2)
            logging.info(f'One the step {step} Player 1 got {cards2[-1]} with {cards1[-1]}, '
                         f'the bank taken {cards1, cards2}')
            logging.info(f'Players 1 cards: {player1}')
            logging.info(f'Players 2 cards: {player2}')
        else:
            player2.extend(cards1)
            player2.extend(cards2)
            logging.info(f'On the step {step} Player 2 got {cards1[-1]} with {cards2[-1]}, '
                         f'the bank taken {cards1, cards2}')
            logging.info(f'Players 1 cards: {player1}')
            logging.info(f'Players 2 cards: {player2}')

    if player1:
        print(f'Player 1 wins! Number of steps {step}')
    else:
        print(f'Player 2 wins! Number of steps {step}')