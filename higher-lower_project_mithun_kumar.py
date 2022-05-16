from replit import clear
import art4
from random import choice
import game_data
print(art.logo)
B_list = choice(game_data.data)
cont_on_good_ans = True
score = 0
while cont_on_good_ans:
  A_list = B_list
  print(f"Compare A: {A_list['name']}, a {A_list['description']}, from {A_list['country']}.")
  print(art.vs)
  B_list = choice(game_data.data)
  if A_list == B_list:
    B_list = choice(game_data.data)
  print(f"Against B: {B_list['name']}, a {B_list['description']}, from {B_list['country']}.")
  user_ans = input("Who has more followers? Type 'A' or 'B': ")
  actual_ans = ""
  if A_list['follower_count'] > B_list['follower_count']:
    actual_ans = "A"
  else:
    actual_ans = "B"
  if user_ans == actual_ans:
    cont_on_good_ans = True
    score += 1
    clear()
    print(art.logo)
    print(f"You're right! Current score: {score}")
  else:
    cont_on_good_ans = False
  

print(f"Sorry, that's wrong. Final score: {score}")