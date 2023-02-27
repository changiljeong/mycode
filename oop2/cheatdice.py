#!/usr/bin/python3

from random import randint

class Player:
    def __init__(self):
        self.dice=[]

    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice


class Cheat_Swapper(Player):
    def cheat(self):
        self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
    def cheat(self):
        i = 0;
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

class Cheat_Mulligan(Player):
    def cheat(self):
        if sum(self.dice) <= 9:
            self.dice = []
            for i in range(3):
                self.dice.append(random.randint(1,6))

class Cheat_Extra_Die(Player):
    def cheat(self):
        self.dice.append(random.randit(1,6))


class Cheat_Lucky_Die(Player):
    def cheat(self):
        if self.dice[0] < 3:
            sef.dice[0] = random.randint(3,6)

class Cheat_Saboteur(Player):
    def cheat(self, other_player):
        other_player.dice = [random.randit(1,3) for i in range(3)]

if __name__ == "__main__":
    main()
