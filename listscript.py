#!/usr/bin/env python3
"""Working with lists"""

def main():
    grocery_list=[]
    while True:
        print("Enter an item to add to the list or 'done' if finished")
        grocery_item = input("What do you need from the store?")
        if grocery_item.lower() == 'done':
            print("this is your grocery list:", grocery_list)
            print("The last item on your regular list is:", grocery_list[-1])
            break
        else: grocery_list.append(grocery_item)

if __name__ == "__main__":
    main()

