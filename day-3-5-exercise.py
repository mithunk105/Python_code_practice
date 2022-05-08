"""
## Love Calculator

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# 💪 This is a Difficult Challenge 💪

# Instructions

You are going to write a program that tests the compatibility between two people.  

To work out the love score between two people:

> Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 


For Love Scores **less than 10** or **greater than 90**, the message should be:

`"Your score is **x**, you go together like coke and mentos."` 

For Love Scores **between 40** and **50**, the message should be:

`"Your score is **y**, you are alright together."`

Otherwise, the message will just be their score. e.g.:

`"Your score is **z**."`

e.g. 

`name1 = "Angela Yu"`

`name2 = "Jack Bauer"`

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

# Example Input 1

```
name1 = "Kanye West"
```

```
name2 = "Kim Kardashian"
```

# Example Output 1

```
Your score is 42, you are alright together.
```

# Example Input 2

```
name1 = "Brad Pitt"
```

```
name2 = "Jennifer Aniston"
```

# Example Output 2

```
Your score is 73.
```

e.g. When you hit **run**, this is what should happen:  

![](https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr)

The testing code will check for print output that is formatted like one of the lines below:
```
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
```

# Hint

1. The `lower()` function changes all the letters in a string to lower case. 

[https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python](https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python)

2. The `count()` function will give you the number of times a letter occurs in a string. 

[https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string](https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string)

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-3-5-test-your-code](https://repl.it/@appbrewery/day-3-5-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 





# Solution

[https://repl.it/@appbrewery/day-3-5-solution](https://repl.it/@appbrewery/day-3-5-solution)
"""
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lwr = name1.lower()
name2_lwr = name2.lower()
cnt = 0
cnt1 = 0
cnt+=name1_lwr.count("t")
cnt+=name1_lwr.count("r")
cnt+=name1_lwr.count("u")
cnt+=name1_lwr.count("e")

cnt+=name2_lwr.count("t")
cnt+=name2_lwr.count("r")
cnt+=name2_lwr.count("u")
cnt+=name2_lwr.count("e")

cnt1+=name1_lwr.count("l")
cnt1+=name1_lwr.count("o")
cnt1+=name1_lwr.count("v")
cnt1+=name1_lwr.count("e")

cnt1+=name2_lwr.count("l")
cnt1+=name2_lwr.count("o")
cnt1+=name2_lwr.count("v")
cnt1+=name2_lwr.count("e")

lv_cal = int(str(cnt)+str(cnt1))

if lv_cal < 10 or lv_cal > 90:
  print(f"Your score is **{lv_cal}**, you go together like coke and mentos.")
elif lv_cal > 40 and lv_cal < 50:
  print(f"Your score is **{lv_cal}**, you are alright together.")
else:
  print(f"Your score is **{lv_cal}**.")