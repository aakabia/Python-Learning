# Menu for UI
# Get user input
# Add a plate
# Plate at the bottom must be the same size or larger than plates at top
# Larger plates are first in list
# If plate input < or = 0 do not add
# Display plates
# If no plates display message
# Remove plates from top of stack (End of list)
# Remove value should be positive
# If remove input greater than amount of plates reject
# Exit

plates =[]


def pickFromMenu():
    """
    Asks a user what task they would like to perform.

    This function presents the user with a set of options and asks for input 
    corresponding to the desired task. It ensures that the user provides 
    a valid choice from the menu options.

    Parameters:
    none

    Returns:
    str: The user's choice as a string, representing the selected task.

    Raises:
    loops: If the input string is not equal to  "0" "1", "2", or  "3" .
    """

    userChoice = None

    choices = f""" 
        Menu
        ================
        0. [Exit]       
        1. Add a plate  
        2. Print plates 
        3. Remove plates
        Select [0-3]: """

    while True:
        userChoice = input(choices)
        if userChoice not in [ "0","1", "2", "3"]:
            print("Please pick Valid choice!")
        else:
            break

    return userChoice




def addPlate():
    
    """
    Add a plate to plates list.

    This function asks a user for a plate size and adds it to the plates list.
    It only adds the plate if the chosen plate size is a postive number greater than 0
    and if it is less than the last index in the lists array.

    Parameters:
    none

    Returns:
    none

    Raises:
    Success: A log statement will indicate that the plate has been successfully added.
    Error:  An error will be raised for non-positive numbers or sizes greater than the last index of the plates list.
    """
    
    
    while True:
        plateSize = input("What size is this plate?:")
        
        if not plateSize.isdigit() or int(plateSize) <= 0:
            print("Please pick a positive number greater than 0.")
        else:
            intPlateSize = int(plateSize)
            break  
    
    

    
    if len(plates) == 0:
        plates.append(intPlateSize)
        print(f"Added first plate with size of {intPlateSize} to the stack!")
        return
    elif intPlateSize > plates[-1]:
        print(f"Cannot place a plate of size {intPlateSize} on top of another plate of size {plates[-1]}!")
        return
    else: plates.append(intPlateSize)
    
    print(f"Success plate of size {intPlateSize} added to top of stack!")
    
    return
    
    

def displayPlates():
    
    
    """
    Display plates to the user.

    This function sorts the plates array and displays all the plates to the user in a formatted manner.

    Parameters:
    none

    Returns:
    none

    Raises:
    Error: If the plates list is empty, the message "There are no stacked plates" will be printed.
    """
    
    
    
    if len(plates) == 0:
        print("""
            Print plates
            ============
            There are no stacked plates.""")
        return
    
    
    plateSymbol = "#"
    
    
    sortedPlates = sorted(plates)
    # Above, I use the sorted() instead of sort() method because it returns a new sorted list without modifying the original list.
    
     
    console_width = 35
    # Above I deterimine a console width
    
    
    print("""
            Print plates
            ============""")
    
    
    
    for index, plate in enumerate(sortedPlates):
        plateFigure = f"{plate}. { plateSymbol * plate}"
        
        centeredPlate = plateFigure.center(console_width)
        #Above, I use .center to help center my platfigure under " Print Plates" in the terminal.
        # center() is a string method that centers the text within the specified width
        
        print(centeredPlate)
    
    return 
    
        



def removePlates():
    
    """
    Removes a specific amount of plates from the plates list.

    This function prompts the user for the number of plates to remove,
    validates the input, and removes the specified number of plates 
    from the end of the plates list.

    Parameters:
    none

    Returns:
    none

    Raises:
    Error: If the requested number of plates to remove exceeds the length of the plates list.
    """
    
    
    if len(plates) == 0:
        print("Currently, there are no plates to remove!")
        return
    
    
    
    while True:
        amountToRemove = input("How many plates would you like to remove?:")
        
        if not amountToRemove.isdigit() or int(amountToRemove) <= 0:
            print("Please pick a positive number greater than 0.")
        else:
            intAmountToRemove = int(amountToRemove)
            break   
    
    
    if intAmountToRemove > len(plates):
        print(f"Cannot remove more than {len(plates)} plates. You chose {intAmountToRemove}.")
        return
        

    del plates[-intAmountToRemove:]
    # Above, I use a negative integer in the delete statement to remove multiple items from the end of the list.
    
    print(f"Successfully removed {intAmountToRemove} plates from the top of stack.")
    
    return 
    













def app():
    
    
      
    """
    Functionality for our stack plates app.

    1. Utilizing a variable (option) to capture user input effectively.
    2. Employing a while loop to ensure the application runs continuously until the user opts to exit.
    3. Implementing a match statement to invoke the corresponding function based on the user's selection.

    Parameters:
    none

    Returns:
    none

    Raises:
    loops: Will continue to loop until variable "option" equals  "0".
    """
    
    

    
    print(" Welcome Friend! What would you like to do today? ")
    
    
    option = None 
    
    while option != "0":
     
        option = pickFromMenu()
        
        match option:
            case "1":
                addPlate()
            case "2":
                displayPlates()    
            case "3":   
                removePlates()
            case _:
                print("Select [0-3]:")
    
    
    return
    


if __name__ == "__main__":
    app()
    
    
# The above if statment use a special built-in variable in Python "__name__". 
# The statment ensures that our script can only be run directly and not when imported.
   
    