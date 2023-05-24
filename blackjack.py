from art import logo
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
end_game = False


def deal_card():
    user_hand = random.sample(cards, 2)
    dealer_hand = random.sample(cards, 2)
    print(f"""
    Your hand: {user_hand}
    Dealer first card: {dealer_hand[0]} """)
    hands = [user_hand, dealer_hand]
    return hands
    

def calculate_score(hands):
    user_score = sum(hands[0])
    dealer_score = sum(hands[1])
    if user_score == 21:
        print(f"You have a Blackjack! You win! 🃏")
        end_game = True
    elif dealer_score == 21:
        print("The dealer has a blackjack. You lose ☹️")
        end_game = True
    scores = [user_score, dealer_score]
    return scores
    
    
def check_who_wins(scores):
    if scores[0] > 21 and scores[1] < 21:
        print(f"Bust! Your score is {scores[0]},You lose")
        end_game = True
    elif scores[1] > 21 and scores[0] < 21:
        print(f"You win! Dealer score was {scores[1]} ")
        end_game = True

def draw_a_card(scores):
    draw = input("Would you like another card? y or n: ")
    if draw == "y":
        another_card = random.randint(cards)
        scores[0] = scores[0].append(another_card)
        calculate_score(scores)
    else:
        scores[1] = scores[1].append(another_card)
        calculate_score(scores)

        
    
    
    

    

def run_game():
    hands = deal_card()
    while end_game == False:
        scores = calculate_score(hands)
        if end_game == True:
            print("Game Over. Thank you for playing!")
        elif end_game == False:
            check_who_wins(scores)
            if end_game == True:
                print("Game Over. Thank you for playing")
            else:
                draw_a_card(scores)


run_game()

