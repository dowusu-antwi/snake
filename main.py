#!/usr/bin/env python3

"""
Snake
author: dowusu-antwi

User controls snake avatar that grows each time
 it eats (passes over) a food item; dies if runs
 into itself.
"""

class Snake():

    def __init__(self, anchor, length, direction):
        self.anchor = anchor
        self.length = length
        self.direction = direction

class Mouse():

    def __init__(self, anchor):
        self.anchor = anchor

class Game():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.make_empty_board(width, height)

    def make_empty_board(self, width, height):
        """
        This will make an empty game board given
        game dimensions
        """
        return [[0 for x in range(self.width)]
                for x in range(self.height)]

    def render_board(self):
        """
        This renders the board, treating alives (1)
         as hashes (#) and deads (0) as spaces, and
         uses asterisks for the boundary
        """

        # this prints the top and bottom boundaries,
        #  an in between renders '*' + row cells + '*'
        #  for each row on the board
        print('-'*(self.width+2))
        for row in self.board:
            rendered_row = ['o' if elem == 's' else
                            'x' if elem == 'm' else
                            ' ' for elem in row]
            print('|' + ''.join(rendered_row) + '|')
        print('-'*(self.width+2))

if __name__ == "__main__":

    game = Game(30,10)
    game.render_board()
