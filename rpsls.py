#!/usr/bin/python

from collections import OrderedDict
from random import choice, seed
from sys import exit


WEAPONS = OrderedDict([
    ('rock', 1),
    ('paper', 2),
    ('scissors', 3),
    ('lizard', 5),
    ('spock', 4)
])


EXPLANATIONS = {
    'lizardlizard': 'Lizard equals lizard',
    'lizardpaper': 'Lizard eats paper',
    'lizardrock': 'Rock crushes lizard',
    'lizardscissors': 'Scissors decapitate lizard',
    'lizardspock': 'Lizard poisons spock',
    'paperpaper': 'Paper equals paper',
    'paperrock': 'Paper wraps rock',
    'paperscissors': 'Scissors cut paper',
    'paperspock': 'Paper disproves Spock',
    'rockrock': 'Rock equals rock',
    'rockscissors': 'Rock breaks scissors',
    'rockspock': 'Spock vapourises rock',
    'scissorsscissors': 'Scissors equal scissors',
    'scissorsspock': 'Spock breaks scissors',
    'spockspock': 'Spock equals Spock'
}


def do_battle(player_weapon, cpu_weapon):
    explanation = EXPLANATIONS[''.join(sorted([player_weapon, cpu_weapon]))]
    result = (WEAPONS[player_weapon] - WEAPONS[cpu_weapon]) % 5
    if result == 0:
        message = 'It\'s a draw.'
    elif result % 2 == 0:
        message = 'CPU wins!'
    else:
        message = 'Player wins!'
    return '{}. {}'.format(explanation, message)


def is_valid_weapon(weapon):
    return weapon in WEAPONS.keys()


def get_random_weapon():
    seed()
    return choice(WEAPONS.keys())


def run():
    print 'Choose your weapon ({}), or quit:'.format(', '.join(WEAPONS.keys()))
    player_weapon = raw_input('> ').lower()
    if player_weapon == 'quit':
        print 'Thanks for playing.'
        exit()
    if not is_valid_weapon(player_weapon):
        print '\'{}\' is not a valid weapon, try again.\n'.format(player_weapon)
        run()
    cpu_weapon = get_random_weapon()
    print '(Player) {} - vs - {} (CPU)'.format(player_weapon, cpu_weapon)
    print '{}\n'.format(do_battle(player_weapon, cpu_weapon))
    run()


if __name__ == '__main__':
    run()


