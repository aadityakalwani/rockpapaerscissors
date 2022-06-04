import random

def play():
  player_turn = (input("Enter the move you want to make\ntype 'r' for rock, 'p' for paper and 's' for scissors:\n"))
  computer_turn = random.choice(['r', 'p', 's'])
  print(f"the computer chose {computer_turn}")

  if player_turn == computer_turn:
    return "draw"

def is_win(player, opponent):
  
    
# while loop that says 'while game is not won'

play()