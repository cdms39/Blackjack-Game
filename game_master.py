import random
import os


class Game_Master():

    def __init__(self):
        # Initializes the cards to be played
        
        self.SPECIAL_CARDS = {
            "K": 10,
            "Q": 10,
            "J": 10,
            "A": 11,
        }

        self.cards = []
        for num in range(2, 11):
            self.cards.append(num)
        for key in self.SPECIAL_CARDS:
            self.cards.append(key)

        # Initializes the game to begin
        self.play = 'y'
        self.game_over = False
        self.to_hit = 'y'
        
        
    def initialize_state(self):
        """Re-initializes the game state when playing again"""
        
        self.game_over = False
        self.to_hit = 'y'


    def clear_console(self):
        """Clears the console"""
        
        command = 'clear'
        if os.name in ('nt', 'dos'): #Sets command as 'cls' if system runs on Windows
            command = 'cls'
        os.system(command) #Issues clear command to system interpreter


    def calculate_hand(self, hand):
        """Adds the sum of the hand of cards"""
        
        total_sum = 0

        for card in hand:
            if isinstance(card, int):
                total_sum += card
            
            # Checks if card is special (if str) and applies respective values to it
            elif isinstance(card, str):
                for key in self.SPECIAL_CARDS:
                    if card == key and key != 'A':
                        total_sum += self.SPECIAL_CARDS[key]
                    elif card == key and key == 'A':
                        if (total_sum + self.SPECIAL_CARDS[key]) > 21:
                            total_sum += 1
                        else:
                            total_sum += self.SPECIAL_CARDS[key]

        return total_sum


    def set_result(self, player_sum, dealer_sum):
        """Sets round result based on the sums"""
        
        if player_sum <= 21 and dealer_sum <= 21:
            if player_sum > dealer_sum:
                return "\nYou win!"
            elif player_sum == dealer_sum:
                return "\nIt's a draw!"
            else:
                return "\nYou lose."

        elif player_sum <= 21 and dealer_sum > 21:
            return "\nYou win!"
        elif player_sum > 21 and dealer_sum > 21:
            return "\nIt's a draw!"
        else:
            return "\nIt's a bust. You lose."


    def hit_card(self, hitter):
        """Allows player to hit to their hand"""
        
        while (self.to_hit != 'n' and hitter.hand_sum < 21) and self.game_over == False:
            self.to_hit = input("\nWould you like to hit ('y' or 'n')? ")
            self.to_hit = self.to_hit.lower()

            if self.to_hit == 'y':
                # Adds a card if 'yes', and calculates the updated sum of the hand
                hitter.add_card(self.cards[random.randint(0, len(self.cards)-1)])
                hitter.hand_sum = self.calculate_hand(hitter.hand)
                print(f"\nYour Hand: {hitter.hand}")

            elif self.to_hit != 'n':
                print("Choice invalid.")
        
            if hitter.hand_sum > 21:
                #Sets game over if player's hand is now over 21
                self.game_over = True


    def set_dealer(self, dealer):
        """Adds more cards to the dealer's hand"""
        
        #Adds more cards to the dealer's hand, as long as their total is still less than 17
        while dealer.hand_sum < 17:
            dealer.hand.append(self.cards[random.randint(0, len(self.cards)-1)])
            dealer.hand_sum = self.calculate_hand(dealer.hand)


    def to_play_again(self):
        """Asks player if they'd like to play again"""
        
        self.play = 'n'

        while self.play != 'y':
            self.play = input("\nWould you like to play again ('y' or 'n')? ")
            self.play = self.play.lower()

            if self.play == 'y':
                self.initialize_state()
                self.clear_console()
            elif self.play != 'n':
                print("\nChoice invalid.")

