"""One shot worlde."""

__author__: str = "730563626"

secret_word: str = ("python")
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
index_number: int = 0
emoji_string: str = ""
alt_index: int = 0
true_false: bool = False 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")


while index_number < len(secret_word):
    if secret_word[index_number] == guess_word[index_number]:
        emoji_string = emoji_string + GREEN_BOX
    if secret_word[index_number] != guess_word[index_number]:
        while true_false is False and alt_index < len(secret_word):
            if guess_word[index_number] == secret_word[alt_index]:
                true_false = True
            else: 
                alt_index = alt_index + 1
   
    if true_false is True and secret_word[index_number] != guess_word[index_number]:
        emoji_string = emoji_string + YELLOW_BOX
       
    if true_false is False and secret_word[index_number] != guess_word[index_number]:     
        emoji_string = emoji_string + WHITE_BOX
        
    index_number = index_number + 1
    true_false = False
    alt_index = 0


print(emoji_string)

if guess_word != secret_word:
    print("Not quite. Play again soon!")

if guess_word == secret_word:
    print("Woo! You got it!")