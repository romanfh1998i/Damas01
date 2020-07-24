class Deck:

    def __init__(self, color):

                if color == 'x':
                    self.deck =      [[' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                                      ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
                                      [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                      ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                                      [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                                      ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' ']]

                else:
                    self.deck =      [[' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                                      ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                                      [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                      ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
                                      [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                                      ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' ']]

    def deck_output(self):
        """
        metodo para ver tablero
        """
        letter = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        number = ('1', '2', '3', '4', '5', '6', '7', '8')
        print('    ' + ' '.join(letter))

        for index, i in enumerate(self.deck):
            print(f'{number[index]}  ' + '|' + '|'.join(i) + '|' + f'  {number[index]}')

        print('    ' + ' '.join(letter))

    def deck_update(self, coords, move_dest, target=None):
        """
        Metodo para reescribir el tabler
        """
        self.deck[move_dest[0]][move_dest[1]] = self.deck[coords[0]][coords[1]]
        self.deck[coords[0]][coords[1]] = ' '
        return self.deck