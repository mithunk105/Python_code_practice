from replit import clear
#HINT: You can call clear() to clear the output in the console.

bidder_list = {}
def accept_name_bid():
  name = input("What's your name?: ")
  bidder_list[name] = int(input("What's your bid?: $"))
def find_highest_bidder():
  usr = ""
  max = 0
  for user in bidder_list:
    if bidder_list[user] > max:
      usr = user
      max = bidder_list[user]

  print(f"The winner is {usr} with a bid of ${max}")

from art import logo
print(logo)
print("Welcome to the secret auction program.")
is_user_bid = True
while is_user_bid == True:
  accept_name_bid()
  user_input = input("Are there any other bidder, Type 'yes' or 'no'\n")
  if user_input == "no":
    is_user_bid = False
  clear()

find_highest_bidder()