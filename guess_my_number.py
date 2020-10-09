# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:59:08 2020

@author: 33624
"""

import random

MIN=0
MAX=1000

class GuessMachine():
    def __init__(self):
        self._number_to_guess = random.randint(MIN,MAX)
        self.number_of_attempt = 0
    def guess(self,num):
        self.number_of_attempt +=1
        if num<self._number_to_guess:
            return 'too low'
        elif num>self._number_to_guess:
            return 'too high'
        else:
            return 'found'

if __name__== '__main__':
    number_to_guess = random.randint(MIN,MAX)
    print('Hey! Try to guess a number between %d and %d' % (MIN,MAX))
    while True:
        user_input = input('Your guess?')
        try:
            user_attempt=int(user_input)
            if user_attempt==number_to_guess:
                print('Fantastic, you coud find the number I had in mind!')
                break
            elif user_attempt < number_to_guess:
                print('too low')
            else:
                print('too high')
        except ValueError:
            print('You joker...that was not an integer!')
