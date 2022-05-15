############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
from replit import clear
from art2 import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def is_play():
  should_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if should_play == 'y':
    clear()
    return True
  else:
    return False

def cal_score(hand_list):
  if sum(hand_list) == 21 and len(hand_list) == 2:
    return 0

  if 11 in hand_list and sum(hand_list) > 21:
    hand_list.remove(11)
    hand_list.append(1)
  return sum(hand_list)

def another_card():
  if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
    return True
  else:
    return False
def print_player_hand(P_hand, score):
  print(f"Your cards: {P_hand}, current score: {score}")
  
def print_comp_hand(C_hand):
  print(f"Computer's first card: {C_hand[0]}")

def decide_winner(P_scr, C_scr):

  if P_scr > 21 and C_scr > 21:
    print("You went over. You lose 😤")

  if P_scr == C_scr:
    print("Draw 🙃")
  elif P_scr == 0:
    print("Win with a Blackjack 😎")
  elif C_scr == 0:
    print("Lose, opponent has Blackjack 😱")
  elif C_scr > 21:
    print("Opponent went over. You win 😁")
  elif P_scr > 21:
    print("You went over. You lose 😭")
  elif P_scr > C_scr:
    print("You win 😃")
  else:
    print("You lose 😤")

while is_play():
  print(logo)
  Player_hand = [random.choice(cards), random.choice(cards)]
  Computer_hand = [random.choice(cards), random.choice(cards)]
  usr_scr = cal_score(Player_hand)
  print_player_hand(Player_hand, usr_scr)
  print_comp_hand(Computer_hand)
  comp_scr = cal_score(Computer_hand)
  is_another_card = another_card()
  while is_another_card:
    Player_hand.append(random.choice(cards))
    usr_scr = cal_score(Player_hand)
    print_player_hand(Player_hand, usr_scr)
    print_comp_hand(Computer_hand)
    if usr_scr == 0 or comp_scr == 0 or usr_scr > 21:
      is_another_card = False
    else:
      is_another_card = another_card()
  while comp_scr != 0 and sum(Computer_hand) < 17:
    Computer_hand.append(random.choice(cards))
    comp_scr = cal_score(Computer_hand)    
  
  print(f"Your final hand: {Player_hand}, final score: {usr_scr}")
  print(f"Computer's final hand: {Computer_hand}, final score: {comp_scr}")
  decide_winner(usr_scr, comp_scr)
    
