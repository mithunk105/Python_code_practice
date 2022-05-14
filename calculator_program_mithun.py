from replit import clear
def add(first, second):
  return first + second
def sub(first, second):
  return first - second
def mul(first, second):
  return first * second
def div(first, second):
  return first / second
operation_list = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
}
def display(oper):
  for sym in oper:
    print(sym)

from art1 import logo
def calculator():
  clear()
  print(logo)
  first_num = float(input("What's the first number?: "))
  display(operation_list)
  choose = True
  result = 0.0
  while choose == True:
    pick_oper = input("Pick an operation: ")
    next_num = float(input("What's the next number?: "))
    result = operation_list[pick_oper](first_num, next_num)
    print(f"{first_num} {pick_oper} {next_num} = {result}")
    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: \n") == "y":
      first_num = result
    else:
      choose = False
  clear()
  calculator()

calculator()