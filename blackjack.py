from art import logo
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    user_hand = random.sample(cards, 2)
    dealer_hand = random.sample(cards, 2)
    print(f"""
    Your hand: {user_hand}
    Dealer first card: {dealer_hand[0]} """)
    hands = [user_hand, dealer_hand]
    return hands
    

def calculate_score(user_hand, dealer_hand):
    user_score = sum(user_hand)
    dealer_score = sum(dealer_hand)
    if user_score == 21:
        print(f"You have a Blackjack! You win! 🃏")
    elif dealer_score == 21:
        print("The dealer has a blackjack. You lose ☹️")
    

def run_game():
    deal_card()
    calculate_score()

run_game()

