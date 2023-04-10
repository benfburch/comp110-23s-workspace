"""Bens Almost Blackjack."""

__author__: str = "730563626"

import random
points: int = 2
player: str = ""
cards: dict[str, int] = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "10": 10, "J": 10, "Q": 10, "K": 10, "a": 1, "A": 11}
SPADE: str = '\U00002660'
HEART: str = '\U00002665'
DIAMOND: str = '\U00002666'
CLUB: str = '\U00002663'
DEALER: str = '\U0001F60F'
PLAYER: str = '\U0001F601'


def greet() -> None: 
    """Greets and gets player name."""
    print(f"{SPADE}{HEART}{DIAMOND}{CLUB} Welcome to Bens Almost Blackjack Game! {SPADE}{HEART}{DIAMOND}{CLUB}")
    print(f"{SPADE}{HEART}{DIAMOND}{CLUB} This game is very similar to traditional black jack, however in this game the Aces are different. {SPADE}{HEART}{DIAMOND}{CLUB}")
    print(f"{SPADE}{HEART}{DIAMOND}{CLUB} In my version you cannot decide what you want the ace to be, it comes predetermined to be either an A (value of 11) or an a (value of 1). {SPADE}{HEART}{DIAMOND}{CLUB}")
    print(f"{SPADE}{HEART}{DIAMOND}{CLUB} Each time you play you bet two points. If you win you get 1.5x your bet :) If you lose, you lose the points :( {SPADE}{HEART}{DIAMOND}{CLUB}")
    global player
    player = input("When you're ready to begin enter your name: ")
    return None 


def learn() -> None:
    """Teaches players how to play and gives them their initial points that they bet with."""
    global points
    global player
    print(f"{SPADE}{HEART}{DIAMOND}{CLUB} Hey {player}, this game is not a complicated one. Heres how it works: {SPADE}{HEART}{DIAMOND}{CLUB}")
    print(f"{SPADE}{HEART}{DIAMOND}{CLUB} Blackjack is a card game played with playing cards. Number cards are worth their inherent values and face cards, with the exception of aces, have a value of 10. The goal of the game is to have a hand value closer to 21 than the dealer's without going over. Players make their initial bets and receive two cards each, while the dealer receives one card face-up and one card face-down. Players can then choose to hit (receive additional cards) or stand (keep their current hand), and the dealer must hit until their hand value is 17 or higher. {SPADE}{HEART}{DIAMOND}{CLUB}")
    exp: str = input(f"{SPADE}{HEART}{DIAMOND}{CLUB} How many years of experience do you have {player}? {SPADE}{HEART}{DIAMOND}{CLUB}"  )
    if int(exp) <= int(4):
        print(f"Looks like you're still a new player {player} so we will start you off with some bonus extra points!")
        points += 28 
    else: 
        print(f"Experienced eh! Heres your points to play {player}:")
        points += 18
    print(f"{SPADE}{HEART}{DIAMOND}{CLUB} {player}'s points: {points} {SPADE}{HEART}{DIAMOND}{CLUB}")
    return None


def dealing_function(deck: dict[str,int]) -> str:
    """Gives random cards from the dict and returns a list."""
    keys: str = ""
    keys = (random.choice(list(deck.keys())))
    return keys
    

def check_22() -> list[str]:
    """Uses dealing_function to make list of cards that doesnt = 22."""
    global cards
    tf: bool = False
    hand: list[str] = list()
    while tf is False: 
        hand += dealing_function(cards)
        hand += dealing_function(cards)
        if cards[hand[0]] + cards[hand[1]] < 22:
            return hand
        if cards[hand[0]] + cards[hand[1]] == 22:
            hand = list()
## take this out


def hit(players_cards: list[str]) -> list[str]:
    """adds an extra card to the players cards."""
    global player
    global cards
    hit_cards: list[str] = players_cards
    hit_cards += dealing_function(cards)
    idx: int = 2
    tf: bool = False
    print(f"Your new card: {hit_cards[idx]}")
    while tf == False:
        player_input: str = input(f"Would you like to hit again {player}? yes/no: ")
        while player_input != 'yes' and player_input != 'no':
            print("Please input \"yes\" or \"no\"")
            player_input: str = input(f"Would you like to hit again {player}? yes/no: ")
        if player_input == "yes": 
            hit_cards += dealing_function(cards)
            idx += 1
            print(f"Your new card: {hit_cards[idx]}")
        if player_input == "no": 
            return hit_cards


def dealer(dealer_cards: list[str]) -> list[str]:
    """Checks whether or not cards are over 17. if not adds cards until it is over 17."""
    global cards
    dealer_value: int = 0
    dealer_hand: list[str] = dealer_cards
    idx: int = 2
    for key in dealer_hand:
        dealer_value += cards[key]
    while dealer_value < 17:
        dealer_hand.append(dealing_function(cards))
        print(f"New dealer hand: {dealer_hand}")
        dealer_value = 0
        for key in dealer_hand:
            dealer_value += cards[key]
    if dealer_value >= 17:
        return dealer_hand


def stand(player_cards: list[str], dealers_cards: list[str]) -> str:
    """Where player stands, card values are compared, dealer gets more cards if needed (if dealer goes over game is over), returns winner."""
    global cards
    global player
    player_value: int = 0
    dealer_value: int = 0
    dealer_hand: list[str] = list()
    winner: str = ""
    #makes sure dealers cards are >17
    dealer_hand = dealer(dealers_cards)
    for specific_card in player_cards:
        player_value += cards[specific_card]
    for specific_card in dealer_hand:
        dealer_value += cards[specific_card]
    #returns winner
    print(f"Dealer cards: {dealer_hand}")
    print("")
    print(f"Player cards: {player_cards}")
    while dealer_value <= 21 and player_value <= 21:
        if dealer_value > player_value:
            winner = "Dealer"
            return winner
        if dealer_value < player_value:
            winner = player
            return winner
    while dealer_value > 21 and player_value > 21:
        winner = "No winner"
        return winner
    if dealer_value > 21 and player_value <= 21:
        winner = player
    if dealer_value <= 21 and player_value > 21:
        winner = "Dealer"
    return winner


def play(play_points: int) -> int: 
    """Takes a bet, enables the game to be played, then returns the number of points based on whether or not they win."""
    global player
    player_cards: list[str] = list()
    dealer_cards: list[str] = list()
    winner: str = ""
    updated_points: int = play_points
    player_input: str = ""
    tf: bool = True
    if points < 2:
        print("Dont forget to learn how to play. Learn to get more points!")
        return 
    #give some information to start game
    #cards get dealt
    player_cards: list[str] = check_22()
    dealer_cards: list[str] = check_22()
    #cards get printed
    print(f"{DEALER} : \"Dealing the cards!\"")
    print("...")
    print(f"{DEALER} DEALERS CARDS: {dealer_cards[0]}")
    print("")
    print(f"{PLAYER} PLAYERS CARDS: {player_cards}")
    #gets to choose whehter to hit or stand
    while tf == True:
        player_input = input(f"would you like to stand or hit? {player}: ")
        if player_input != 'stand' and player_input != 'hit':
            player_input = input(f"would you like to stand or hit? {player}: ")
        if player_input == "hit":
            #run hit function
            player_cards = hit(player_cards)
            print(f"Your updated card list {player}: {player_cards}")
            player_input = ""
                #hits until they want to stop.
        if player_input == "stand":
            #run stand function
            winner = stand(player_cards, dealer_cards)
            #returns winner 
            print("The winner is...")
            print(f"{winner}!!!")
            if winner == player: 
                updated_points += 3
                print("You won! check your points.")
            if winner == "Dealer" or winner == "No winner":
                updated_points -= 2
                print("You lost. :( check your points.")
            return updated_points
        else:
            print("Please input \"stand\" or \"hit\"")
    

def end_game() -> None:
    print(f"Thanks for playing Bens Almost Blackjack Game! See ya next time!")
    print(f"Your points accumulated: {points}")
    return None


def main() -> None: 
    """Main function."""
    global points
    keep_playing: bool = True
    greet()
    #3 options, use input to decide which one to do. 
    while keep_playing == True:
            options: str = input("Would you like to: Play, Learn, or End the game?: ")
            if options == 'End the game':
                end_game()
                return None            
            if options == 'Play':
                points = play(points)
                print(f"Your current points: {points}")
            if options == 'Learn':
                learn()


if __name__ == "__main__":
    main()