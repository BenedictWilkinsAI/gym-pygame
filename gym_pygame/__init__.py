#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 15-09-2020 18:44:00

    [Description]
"""
__author__ = "Benedict Wilkins"
__email__ = "benrjw@gmail.com"
__status__ = "Development"

import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.environ["SDL_VIDEODRIVER"] = 'dummy'

from gym.envs.registration import register

from . import envs

_all__ = ('envs', )

register(id='Paddles-v0', entry_point='gym_pygame.envs:Paddles')
register(id='Paddles-v1', entry_point='gym_pygame.envs:PaddlesNoop')
register(id='Paddles-v2', entry_point='gym_pygame.envs:PaddlesShared')

register(id='Expander-v0', entry_point='gym_pygame.envs:Expander')
register(id='Expander-v1', entry_point='gym_pygame.envs:ExpanderNoop')

register(id='Circular-v0', entry_point='gym_pygame.envs:Circular')
register(id='Circular-v1', entry_point='gym_pygame.envs:CircularNoop')

register(id='Motorway-v0', entry_point='gym_pygame.envs:Motorway')
register(id='Motorway-v1', entry_point='gym_pygame.envs:MotorwayNoop')

register(id='Windy-v0', entry_point='gym_pygame.envs:Windy')
register(id='windy-v1', entry_point='gym_pygame.envs:WindyNoop')

register(id='Balls-v0', entry_point='gym_pygame.envs:BallsS')
register(id='Balls-v1', entry_point='gym_pygame.envs:BallsI')
register(id='Balls-v2', entry_point='gym_pygame.envs:BallsC')
register(id='Balls-v3', entry_point='gym_pygame.envs:BallsW')
register(id='Balls-v4', entry_point='gym_pygame.envs:BallsO')