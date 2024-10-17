player1 = input("What is Player 1 name:")
player2 = input("what is Player 2 name:")

# Above gets the input of the the first and second player name.
# We keep player info out of loop to not have to re enter it over.

gameChioces1 = """ Player 1:
1. Rock
2. Paper
3. Scissors
Select [1-3]: """

gameChioces2 = """ Player 2:
1. Rock
2. Paper
3. Scissors
Select [1-3]: """


# Above are the choices for the player one and two 




player1Wins = 0
player2Wins = 0
tie = 0

# Above initalizes the current wins for the game session 
# They all reset to zero and are placed out side our while loop to keep reference. 



while True:
    # Above is our while loop that will continuously run the game until we break
    

    
    
    while True: 
        player1Choice = input(gameChioces1)
        if player1Choice not in ["1", "2", "3"]:
            print("Player1: please pick Valid choice")
        else: break
    
  
    
   
    
    while True: 
        player2Choice = input(gameChioces2)
        if player2Choice not in ["1", "2", "3"]:
            print("Player2: please pick Valid choice")
        else: break
        
    # Above, are nested while loops that continues to prompt the user until a correct choice is made 
    
    match player1Choice:
        case "1":
            player1Choice = "Rock"
            print(f"Player One is {player1Choice}")
        case "2":
            player1Choice = "Paper"
            print(f"Player One is {player1Choice}")
        case "3":
            player1Choice = "Scissors"
            print(f"Player One is {player1Choice}")
        case _:
         print("Select [1-3]:")
        
        
    match player2Choice:
        case "1":
            player2Choice = "Rock"
            print(f"Player Two is {player2Choice}")
        case "2":
            player2Choice = "Paper"
            print(f"Player Two is {player2Choice}")
        case "3":
            player2Choice = "Scissors"
            print(f"Player Two is {player2Choice}")
        case _:
         print("Select [1-3]:")
         
         
    # Above are match statments that transform the players choice to either Rock, Paper, or Scissors
         
         
   
    
    if player1Choice == "Rock" and player2Choice == "Paper":
        print("Player 2 Wins")
        player2Wins = player2Wins + 1
        
    elif player1Choice == "Rock" and player2Choice == "Scissors":
        print("Player 1 Wins")
        player1Wins = player1Wins + 1
        
    elif player1Choice == "Paper" and player2Choice == "Rock":
        print("Player 1 Wins")
        player1Wins = player1Wins + 1
        
    elif player1Choice == "Paper" and player2Choice == "Scissors":
        print("Player 2 Wins")
        player2Wins = player2Wins + 1
        
    elif player1Choice == "Scissors" and player2Choice == "Paper":
        print("Player 1 Wins")
        player1Wins = player1Wins + 1
        
    elif player1Choice == "Scissors" and player2Choice == "Rock":
        print("Player 2 Wins")
        player2Wins = player2Wins + 1
        
    elif player1Choice == player2Choice:
        print("Its a tie :) !")
        tie = tie + 1
    
    else: print(" thanks for playing")
    
    # Above is our game functionality
    # The if statment identifies each possible way to win and the result after. 
    
    
    
   
    
    playAgain = input("would you like to play again? [yes or no]")
    
    # Above prompts the Players to play again 
    
    
    
    if playAgain == "no":
        print(f"""
        {player1} has: {player1Wins} wins   
        {player2} has: {player2Wins} wins
        There were {tie} ties """) 
        break
        
    # Above breaks out of our current while loop only if the answer "no".
    # Before it breaks it lists the total scores for each player or ties.
    
        
    
    
    
         
         
         
         
        
  
    
    