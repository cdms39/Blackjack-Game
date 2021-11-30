from game_master import Game_Master
from player import Player
import random

gm = Game_Master()

# Main loop of the game
while gm.play == 'y':
    user = Player()
    dealer = Player()

    print("\nWelcome to BLACKJACK!")

    # Initializes cards in deck
    print(f"\nCard Deck: {gm.cards}")

    # Randomly initializes two cards for player and dealer
    for _ in range(2):
        user.add_card(gm.cards[random.randint(0, len(gm.cards)-1)])
        dealer.add_card(gm.cards[random.randint(0, len(gm.cards)-1)])
    
    print(f"\nINITIAL ROUND\nYour Hand: {user.hand}")
    print(f"Dealer Hand: [{dealer.hand[0]}, ?]")
    
    
    # Initally calculates the sum of current hands
    user.hand_sum = gm.calculate_hand(user.hand)
    dealer.hand_sum = gm.calculate_hand(dealer.hand)
    
    # Asks player if they'd like to hit (continues until 'no' or if hand is above 21)
    gm.hit_card(user)
    
    if gm.game_over != True:
        # Checks if dealer's hand sum is below 17; adds another card if so
        gm.set_dealer(dealer)

        # Calculates the final sum of the hands
        user.hand_sum = gm.calculate_hand(user.hand)
        dealer.hand_sum = gm.calculate_hand(dealer.hand)

    print(f"\nFINAL ROUND\nYour Hand: {user.hand}")
    print(f"Dealer Hand: {dealer.hand}")

    print(f"\nPlayer sum: {user.hand_sum}")
    print(f"Dealer sum: {dealer.hand_sum}")

    print(gm.set_result(user.hand_sum, dealer.hand_sum))
   
    gm.to_play_again()
            

# Outside main loop      
print("\nThank you for playing Blackjack!\n")