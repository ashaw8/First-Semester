import random
#Authors: Aidan Shawyer + Zhen Yu
# ASCII art Sourced from github user wynand1004 
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def printMove(move):
    if move == 'rock' :
        return rock 
    if move == 'paper':
        return paper 
    if move == 'scissors':
        return scissors 

def makePlayerMove(playerMove):         #player input to assoaciated picked moved to animated art
   # print("Please enter your name")
   # playerName = input()
    print("Please enter your move rock, paper, or scissors")
    playerMove =  input()
    print("Picked:", playerMove, printMove(playerMove))
   # playerArt = printMove(playerMove) 
    return playerMove

# The following function takes in the computerName as a parameter. 
# The function will return the computerMove as a string

def makeComputerMove(computerName):
        num = random.randint(1,3) #generating the random integer
        computerMove = ""
        if (num == 1):
                computerMove = "rock" #assigning 1 to the move, rock
        elif (num == 2):
                computerMove = "paper" #assigning 2 to the move, paper
        else:
                computerMove = "scissors" #assigning 3 to the move, scissors
        computerArt = printMove(computerMove) #printMove function is called and the computerMove (rock,paper, scissors) is input, and assigned to computerArt function
        print(computerArt) #the corresponding art for the computerMove is printed 
        return computerMove
        
def checkRoundWinner(playerMove, computerMove):  #evaulates player move vs computer move to determin who run the individual round. 
        result = ""
        if (playerMove == "rock"): 
                if (computerMove == "paper"):
                    result = "Computer Won"
                    return result
                elif (computerMove == "scissors"):
                    result = "Player Won"
                    return result
                else:
                    result = "Tie"
                    return result
        elif (playerMove == "paper"): 
                if (computerMove == "rock"):
                        result = "Player Won"
                        return result
                elif (computerMove == "scissors"):
                        result = "Computer Won"
                        return result
                else:
                        result = "Tie"
                        return result
        elif (playerMove == "scissors"): 
                if (computerMove == "rock"):
                        result = "Computer Won"
                        return result
                elif (computerMove == "paper"):
                        result = "Player Won"
                        return result
                else:
                        result = "Tie" 
                        return result
# Return statement(s)

def main():
    playerName = input("Enter Name of player: ")
    computerName = input("Enter Name of computer: ")
    playerWins = 0
    computerWins = 0
    playerMove = str 
    computerMove = str

##iteration to determine if the match has ended, 2 out of three 
    while True: 
        playerMove = makePlayerMove(playerMove)
        computerMove = makeComputerMove(computerMove)

        roundWinner = checkRoundWinner(playerMove, computerMove)
        if roundWinner == "Player Won":
            print(playerName, "won the round!")
            playerWins += 1
       
        elif roundWinner == "Computer Won":
            print(computerName, "wins the round!")
            computerWins += 1
        
        else:
            print("It was a tie!")
            
        if playerWins == 2:
            print(playerName, "won the match!")
            break

        if computerWins == 2:
            print(computerName, "won the match!")
            break
    return 
        



main()
