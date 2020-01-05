#!/usr/bin/env python3
import random


moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'


    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


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


class ReflectPlayer(Player):
    their_move = random.choice(moves)
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    my_move = random.choice(moves)
    def move(self):
        index = moves.index(self.my_move)
        index = (index + 1) % 3
        return moves[index]
        #if self.my_move == "rock":
        #    return "paper"
        #elif self.my_move == "paper":
        #    return "scissors"
        #elif self.my_move == "scissors":
        #    return "rock"


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
        print(f"Score: Player One: {self.countP1}, Player Two: {self.countP2} \n")


    def play_game(self):
        print("Game start!")
        round = 0
        while True:
           if self.countP1 - self.countP2 == 3:
               break
           elif self.countP2 - self.countP1 == 3:
               break
           else:
               print(f"Round {round} --")
               self.play_round()
               round += 1
        print((f"FINAL SCORE: \nPlayer One: {self.countP1}, Player Two: {self.countP2} \n"))
        if self.countP1 > self.countP2:
            print("Player One is the final WINNER! \n" +
                  "Congratulation!")
        else:
            print("Player Two is the final WINNER! \n" +
                  "Congratulation!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
