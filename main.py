import copy
import matplotlib.pyplot as plt
import numpy as np

org_deck = [
    'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
    'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
    'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
    'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD'
]


def king_king(deck):
    for i in range(len(deck) - 1):
        if deck[i][0] == 'K' and deck[i + 1][0] == 'K':
            return True


def king_queen(deck):
    n = len(deck)
    for i in range(n - 1):
        if deck[i][0] + deck[i + 1][0] in ['KQ', 'QK']:
            return True
        if i != n - 2:
            if deck[i][0] + deck[i + 2][0] in ['KQ', 'QK']:
                return True


def monte_carlo(n):
    res = 0
    for i in range(n):
        deck = copy.deepcopy(org_deck)
        np.random.shuffle(deck)
        if king_king(deck):
            res += 1

    if res == 0:
        return 0

    return res / n * 100


duration = []

for a in range(7):
    result = monte_carlo(10 ** a)
    duration.append(result)
    print('10^' + str(a) + ' -> ', result)


plt.figure(figsize=(3,1.5))
plt.hist(duration,density=True)
plt.axvline(9,color='r')
plt.show()
