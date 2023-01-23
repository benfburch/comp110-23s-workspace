"""chardle program"""

__author__ = "730563626"


word_target: str = input("Enter a 5-character word: ")

if (len(word_target) != 5):
    print("Error: Word must contain 5 characters.")
    exit()


letter_target: chr = input("Enter a single character: ")

if (len(letter_target) != 1):
    print("Error: Character must be a single character.")
    exit()

instance: int = 0 


print("Searching for " + (letter_target) + " in " + (word_target))


if (word_target[0] == letter_target):
    print(letter_target + " found at index 0")
    instance = (instance) + 1

if (word_target[1] == letter_target):
    print(letter_target + " found at index 1")
    instance = (instance) + 1

if (word_target[2] == letter_target):
    print(letter_target + " found at index 2")
    instance = (instance) + 1

if (word_target[3] == letter_target):
    print(letter_target + " found at index 3")
    instance = (instance) + 1

if (word_target[4] == letter_target):
    print(letter_target + " found at index 4")
    instance = (instance) + 1


if (instance == 0):
    print("No instances of " + letter_target + " found in " + word_target)

if (instance == 1):
    print(str(instance) + " instance of " + letter_target + " found in " + word_target)

if (instance > 1): 
    print(str(instance) + " instances of " + letter_target + " found in " + word_target)