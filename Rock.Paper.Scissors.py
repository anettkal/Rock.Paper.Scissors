#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        move = random.choice(moves)
        return move

class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, scissors? >").lower()
            if move == "rock" or move == "paper" or move == "scissors":
                break
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.countP1 = 0
        self.countP2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("** TIE **")
        elif beats(move1,move2) is True:
            self.countP1 += 1
            print("** PLAYER ONE WINS **")
        else:
            self.countP2 += 1
            print("** PLAYER TWO WINS **")
        print(f"Score: Player One {self.countP1}, Player Two {self.countP2}")


    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round} --")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
