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

    def take_step(self, position, mouse_eaten):
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
        
        # only pops off the back if a mouse hasn't
        #  been eaten
        if not mouse_eaten:
            end = self.body[0]
            self.body = self.body[1:] + [position]
            self.body_points.remove(end)
        else:
            self.body = self.body + [position]
            new_anchor = mouse_eaten.get_new_anchor(self)
            mouse_eaten.is_eaten(new_anchor)

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

    def __init__(self, anchor, board_dimensions):
        self.anchor = anchor
        self.board_width, self.board_height = board_dimensions

    def is_this_mouse_position(self, position):
        """
        This returns True if the given position is
         taken by the mouse
        """
        return position == self.anchor

    def get_new_anchor(self, snake):
        """
        This gets a new anchor that is inside the game
         board, but also not inside the snake
        """
        new_anchor = (random.randint(0,self.board_height), random.randint(0,self.board_width))
        while snake.inside_snake(new_anchor):
            new_anchor = (random.randint(0,self.board_height), random.randint(0,self.board_width))
        return new_anchor

    def is_eaten(self, new_anchor):
        """
        """
        self.anchor = new_anchor

class Game():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.make_empty_board(width, height)

        self.snake = Snake([(0,i) for i in range(5)], 'down')

        self.mice = self.generate_mice(1)

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

    def generate_mice(self, mice_count):
        """
        This will generate a number of mice and put them
         all in random places on the game board, returning
         a list of mice
        """

        # this will generate a list of mice and place
        #  them on the board in random positions (so
        #  long as the position is not taken by the snake)
        w, h, mice = self.width, self.height, []
        for mouse in range(mice_count):
            mouse_position = (random.randint(0,h), random.randint(0,w))
            while self.snake.inside_snake(mouse_position):
                mouse_position = (random.randint(0,h), random.randint(0,w))
            mice.append(Mouse(mouse_position, (self.width, self.height)))

        return mice

    def is_anchor_a_mouse(self, anchor):
        """
        This returns True if the given anchor position is
         occupied by a Mouse, False otherwise
        """

        for mouse in self.mice:
            if mouse.is_this_mouse_position(anchor):
                return mouse
        return False

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
                            'm' if self.is_anchor_a_mouse((row, col)) else
                            ' ' for col, elem in enumerate(line)]
            print('|' + ''.join(rendered_row) + '|')
        print('-'*(self.width+2))

    def get_next_state(self, keypress):
        """
        This will look at the current state of the board
         and update each cell according to the positions
         of the cells in the snake body
        """
       
        # this looks for a new direction by getting the keypress
        #  and computing the next anchor, only updating if the
        #  next anchor is a valid anchor 
        direction_found = False
        while not direction_found:
            new_direction = snake_directions[keypress]
            new_anchor = (self.snake.anchor[0] + new_direction[0],
                          self.snake.anchor[1] + new_direction[1])

            if self.in_boundary(new_anchor) and not self.snake.inside_snake(new_anchor):

                # this will check for a mouse in the new position,
                #  and if one is found, it will increment the snake's
                #  length by 1 by not removing the snake's end
                mouse_eaten = self.is_anchor_a_mouse(new_anchor)
                self.snake.take_step(new_anchor, mouse_eaten)
                direction_found = True

        print("keypress: %s" % keypress)
        print("mice: %s" % self.mice)

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
                    mouse_eaten = self.is_anchor_a_mouse(new_anchor)
                    self.snake.take_step(new_anchor, mouse_eaten)
                    direction_found = True

if __name__ == "__main__":

    game = Game(30,10)
    game.play_game()
