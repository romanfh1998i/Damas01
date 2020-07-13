import random
import Tablero
import AI

import Juego

encabezado = """
    ____                                _______            _                   __            
   / __ \____ _____ ___  ____ ______   / ____(_____  _____(_____  ____  ____ _/ /___  _______
  / / / / __ `/ __ `__ \/ __ `/ ___/  / /   / / __ \/ ___/ / __ \/ __ \/ __ `/ __/ / / / ___/
 / /_/ / /_/ / / / / / / /_/ (__  )  / /___/ / / / / /__/ / / / / / / / /_/ / /_/ /_/ (__  ) 
/_____/\__,_/_/ /_/ /_/\__,_/____/   \____/_/_/ /_/\___/_/_/ /_/_/ /_/\__,_/\__/\__,_/____/  by Rom's                                                                                         
"""
color = random.choice(['black', 'white'])

if color == 'black':
    user_color = 'x'
    bot_color = 'o'

else:
    user_color = 'o'
    bot_color = 'x'

print('\nYou will play for', color + '!\n')


deck = Tablero.Deck(user_color)

while True:
    print(encabezado)

    deck.deck_output()

# user logic
    while True:
        user = AI.Usuario(user_color, deck.deck)
        user.JEnemigo()

        try:
            user_coords_from = user.ccordinadas(input('Enter your checker coordinates: '))
            user_coords_to = user.ccordinadas(input('Enter your move destination coordinates: '))
        except KeyError or IndexError:
            continue

        user_step_validation_1 = user.validacion(user_coords_from)[0]
        user_step_validation_2 = user.validacion(user_coords_from)[1]

        user_checker = Juego.Checker(user_coords_from, user_color, deck.deck)

        if user_checker.attack_needed(user.JEnemigo()):

            user_coords_from = user.ccordinadas(input('Enter your checker for attack: '))
            user_coords_to = user.ccordinadas(input('Enter your move destination coordinates: '))
            user_checker.attack(user_coords_to)
            break

        user_step = user_checker.step(user_coords_to, user_step_validation_1, user_step_validation_2)

        if user_step:
            deck.deck_update(user_coords_from, user_coords_to)
            break
        else:
            print('User input - incorrect!')

        # Bot logic
    bot = Juego.Bot(bot_color, deck.deck)
    bot.player_army()

    bot_step = list(bot.bot_step())

    bot_checker_choice = bot_step[0]

    bot_movement = bot_step[1]

    bot_checker = Tablero.Checker(bot_color, bot_checker_choice, deck.deck)

    deck.deck_update(bot_checker_choice, bot_movement)
 