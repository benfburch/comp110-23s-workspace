"""Wordle."""

__author__: str = "730563626"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(searched_str: str, searched_chr: str) -> bool:
    """searches through a string to see if chr is within it"""
    assert len(searched_chr) == 1
    contain_idx: int = 0
    chr_tf: bool = False
    while (len(searched_str) > contain_idx) and chr_tf is False:
        if searched_chr == searched_str[contain_idx]:
            chr_tf = True
        else:
            contain_idx = contain_idx + 1    
    if chr_tf is False:
        return False
    if chr_tf is True:
        return True


def emojified(guess_word: str, secret_word: str) -> str:
    """takes two words and color codes them"""
    assert len(secret_word) == len(guess_word)
    emoji_str: str = ""
    external_idx: int = 0
    while len(secret_word) > external_idx:
        if secret_word[external_idx] == guess_word[external_idx]:
            emoji_str = emoji_str + GREEN_BOX
        if secret_word[external_idx] != guess_word[external_idx]:
            if contains_char(secret_word, guess_word[external_idx]) == True: 
                emoji_str += YELLOW_BOX
            if contains_char(secret_word, guess_word[external_idx])== False: 
                emoji_str += WHITE_BOX    
        external_idx = external_idx + 1
    return emoji_str


def input_guess(expected_len: int) -> str:
    """makes sure guess is right len and returns guess word."""
    guess: str = input(f"Enter a {expected_len} character word: ")
    while expected_len != len(guess): 
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    if len(guess) == expected_len:
        return guess
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    code_word: str = "codes"
    player_guess: str = ""
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")       
        player_guess = input_guess(len(code_word))
        print(emojified(player_guess, code_word))
        if player_guess == code_word:
            print(f"You won in {turns}/6 turns!")
            return None
        else:
            turns += 1
    if turns > 6: 
        print("X/6 - Sorry, try again tomorrow!")
        return None

if __name__ == "__main__":
    main()