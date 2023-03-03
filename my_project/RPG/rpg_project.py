#!/usr/bin/env python3

import requests
from random import randint

"""Show the game instructions when called"""
def showInstructions():
    """Show the game instructions when called"""
    print('''
    RPG Game    
    ========    
    Commands:      
        go [direction]      
        get [item]    
        ''')

def showStatus():
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory:', inventory)
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
inventory = []

# sphinx API logic
APIURL = "https://catfact.ninja/fact"

def allKnowingSphinx():
    fact = requests.get(f"{APIURL}")
    fact = fact.json()
    print(fact['fact'])


riddle_questions = {
    "Who created Python?: ": 
        {
        "choices": "A. Jeff Bezos, B. Elon Musk, C. Bill Gates, D. Guido van Rossum",
        "answer" : "D"
        },
    "What year was the Python born?: ":
        {
        "choices": "A. 1988, B. 1991, C. 2002, D. 2010",
        "answer" : "B"
        },
    "What statement/function does Python uses to display messages onto the screen?:": {
        "choices": "A. console.log(), B. System.out.println(), C. print(), D. println()",
        "answer" : "C"
    }
    }

def riddles():

    correct_guesses = 0

    for index, (key, value) in enumerate(riddle_questions.items()):

        print(f"***********************************************************\n{key}")
        print(value.get("choices"))

        guess = input("Select answers & type (A, B, C, or D): ")
        guess = guess.upper()

        if guess == value.get("answer"):
            correct_guesses += 1
            print(f"you got it! So far you correctly guessed: {correct_guesses}")            
        else:
            correct_guesses -= 1
            print(f"WRONG! Deducting your score. So far you correctly guessed: {correct_guesses}")

    if correct_guesses >= 3:
        print("Good job, you guessed all 3 answers correctly. You have earned an item: 'star'. You can go south now.")
        inventory.append("Star")
    else:
        print("*********** GAME OVER! *********** \nYou didn't make it! Restart the program to start over!")
        quit()
        
        # print(f"\nWell, you exhuasted all my questions prepared! Let's try again!")
        # riddles()
    

def game():

    choices = ["rock", "paper", "scissors"]
    computer = choices[randint(0,2)]
    win_count=0

    while True:
        if win_count > 0:
            break
        player = input("Let's play a game with a computer! Please input Rock, Paper or Scissors. \n>>> ")
        player = player.lower()

        if player == computer:
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print(f"You lose! {computer} covers {player}")
            else:
                print(f"You win! {player} smashes {computer}! You can move again now!")
                win_count+=1
        elif player == "paper":
            if computer == "scissors":
                print(f"You lose! {computer} cut {player}")
            else:
                print(f"You win! {player} covers {computer}! You can move again now!")
                win_count+=1
        elif player == "scissors":
            if computer == "rock":
                print(f"You lose! {computer} smashes {player}")
            else:
                print(f"You win! {player} cut {computer}")
                win_count+=1
        else:
            print("Something went wrong. Try check your spelling!")

        computer = choices[randint(0,2)]



rooms = {

    'Hall': {
        'south': 'Sphinx Room',
        'east': 'Dining Room',
        'item': 'key'
    },    
    'Sphinx Room': {
        'north': 'Hall',
        'south': 'Kitchen',
        'item': 'encyclopedia'
    },
    'Kitchen': {
        'north': 'Sphinx Room',

    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Riddle Room',
        'item': 'potion'
    },
    'Riddle Room': {
        'north': 'Dining Room',
        'south': 'Garden'
    },
    'Garden': {
        'north': 'Riddle Room'
    }
}



currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    if move[0] == 'get' :
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
             print('Can\'t get ' + move[1] + '!')

    if currentRoom == 'Riddle Room':
        print("Haha, you thought you can move around easily like that? You must successfully solve 3 random questions to move north or south! Good luck!")
        riddles()
    
    if currentRoom == 'Sphinx Room':
        print("Hello explorer! It is I— the All-knowing Sphinx!\n")
        print("Here is a cat fact for your travels: ")
        allKnowingSphinx()

    if currentRoom == 'Kitchen':
        game()

    # if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    #     print('A monster has got you ... GAME OVER!')
    #     break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
