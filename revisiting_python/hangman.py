
import random

# create a greeting
print("Welcome to our game")
# create your world list
words = ["hacker","county","random","equity","split"]
# randomly chose a word from the list you have created
secret_word = random.choice(words)
# ask the user to guess a letter
# make the program take input from the user and make it lowercase
guess = input("Guess a letter: ").lower()
print(guess)
# check if the letter is in the word
for letter in secret_word:
  if letter == guess:
    print("Correct!")
  else:
    print("wrong")