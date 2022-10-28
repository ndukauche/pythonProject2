# import random
# print("welcome to hangman Game")
# word_list = ["ardvack", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# print(chosen_word)
# display = []
# lives = 6
# end_of_game = False
# for n in chosen_word:
#     display.append("_", )
# print(display)
# while not end_of_game:
#     guess = input("guess a letter:?\n").lower()
#     if guess in display:
#          print(f"u have already guessed {guess}")
#     for letter in range(len(chosen_word)):
#         lett = chosen_word[letter]
#         if lett == guess:
#             display[letter] = lett
#     print(display)
#     if guess not in chosen_word:
#         print(f"you guessed {guess}. its not in the word")
#         lives -= 1
#         print("u lost a live")
#     if lives == 0:
#         end_of_game = True
#         print("you loss")
#     if "_" not in display:
#         end_of_game = True
#         print("you win")
# name = input("what is your name?\n")
def greet(name):
    print(f"hello {name}")
    print(f"how do u do   k?")
    print(f"isn't?")

# greet(name)
#
import math
# def paint_calculator():
#     print(f"Area calculator")
#     height = int(input("Height of the wall?\n"))
#     width = int(input("width of the wall?\n"))
#     area = height*width
#     coverage = 5
#     are = math.ceil(area / coverage)
#     print(f"you will need {are} cans of paints")
# paint_calculator()

def prim():
    is_prime = True
    num = int(input("whats the number u want to check?:\n"))
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f"it's a prime number")
    else:
        print(f"it's not prime number")
prim()