#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 15-09-2020 18:44:37

    [Description]
"""
__author__ = "Benedict Wilkins"
__email__ = "benrjw@gmail.com"
__status__ = "Development"

import copy
import numpy as np
from ..pygame import PyGameEnvironment 

DEFAULT_SIZE = (64,64)

class Player:

    def __init__(self, x, y, w, h, speed=1):
        self.position = np.array([x,y])
        self.size = np.array([w,h])
        self.speed = 1

    def center(self):
        return self.position + self.size/2


physics = [
    {"up":np.array([0,-1]), "down":np.array([0,1])},                           # simple
    {"up":np.array([0,-1]), "down":np.array([0,1]), "noop":np.array([0,0])},  # simple + no-op
    {"up":np.array([0,-1]), "down":np.array([0,1]), "left":np.array([-1,0]), "right":np.array([1,0])}
]

class Paddles(PyGameEnvironment):

    def __init__(self, size=DEFAULT_SIZE, physics=physics[0], player2_policy=None, dtype=np.float32, format="CHW"):
        super(Paddles, self).__init__(list(physics.keys()), display_size=size, background_colour=(0,0,0), dtype=dtype, format=format)
        self.physics = physics
        self.player1 = Player(size[0]*1/8, size[1]/2, size[0]/20, size[1]/8)
        self.player2 = Player(size[0]*7/8, size[1]/2, size[0]/20, size[1]/8)
        self.__initial_state = copy.deepcopy((self.player1, self.player2))
        if player2_policy is None:
            player2_policy = lambda self, *args, **kwargs: self.action_space.sample()
        self.player2_policy = player2_policy
        self.display_size = np.array(self.display_size)

    def step(self, action):
        #update state
        self.player1.position += self.player1.speed * self.physics[self.actions[action]]
        self.player1.position = np.clip(self.player1.position, 0, self.display_size - self.player1.size)
        self.player2.position += self.player2.speed * self.physics[self.actions[self.player2_policy(self, self.get_image(), action)]]
        self.player2.position = np.clip(self.player2.position, 0, self.display_size - self.player2.size)

        # update graphics
        self.clear(self.background_colour) 
        self.fill_rect(self.player1.position, self.player1.size)
        self.fill_rect(self.player2.position, self.player2.size)

        return self.get_image(), 0., False, None

    def reset(self):
        self.player1, self.player2 = copy.deepcopy(self.__initial_state)
        self.clear(self.background_colour) # clear graphics buffer
        self.fill_rect(self.player1.position, self.player1.size)
        self.fill_rect(self.player2.position, self.player2.size)

        return self.get_image()

def PaddlesNoop(**kwargs):
    kwargs['physics'] = physics[1]
    return Paddles(**kwargs)

def PaddlesShared(**kwargs):
    kwargs['physics'] = physics[0]
    kwargs['player2_policy'] = lambda self, state, action, *args, **kwargs: np.random.choice([action, self.action_space.sample()])
    return Paddles(**kwargs)





