import random

class Player:
    def __init__(self, color, deck):
        self.color = color
        self.Enemigo = []
        self.paso = ()
        self.deck = deck


    def JEnemigo(self):
        for x in range(len(self.deck.deck)):
            for y in range(len(self.deck.deck[x])):
                if self.deck.deck[x][y] == self.color:
                    self.Enemigo.append((x, y))

        return self.Enemigo


class Usuario(Player):
    def ccordinadas(self, user_coordinate):
        dict_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        dict_number = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}

        y = dict_letters[user_coordinate[0]]
        x = dict_number[user_coordinate[1]]
        converted_coordinates = (x, y)

        return converted_coordinates

    def validacion(self, damascoordinadas):
        condicion1 = (damascoordinadas[0] + 1, damascoordinadas[1] + 1)
        condicion2 = (damascoordinadas[0] - 1, damascoordinadas[1] - 1)
        return condicion1, condicion2


class bot(Player):
    def validacion(self, damascoordinadas):
        condicion1 = (damascoordinadas[0] + 1, damascoordinadas[1] + 1)
        condicion2 = (damascoordinadas[0] - 1, damascoordinadas[1] - 1)
        return condicion1, condicion2

    def _paso(self):
        nada = []
        botdamas = []
        botpasos = []
        for x in range(len(self.deck.deck)):
            for y in range(len(self.deck.deck[x])):
                if self.deck.deck[x][y] == ' ':
                    nada.append((x, y))
        for i in self.Enemigo:
            for ef in nada:
                if ef == self.validacion(i)[0] or ef == self.validacion(i)[1]:
                    botdamas.append(i)
                    botpasos.append(ef)
        unicodamas = list(set(botdamas))
        unicopasos = list(set(botpasos))
        print('Bot decision correcta', unicodamas)
        botpasos = random.choice(unicodamas)
        print('Bot Damas pasos ', botpasos)

        return [botpasos, botdamas]
