import os #Imports "os" giving us the ability to "clear" the terminal
import time #Imports "time" giving us the ability to "sleep" the program
import sqlite3 #Imports "sqlite3" giving us the ability to access and change our database
from SafeSleepClearr import safe_sleep_clear #Connects the 2 files giving us the ability to use whats in SafeSleepClearr
from INTERNAL_functions import DisplayCards, EditCards, AddCards, RemoveCards #Connects the 2 files
from config2 import configure #You will need to find out.....

DATABASE = 'DataBase.db' #Defines what I mean by "DATABASE"

#The main function runs all other functions and the home page
def main():
    while True:
        os.system('clear') #Gives the effect that the terminal was cleared
        print('-- Monstars --\n')
        print('''    1. Display all cards
    2. Add cards
    3. Edit cards
    4. Remove cards
    5. Exit
    6. Evidence''')
        user_opt = input(': ').capitalize()

        if user_opt == '1' or user_opt.lower() == 'Display all cards':
            safe_sleep_clear(0.1) #Runs safesleepclearr and sleeps for 0.1 seconds
            DisplayCards() #Runs DisplayCards in INTERNAL_functions
            done = input('exit? (y/n) ').capitalize()

            if done == 'Y':
                main() #Re-runs main function essentually bringing the user to the beginning
            elif done == 'N':
                time.sleep(1) #Sleeps the code for 1 second
                print('Why did you even type this in the first place...')
                time.sleep(2.5) #Sleeps the code for 2.5 seconds
                print('you egg.')
                safe_sleep_clear(2) #Runs safesleepclearr and sleeps for 2 seconds
                exit() #Exits the code
            else:
                done = input('exit? (y/n) ').capitalize()

        elif user_opt == '2' or user_opt.lower() == 'Add cards':
            safe_sleep_clear(0.1) #Runs safesleepclearr and sleeps for 0.1 seconds
            print('-- Monstars --\n')
            name = input("Enter a new monster's name (try to pick one that doesnt exist already): ")
            if name == "":
                print('Try within 14 letters')
                name = input("Enter a new monster's name (try to pick one that doesnt exist already): ")
            name_len = len(name)
            if name_len <= 14:
                pass
            else:
                print('Try within 14 letters')
                name = input("Enter a new monster's name (try to pick one that doesnt exist already): ")
            strength = int(input("Enter a strength value: "))
            if 1 <= strength <= 20:
                pass
            elif strength == "":
                print('Try within 1 and 20')
                strength = int(input("Enter a strength value: "))
            else:
                print('Try within 1 and 20')
                strength = int(input("Enter a strength value: "))
            speed = int(input("Enter a speed value: "))
            if 1 <= speed <= 20:
                pass
            elif speed == "":
                print('Try within 1 and 20')
                speed = int(input("Enter a speed value: "))
            else:
                print('Try within 1 and 20')
                speed = int(input("Enter a speed value: "))
            stealth = int(input("Enter a stealth value: "))
            if 1 <= stealth <= 20:
                pass
            elif stealth == "":
                print('Try within 1 and 20')
                stealth = int(input("Enter a stealth value: "))
            else:
                print('Try within 1 and 20')
                stealth = int(input("Enter a stealth value: "))
            cunning = int(input("Enter a cunning value: "))
            if 1 <= cunning <= 20:
                pass
            elif cunning == "":
                print('Try within 1 and 20')
                cunning = int(input("Enter a cunning value: "))
            else:
                print('Try within 1 and 20')
                cunning = int(input("Enter a cunning value: "))
            result = AddCards(DATABASE, name, strength, speed, stealth, cunning)
            print(result) #Prints the final result of AddCards

        elif user_opt == '3' or user_opt.lower() == 'Edit cards':
            safe_sleep_clear(0.1) #Runs safesleepclearr and sleeps for 0.1 seconds
            print('-- Monstars --\n')
            monstersID = input("Enter the monster's ID (enter ? to see all cards + IDs): ").strip()
            if monstersID == "?" or monstersID == "":
                DisplayCards()
                monstersID = input("Enter the monster's ID: ").strip()
            else:
                try:
                    monstersID = int(monstersID)
                except ValueError:
                    print("Invalid input. Enter a number or '?'")
                    monstersID = input("Enter the monster's ID: ").strip()
            connect = sqlite3.connect(DATABASE)
            cursor = connect.cursor()
            cursor.execute("SELECT 1 FROM \"Monster Cards\" WHERE ID = ?", (monstersID,))
            result = cursor.fetchone()
            if result is None:
                DisplayCards()
                print("Please say a monster's ID in the database")
                monstersID = int(input("Enter the monster's ID: "))
            else:
                connect.close()
            stat = input("Which stat do you want to edit? (Strength, Speed, Stealth, Cunning): ").lower()
            if stat not in ["strength", "speed", "stealth", "cunning"]:
                print("Must be within those stats named")
                stat = input("Which stat do you want to edit? (Strength, Speed, Stealth, Cunning): ").lower()
            newvalue = input(f'Enter the new value for "{stat}": ') #Inputs the users input from stat
            newvalue = int(newvalue)
            if 1 <= newvalue <= 20:
                pass
            elif newvalue == "":
                print('Try within 1 and 20')
                newvalue = input(f"Enter the new value for {stat}: ")
            else:
                print('Try within 1 and 20')
                newvalue = input(f"Enter the new value for {stat}: ")
            try:
                newvalue = int(newvalue) #Gets the program to read newvalue as a interger
            except ValueError:
                pass
            EditCards(DATABASE, monstersID, stat, newvalue) #Runs EditCards in INTERNAL_functions

        elif user_opt == '4' or user_opt == 'Remove cards':
            safe_sleep_clear(0.1) #Runs safesleepclearr and sleeps for 0.1 seconds
            print('-- Monstars --\n')
            DisplayCards() #Runs DisplayCards in INTERNAL_functions
            monsterID = int(input('Please enter the ID you would like to remove: '))
            RemoveCards(DATABASE, monsterID) #Runs RemoveCards in INTERNAL_functions
        
        elif user_opt == '5' or user_opt == 'Exit':
            exit()
        
        elif user_opt == '6' or user_opt == 'Evidence':
            configure() #Come on.... test it already


        else:
            main()
main() #Runs the main function
