# -*- coding: utf-8 -*-
import random
import sys


class Map:

    def __init__(self):
        self.matrix = {}

        items = [
            'V', 'V', 'V', 'V', 'V', 'X', 'X', 'X',
        ]
        for obst in range(random.choice(range(10, 25))):
            items.append('#')

        for space in range(98-len(items)):
            items.append('_')

        for i in range(0, 10):
            self.matrix[i] = {}
            for j in range(0, 10):

                if i == 0 and j == 0:
                    self.matrix[i][j] = 'S'
                elif i == 9 and j == 9:
                    self.matrix[i][j] = 'E'
                else:
                    index = random.choice(range(0, len(items)))
                    item = items.pop(index)
                    self.matrix[i][j] = item

    def print_matrix(self):
        sys.stdout.write('  ')
        for line in range(len(self.matrix.items())):
            sys.stdout.write(str(line) + ' ')
        print()
        for line in self.matrix.keys():
            sys.stdout.write(str(line) + ' ')
            for column in self.matrix[line].keys():
                sys.stdout.write(str(self.matrix[line][column]) + ' ')
            print()

    def get_map(self):
        return self.matrix