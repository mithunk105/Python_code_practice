"""
## FizzBuzz

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

You are going to write a program that automatically prints the solution to the FizzBuzz game. 

> `Your program should print each number from 1 to 100 in turn.` 

>   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".` 

>     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

>       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

e.g. it might start off like this:

```
`1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz`
```

`.... etc.`

# Hint

1. Remember your answer should start from 1 and go up to and including 100. 

2. Each number/text should be printed on a separate line.

# Solution

[https://repl.it/@appbrewery/day-5-4-solution](https://repl.it/@appbrewery/day-5-4-solution)

Alternatively: [https://en.wikipedia.org/wiki/Fizz_buzz](https://en.wikipedia.org/wiki/Fizz_buzz)

"""
#Write your code below this row 👇
for n in range(1, 101):
    if n % 3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n%5 == 0:
        print("Buzz")
    elif n%3 ==0:
        print("Fizz")
    else:
        print(n)
