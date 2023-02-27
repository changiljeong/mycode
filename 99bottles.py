#!/bin/usr/env python3

def main(n):
        for bottle in range(n,1,-1):
            if (bottle == 2):
                print ("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.")
            if (bottle == 1):
                print (f"{bottle} bottle of beer on the wall, 1 bottle of beer.")
            else:
                print (f"{bottle} bottles of beer on the wall, {bottle} bottles of beer.\nTake one down and pass it around, {bottle-1} bottles of beer on the wall.")

        print ("Take one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.")


if __name__ == "__main__":
  main(99)
