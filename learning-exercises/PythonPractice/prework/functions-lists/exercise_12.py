favorites = []

# 1. Copy your read_required_string function
# into this file.


def read_required_string(str):
    value = input(str)
    while not value.strip():
        print("Error String is empty")
        value = input(str)

    return value


# Above is our required string function that prompts for user input
# function does not stop until user input is a valid string.


# 2. Define a function that uses read_required_string
# to add a favorite (food, books, music, color, animals, whatever...)
# to the `favorites` list.


def addToFavorites(medium):
    value = read_required_string(medium)
    favorites.append(value)


# Above, we pass our read_required_string to addToFavorites
# addToFavorites has one param , get a value from read_required_string and appends it to our favorites list


# 3. Define a function that prints `favorites` to the terminal.


def printFav():
    print(favorites)


# Above, printFav prints our list


# 4. Define a function that removes 1 to n `favorites`
# from the end of the list.
# If the argument is larger than the list length, display an error message.
# Otherwise, remove n items from the end of the list.


def remove_favorites(int1, list):

    int1 = int(int1)  # convert int to actual int

    if int1 > len(list):
        print("Error not enough items in list")
        return

    del list[
        -int1:
    ]  # del and - allow for backward deletion in lists, pop just deletes a specified index.
    print(f"Removed {int1} items from the list.")


# remove_favorites takes two params a int and a list
# it checks if the int is greater than the length of the list
# if it is greater it results in a error
# if it is smaller it deltes from the end of the list.


# 5. Define a function that displays a menu:
# ==============
# Menu
# 1. Add Favorite
# 2. Print Favorites
# 3. Remove Favorites
# 4. Exit
# Select [1-4]:
# ==============
# Use menu decisions to execute functions.
# Exit terminates the program.


def app():
    while True:
        # Above is  a while loop to continue running the app fucntion until broken or returned.

        menu = """
            1. Add Favorite
            2. Print Favorites
            3. Remove Favorites
            4. Exit
            Select [1-4]: """

        # Above, initializes the menu

        while True:
            selection = input(menu)
            if selection not in ["1", "2", "3", "4"]:
                print(" Selection: please pick Valid choice")
            else:
                break

        # Above makes sure that the user input is either "1", "2", "3","4"

        match selection:
            case "1":
                toAdd = "What would you like to add?"

                addToFavorites(toAdd)
                print(f" Added to favorites!")
                
            # case 1 string toAdd is sent to addToFavorites fo execution
            # Print statment at end for verification

            case "2":
                printFav()
                
            # case 2 prints our list

            case "3":
                toRemove = input("How many would you like to remove?")
                
                # toRemove gets input on how many to remove

                while not toRemove.strip():
                    print("Error String is empty")
                    toRemove = input("What would you like to add?")
                    
                # Above checks for empty string

                while not toRemove.isnumeric():
                    print("Error: Please enter a valid number")
                    toRemove = input("How many would you like to remove? ")
                
                # Above checks for numeric value 

                remove_favorites(toRemove, favorites)
                
                # Above calls remove_favorites with toRemove and favorites as arguments

            case "4":
                print("Thank you")
                return
            
            # Above, prints thank you and escapes our loop and app function 

            case _:
                print("Select [1-4]:")
            # Above is the default match
        # Above is our match statment that is responisbile for the functionality of our app.


app()

# Above we call app to run function 
