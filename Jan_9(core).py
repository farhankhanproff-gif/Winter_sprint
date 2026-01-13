import random

class RPSGame:
#-----------initialize player score-----------
    def __init__(self,  player_score=0, computer_score=0):
        
        self.player_score = player_score
        self.computer_score = computer_score
#---------------User inputs name and number of rounds------------
    def round(self):
            player_name = input("Enter player name: ")
            num_rounds = int(input("Enter number of rounds you want to play: "))
            for num in range(num_rounds):

             player_choice = input("Enter your move (rock/paper/scissors): ").lower().strip()
             choices = ['rock', 'paper', 'scissors']
             computer_choice = random.choice(choices)
             print(f"Computer chose: {computer_choice}")

#-------------------Game logic---------------

             if player_choice == 'rock' and computer_choice == 'scissors':
                self.player_score+=1
                result = "You win"
             elif player_choice =='rock' and computer_choice == 'paper':
                self.computer_score+=1
                result = "You lose"
             elif player_choice =='scissors' and computer_choice == 'paper':
                self.player_score+=1
                result = "You win"
             elif player_choice =='scissors' and computer_choice == 'rock':
                self.computer_score+=1
                result = "You lose"
             elif player_choice =='paper' and computer_choice == 'rock':
                self.player_score+=1
                result = "You win"
             elif player_choice =='paper' and computer_choice == 'scissors':
                self.computer_score+=1
                result = "You lose"
             else:
                result = "Draw"
                pass
             
             
             print(f"Result: {result}")
#-------------shows score------------------
             def scoreboard():
               print("-" * 30 + "SCOREBOARD" + "-" * 30)
               print(f"{player_name} : {self.player_score}")
               print(f"Computer : {self.computer_score}")
            
            scoreboard()
             

#------------------Class and method call--------------------   

Game = RPSGame()
Game.round()
      







            

        
