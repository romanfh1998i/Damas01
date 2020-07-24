from Tablero import Deck as Decker
from Juego import juego as Game

import AI
import random




def game_init():
    color = select_user()
    my_deck = Decker(color)

    while True:
        print_game_header()  # Prints the game Header
        my_deck.deck_output()  # Prints the actual Deck
        while True:
            usuario = AI.Usuario(color, my_deck)
            usuario.JEnemigo()
            try:
                usercoordsPara = usuario.ccordinadas(input('Entra la coordenada de la dama:'))
                usercoordsto = usuario.ccordinadas(input('Entra los movimientos coordenadas:'))
            except KeyError or IndexError:
                continue

            user_pasos_validacion_1 = usuario.validacion(usercoordsPara)[0]
            user_pasos_validacion_2 = usuario.validacion(usercoordsPara)[1]

            # user_pasos_validacion_1 = usuario.paso.append(usercoordsPara[0])
            # user_pasos_validacion_2 = usuario.paso.append(usercoordsPara[1])
            usuario_damas = Game(usercoordsPara, color, Decker)

            if usuario_damas.attack_targets():
                usercoordsPara = usuario.ccordinadas(input('Entra la coordenada de la dama:'))
                usercoordsto = usuario.ccordinadas(input('Entra los movimientos coordenadas:'))
                usuario_damas.attack(usercoordsto)
                break
            user_paso = usuario_damas.paso(usercoordsto, user_pasos_validacion_1 , user_pasos_validacion_2)
            if user_paso:
                Decker.update(usercoordsPara, usercoordsto)
            else:
                print('Usuario input-Incorrecto!!')

        bot = AI.bot(color, my_deck)
        usuario.JEnemigo()
        bot_pasos = list(bot._paso())
        bot_damas_choice = bot_pasos[0]
        bot_movimiento = bot_pasos[1]

        bot_damas = Game(color, bot_damas_choice, Decker)
        my_deck.update(bot_damas_choice, bot_movimiento)


def print_game_header():
    encabezado = """
            ____                                _______            _                   __            
           / __ \____ _____ ___  ____ ______   / ____(_____  _____(_____  ____  ____ _/ /___  _______
          / / / / __ `/ __ `__ \/ __ `/ ___/  / /   / / __ \/ ___/ / __ \/ __ \/ __ `/ __/ / / / ___/
         / /_/ / /_/ / / / / / / /_/ (__  )  / /___/ / / / / /__/ / / / / / / / /_/ / /_/ /_/ (__  ) 
        /_____/\__,_/_/ /_/ /_/\__,_/____/   \____/_/_/ /_/\___/_/_/ /_/_/ /_/\__,_/\__/\__,_/____/  by Rom's                                                                                         
        """
    print(encabezado)
    return


def select_user():
    usuario = random.choice(['black', 'white'])

    if usuario == 'black':
        color = 'x'
    else:
        color = 'o'

    print('\nYou will play for', usuario + '!\n')
    return color


if __name__ == "__main__":
    game_init()
