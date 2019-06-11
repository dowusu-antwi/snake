#!/usr/bin/env python3

"""
Snake
author: dowusu-antwi

User controls snake avatar that grows each time
 it eats (passes over) a food item; dies if runs
 into itself.
"""

import time
import random

snake_directions = {'up': (-1,0), 'down': (1,0),
                    'right': (0,1), 'left': (0, -1)}
directions = [(-1,0), (1,0), (0,1), (0,-1)]

class Snake():

    def __init__(self, body, direction):
        self.anchor = body[len(body)-1]
        self.body = body
        self.direction = direction
        self.body_points = set(body)

    def take_step(self, position):
        """
        This will update the snake by adding a new position
         at its head and popping off the old position, all
         the while keeping track of the points in its body
         with the body_points set field 
        """

        # this updates the head of the snake
        self.anchor = position       
 
        # this updates the body of the snake by
        #  adding new position to front and popping
        #  off the back (snake moves around board)
        end = self.body[0]
        self.body = self.body[1:] + [position]
        self.body_points.remove(end)
        self.body_points.add(position)

    def inside_snake(self, point):
        """
        This returns True if new point is inside snake
        """
        return point in self.body_points

    def set_direction(self, direction):
        """
        """

        self.direction = direction

    def get_direction(self):
        """
        """

        return self.direction

class Mouse():

    def __init__(self, anchor):
        self.anchor = anchor

class Game():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.make_empty_board(width, height)

        self.snake = Snake([(0,0), (0,1), (0,2), (0,3), (0,4), (0,5)], 'down')

    def make_empty_board(self, width, height):
        """
        This will make an empty game board given
        game dimensions
        """
        return [[None for x in range(self.width)]
                for x in range(self.height)]

    def in_boundary(self, point):
        """
        This returns True if point parameter is inside
         the boundary of the game board and False otherwise
        """
        row,col = point
        return ((row>=0 and row<self.height) and
                (col>=0 and col<self.width))

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
        for row, line in enumerate(self.board):
            rendered_row = ['@' if (row,col) == self.snake.anchor else
                            'o' if (row,col) in self.snake.body_points else
                            'x' if elem == 'm' else
                            ' ' for col, elem in enumerate(line)]
            print('|' + ''.join(rendered_row) + '|')
        print('-'*(self.width+2))

    def get_next_state(self, keypress):
        """
        This will look at the current state of the board
         and update each cell according to the positions
         of the cells in the snake body
        """
        
        direction_found = False
        while not direction_found:
            rand_direction = directions[random.randint(0,3)]
            new_direction = snake_directions[keypress]
            new_anchor = (self.snake.anchor[0] + new_direction[0],
                          self.snake.anchor[1] + new_direction[1])
            if self.in_boundary(new_anchor) and not self.snake.inside_snake(new_anchor):
                self.snake.take_step(new_anchor)
                direction_found = True
        print("keypress: %s" % keypress)

    def play_game(self):

        while True:
            self.render_board()
            time.sleep(0.1)
            direction_found = False
            while not direction_found:
                new_direction = directions[random.randint(0,3)]
                new_anchor = (self.snake.anchor[0] + new_direction[0],
                              self.snake.anchor[1] + new_direction[1])
                if self.in_boundary(new_anchor) and not self.snake.inside_snake(new_anchor):
                    self.snake.take_step(new_anchor)
                    direction_found = True

if __name__ == "__main__":

    game = Game(30,10)
    game.play_game()
