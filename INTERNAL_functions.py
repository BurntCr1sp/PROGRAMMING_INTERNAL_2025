import sqlite3 #Imports "sqlite3" giving us the ability to access and change our database

DATABASE = 'DataBase.db' #Defines what I mean by "DATABASE"

def DisplayCards():
    with sqlite3.connect(DATABASE) as connection: #Connects the function with the database
        cursor = connection.cursor() #Creates a cursor
        #Tells the curcor what to get from the database. In this case everything
        select_query = """
        SELECT
            *
        FROM 'Monster Cards'
        """
        cursor.execute(select_query) #Tells the cursor to do "select_query"
        cards = cursor.fetchall()
        
        #Formating the data that the cursor has got from the database
        print('')
        print('                         〰〰 CARDS 〰〰')
        print('╭────┬────────────────┬──────────┬─────────┬───────────┬─────────╮')
        print('│ ID │ Name           │ Strength │  Speed  │  Stealth  │ Cunning │')
        print('├────┼────────────────┼──────────┼─────────┼───────────┼─────────┤')
        for card in cards:
            print(f"│{card[0]:<4}│{card[1]:<16}│{card[2]:<10}│{card[3]:<9}│{card[4]:<11}│{card[5]:<9}│")
        print('╰────┴────────────────┴──────────┴─────────┴───────────┴─────────╯')
        #The ":<4" command tells the code to have 4 characters avalible for use (adds white space in unused characters)

def EditCards(DATABASE, monstersID, stat, newvalue):
    stats = {"strength", "speed", "stealth", "cunning"} #Defines what I mean by "stats"

    if stat not in stats: #Gives user a error message and returns
        print('Not a valid stat, please try again')
        return
    
    try:
        connect = sqlite3.connect(DATABASE) #Connects the function with the database
        cursor = connect.cursor() #Creates a cursor

        change = f"UPDATE 'Monster Cards' SET {stat} = ? WHERE ID = ?"
        cursor.execute(change, (newvalue, monstersID)) #Changes the database like a .pop or .append
        question = input('Would you like to commit this? (y/n) ').lower()
        if question == 'y':
            connect.commit() #Commits all changes made to the database
            print('All changes have been commited')
        else:
            connect.rollback() #Disregards all changes made from after the previous commit till now
            print('All changes have been rolled back, nothing commited')

    finally:
        connect.close() #Stops the connection with the database

def AddCards(DATABASE, name, strength, speed, stealth, cunning):
    try:
        connect = sqlite3.connect(DATABASE) #Connects the function with the database
        cursor = connect.cursor()#Creates a cursor
        print("Attempting to insert:", name, strength, speed, stealth, cunning)
        cursor.execute(
            "INSERT INTO \"Monster Cards\" (name, strength, speed, stealth, cunning) VALUES (?, ?, ?, ?, ?)", 
            (name, strength, speed, stealth, cunning)
        )
        connect.commit() #Commits all changes made to the database
        return "Card added successfully."
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        if connect:
            connect.close() #Stops the connection with the database

def RemoveCards(DATABASE, monsterID):
    while True:
        sure = input('Are you sure you want to remove this card? (y/n): ').strip().lower()
        if sure == 'y':
            try:
                connect = sqlite3.connect(DATABASE) #Connects the function with the database
                cursor = connect.cursor()#Creates a cursor
                cursor.execute("DELETE FROM \"Monster Cards\" WHERE ID = ?", (monsterID,))
                connect.commit() #Commits all changes made to the database
                print("Card successfully removed")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
            finally:
                connect.close() #Stops the connection with the database
            break #Breaks from the loop
        elif sure == 'n':
            print("Operation cancelled")
            break #Breaks from the loop
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

