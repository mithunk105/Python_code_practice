#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def choose_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5
  else:
    print("Only type 'easy' and 'hard' to continue!")
    return choose_difficulty()
  
from art3 import logo
import random
real_num = random.randint(1, 100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
num_attempt = choose_difficulty()
print(f"You have {num_attempt} attempts remaining to guess the number")
guess_num = int(input("Make a guess: "))
while num_attempt > 1:
  if guess_num < real_num:
    print("Too low.\nGuess again.")
    num_attempt -= 1
  elif guess_num > real_num:
    print("Too high.\nGuess again.")
    num_attempt -= 1
  else:
    break
  print(f"You have {num_attempt} attempts remaining to guess the number")
  guess_num = int(input("Make a guess: "))

if guess_num == real_num:
  print(f"You got it! The answer was {guess_num}")
else:
  print("You've run out of guesses. You lose.")