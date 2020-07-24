import Tablero
class juego:



        def __init__(self, coordenadas, color, deck):

            self.coordenadas = coordenadas
            self.color = color
            self.deck  = deck

        def step(self, move_dest, valid_condition1, valid_condition2):

            correct_destination = (move_dest == valid_condition1 or move_dest == valid_condition2)
            if self.deck.deck[self.coordenadas[0]][self.coordenadas[1]] == self.color:
                if correct_destination and self.is_empty(move_dest):
                    result = True
                    return result

                else:

                    result = False
                return result
            else:
                print('This is empty field')
                result = False
                return result



        def empty_field_list(self):

            nada = []

            for x in range(len(self.deck.deck)):
                for y in range(len(self.deck.deck[x])):
                    if self.deck.deck[x][y] == ' ':
                        nada.append((x, y))
            return nada

        def is_empty(self, move_dest):
            """
            Metodo que cheque si el campo esta vacio
            """
            if move_dest in self.empty_field_list():
                is_empty = True
            else:
                print('Field is not empty')
                is_empty = False

            return is_empty

        def attack_needed(self, checkers_army):

            enemy_army = []


            first_check = []
            second_check = []

            for i in checkers_army:

                for j in enemy_army:

                    if j == (i[0] + 1, i[1] + 1) or j == (i[0] - 1, i[1] - 1) or j == (i[0] + 1, i[1] - 1) or j == (
                            i[0] - 1, i[1] + 1):
                        first_check.append(j)

            for j in first_check:
                for ef in self.empty_field_list():

                    if ef == (j[0] + 1, j[1] + 1) or ef == (j[0] - 1, j[1] - 1) or ef == (j[0] + 1, j[1] - 1) or ef == (
                            j[0] - 1, j[1] + 1):
                        second_check.append(ef)

            if not second_check:
                result = False

            elif second_check:
                print('You need to attack!!!')
                result = True

            else:
                result = False

            return result

        def attack_targets(self):
            """
            Method configurates dictionary with targets and fields for jumping
            :return: dict
            """
            targ_1 = self.coordenadas[0] - 1, self.coordenadas[1] - 1
            targ_2 = self.coordenadas[0] - 1, self.coordenadas[1] + 1
            targ_3 = self.coordenadas[0] + 1, self.coordenadas[1] - 1
            targ_4 = self.coordenadas[0] + 1, self.coordenadas[1] + 1

            step_attack_1 = self.coordenadas[0] - 2, self.coordenadas[1] - 2
            step_attack_2 = self.coordenadas[0] - 2, self.coordenadas[1] + 2
            step_attack_3 = self.coordenadas[0] + 2, self.coordenadas[1] - 2
            step_attack_4 = self.coordenadas[0] + 2, self.coordenadas[1] + 2

            dict_attack = {step_attack_1: targ_1, step_attack_2: targ_2, step_attack_3: targ_3, step_attack_4: targ_4}

            return dict_attack

        def attack(self, move_dest):
            """
            Metodo que describe y reescribe un metodo antes de un ataque
            """
            dict_attack = self.attack_targets()

            if move_dest in dict_attack and self.is_empty(move_dest):
                target = dict_attack[move_dest]

                if self.deck[target[0]][target[1]] != self.color and self.deck[target[0]][target[1]] != ' ':
                    self.deck[move_dest[0]][move_dest[1]] = self.deck[self.coordenadas[0]][self.coordenadas[1]]
                    self.deck[self.coordenadas[0]][self.coordenadas[1]] = ' '
                    self.deck[target[0]][target[1]] = ' '
                    return self.deck

                else:
                    print('This step is not correct. Do another one')
