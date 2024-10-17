

player1Wins = 0
player2Wins = 0
tie = 0




def getNames():
    
    """
    Asks a player for their Name 

    This function asks a player for a valid name entry via a input.

    Parameters:
    none

    Returns:
    The Players name 

    Raises:
    loops: If the input string is empty.
    """
    
    
    playerName = input("What is Player name:")
    while not playerName:
        print("Please enter a  Valid player Name:")
        playerName = input("What is Player name:")
    return playerName

def gameChoice(playerName):
    
    """
    Asks a player for their Name 

    This function asks a player for a valid choice entry via a input.

    Parameters:
    (str) : The player name whose turn it is to choose.

    Returns:
    The Players Choice 

    Raises:
    loops: If the input string is not equal to "1", "2", or  "3" .
    """
    
    
    
    playerChoice = None
    
    gameChioces = f""" {playerName} please choose one below:
        1. Rock
        2. Paper
        3. Scissors
        Select [1-3]: """
        
    while True: 
        playerChoice = input(gameChioces)
        if playerChoice not in ["1", "2", "3"]:
            print("Player1: please pick Valid choice")
        else: break
    
    return playerChoice


def matchPlayerChoice(playerChoice, playerName):
    
    """
    Matches a players choice to Rock, Paper or Scissor

    This function asks a player for a valid choice entry via a input.

    Parameters:
    (str) : A players choice equal to "1", "2", or  "3"
    (str) : A players name to recognize the player with their chioce.

    Returns:
    The Players Choice converted to Rock, Paper or Scissor

    Raises:
    default : To "Select [1-3]:"
    """
    
    
    
    
    match playerChoice:
        case "1":
            playerChoice = "Rock"
            print(f"{playerName} chose {playerChoice}")
            return playerChoice
        case "2":
            playerChoice = "Paper"
            print(f"{playerName} chose {playerChoice}")
            return playerChoice
        case "3":
            playerChoice = "Scissors"
            print(f"{playerName} chose {playerChoice}")
            return playerChoice
        case _:
         print("Select [1-3]:")
    

def winnerOfGame(playerName1,playerName2, playerOneChoice, playerTwoChoice):
    
    """
    Determines who wins Rock, Paper or Scissor game

    This function checks the input of both players and makes a decison on who wins the game.
    The Winners score is incremented 

    Parameters:
    (str) : A players name.
    (str) : A players name.
    (str) : A players choice equal to Rock, Paper or Scissor
    (str) : A players choice equal to Rock, Paper or Scissor

    Returns:
    non

    Raises:
    default : To "thanks for playing"
    """
    
    
    
    
    
    global player2Wins
    global player1Wins
    global tie 
    
    

    
    if playerOneChoice == "Rock" and playerTwoChoice == "Paper":
        print(f"{playerName2} Wins")
        player2Wins = player2Wins + 1
        
    elif playerOneChoice == "Rock" and playerTwoChoice == "Scissors":
        print(f"{playerName1} Wins")
        player1Wins = player1Wins + 1
        
    elif playerOneChoice == "Paper" and playerTwoChoice == "Rock":
        print(f"{playerName1} Wins")
        player1Wins = player1Wins + 1
        
    elif playerOneChoice == "Paper" and playerTwoChoice == "Scissors":
        print(f"{playerName2} Wins")
        player2Wins = player2Wins + 1
        
    elif playerOneChoice == "Scissors" and playerTwoChoice == "Paper":
        print(f"{playerName1} Wins")
        player1Wins = player1Wins + 1
        
    elif playerOneChoice == "Scissors" and playerTwoChoice == "Rock":
        print(f"{playerName2} Wins")
        player2Wins = player2Wins + 1
        
    elif playerOneChoice == playerTwoChoice:
        print("Its a tie :) !")
        tie = tie + 1
    
    else: print(" thanks for playing")


def app():
    
    
     
    """
    Starts and finishes the entire Rock, Paper or Scissor

    This function 
    1. uses getNames() to get each player name.
    2. gameChoice(playerName) to get each players choice.
    3. matchPlayerChoice(playerChoice, playerName) to match the player choice to Rock, Paper or Scissor.
    4. winnerOfGame(playerName1,playerName2, playerOneChoice, playerTwoChoice) to determine the winner and increment their score.
    5. Prompts to continue playing or end the current gme and display the current scores. 
    
    

    Parameters:
    none

    Returns:
    none

    Raises:
    default : To "thanks for playing"
    """
    
    
    print( "Welcome to Rock, Paper or Scissor.")
    
    playerOneName = getNames()
    playerTwoName = getNames()
    

    
    
    while True:
        
        
        
        
        playerOneNumber = gameChoice(playerOneName)
        playerOneChoice = matchPlayerChoice(playerOneNumber,playerOneName)
        
        playerTwoNumber = gameChoice(playerTwoName)
        playerTwoChoice = matchPlayerChoice(playerTwoNumber,playerTwoName)
        
        winnerOfGame(playerOneName,playerTwoName,playerOneChoice,playerTwoChoice)
        
        playAgain = input("would you like to play again? [yes or no]")
    
        # Above prompts the Players to play again 
    
        if playAgain == "no":
            print(f"""
            {playerOneName} has: {player1Wins} wins   
            {playerTwoName} has: {player2Wins} wins
            There were {tie} ties """) 
            break
        # Above breaks out of our current while loop only if the answer "no".
        # Before it breaks it lists the total scores for each player or ties.
        
        
app()