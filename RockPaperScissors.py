import random
from getpass import getpass as input

class RockPaperScissors:
    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.computer = 0
        self.choices = ["Rock", "Paper", "Scissors"]
        
        print("Rock Paper Scissors") 
        
        print("\nChoose a gameplay")
        print("\n1. Player VS Player")
        print("2. Player VS Computer")
        
        choice_game = int(input("\nWhat would you choose to play? "))
        game_rounds = int(input("How many rounds do you want to play? "))
        
        if choice_game == 1:
            while self.player1 < game_rounds and self.player2 < game_rounds:
                print("\nPlayer 1 Turns")
                player1 = str(input("Rock Paper Scissors => "))
                print("\nPlayer 2 Turns")
                player2 = str(input("Rock Paper Scissors => "))
                
                if player1 == player2:
                    print("\nIt's a tie")
                elif player1 == "Q" or  player1 == "q" and  player2 == "Q" or player2 == "q":
                    print("\nThank you for playing")
                    break
                elif player1 == "Rock" or player1 == "rock":
                    if player1 == "Paper" or player2 == "paper":
                        print("\nPlayer 2 Wins")
                        print("\nYou lose", player2, "crumbled", player1)
                        self.player2 += 1
                        print("\nScores")
                        print(self.player1, "VS", self.player2)
                    elif player2 == "Scissors" or player2 == "scissors":
                        print("\nPlayer 1 Wins")
                        print("\nYou win", player1, "smashed", player2)
                        self.player1 += 1
                        print("\nScores")
                        print(self.player1, "VS", self.player2)
                elif player1 == "Paper" or player1 == "paper":
                    if player2 == "Scissors" or player2 == "scissors":
                        print("\nPlayer 2 Wins")
                        print("You lose", player2, "cuts", player1)
                        self.player2 += 1
                        print("\nScores")
                        print(self.player1, "VS", self.player2)
                    elif player2 == "Rock" or player2 == "rock":
                        print("\nPlayer 1 Wins\n")
                        print("You win", player1, "crumbled", player2)
                        self.player1 += 1
                        print("Scores\n")
                        print(self.player1, "VS", self.player2)
                elif player1 == "Scissors" or player1 == "scissors":
                    if player2 == "Rock" or player2 == "rock":
                        print("\nPlayer 2 Wins")
                        print("You lose", player2, "smashed", player1)
                        self.player2 += 1
                        print("\nScores")
                        print(self.player1, "VS", self.player2)
                    elif player2 == "Paper" or player2 == "paper":
                        print("\nPlayer 1 Wins")
                        print("You win", player1, "cuts", player2)
                        self.player1 += 1
                        print("\nScores")
                        print(self.player1, "VS", self.player2)
                else:
                    print("Incorrect choices")
        elif choice_game == 2:
            while self.player1 < game_rounds and self.computer < game_rounds:
                random_choose = self.choices[random.randint(0, 2)]
                
                if random_choose== 0:
                    random_choose= "Rock"
                elif random_choose == 1:
                    random_choose= "Paper"
                elif random_choose == 2:
                    random_choose= "Scissors"
                
                print("\nPlayer 1 Turn")
                player= str(input("\nRock Paper Scissors => "))
                
                if player == random_choose:
                    print("\nIt's a Tie")
                elif player ==  "Q" or  player == "q":
                    print("Thank you for playing")
                    break
                elif player == "Rock":
                    if random_choose == "Paper":
                        print("\nComputer Wins")
                        print("\nYou lose", random_choose, "crumbled", player)
                        self.computer += 1
                        print("\nScores")
                        print(self.player1, "VS", self.computer)
                    elif random_choose == "Scissors":
                        print("\nPlayer 1 Wins")
                        print("\nYou win", player, "smashed", random_choose)
                        self.player1 += 1
                        print("\nScores")
                        print(self.player1, "VS", self.computer)
                elif player == "Paper":
                    if random_choose == "Scissors":
                        print("\nComputer Wins")
                        print("\nYou lose", random_choose, "cuts", player)
                        self.computer += 1
                        print("\nScores")
                        print(self.player1, "VS", self.computer)
                    elif random_choose == "Rock":
                        print("\nPlayer 1 Wins")
                        print("\nYou win", player, "crumbled", random_choose)
                        self.player1 += 1
                        print("\nScores\n")
                        print(self.player1,"VS", self.computer)             
                elif player == "Scissors":          
                        if random_choose == "Rock":
                            print("\nComputer Wins")
                            print("\nYou lose", random_choose, "smashed", player)
                            self.computer += 1
                            print("\nScores")
                            print(self.player1, "VS", self.computer)
                        elif random_choose == "Paper":
                            print("\nPlayer 1 Wins")
                            print("\nYou win", player, "cuts", random_choose)
                            self.player1 += 1
                            print("\nScores")
                            print(self.player1, "VS", self.computer)   
                else:
                    print("\nIncorrect choices")    
        else:
            print("\nWrong gameplay selected")
            
class Main:
    def __init__(self):
        RockPaperScissors()

if __name__ == "__main__":
    Main()