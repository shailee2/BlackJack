from deck import Deck
from player import Player, House

def start_game(): 
    continue_game = True
    name = input("What is your name?")
    p1 = Player(name)
    print("\nWelcome to Blackjack, " + name + ".")
    while True:
        p1_init_amt = input("\nWhat amount would you like to start with? Please enter a number.")
        try:
            p1_init_amt = float(p1_init_amt)
            if p1_init_amt <= 0:
                print("Amount must be a positive number.")
            else:
                print("Initial Amount Updated: $" + str(p1_init_amt))
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    p1_winnings = p1_init_amt
    house = House()
    while continue_game:
        continue_game_input = input("\nWould you like to start a new round? Y/N")
        if continue_game_input not in ['Y', 'N']:
            print("This is an invalid input.")
        elif continue_game_input == 'N':
            continue_game = False
            print("Game Over")
        else:
            if p1_init_amt <= 0:
                print("Insufficient Funds. Game Over")
                break
            deck_ = Deck() #creates the deck we are using
            deck_.shuffle() #shuffle deck
            p1.clear()
            house.clear()
            for i in range(2):
                p1.receive(deck_.deal())
                house.receive(deck_.deal())
            while True:
                bet_amt = input("\nWhat bet would you like to place? $")
                try:
                    bet_amt = float(bet_amt)
                    if bet_amt <= 0:
                        print("Bet must be a positive number.")
                    elif bet_amt > p1_init_amt:
                        print("Insufficient funds.")
                    else:
                        print("Bet placed: $" + str(bet_amt))
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            p1_sum = p1.total()
            card_strs = p1.show_cards()
            if len(p1.cards) == 2 and p1_sum == 21:
                print(f"\nYou are dealt the {p1.show_cards()}. Blackjack!")
                p1_winnings += bet_amt * 1.5
                print(f"You win 1.5 times your bet! Total winnings: ${p1_winnings}")
                continue 
            house_card_1 = house.show_first_card()
            print(f"\nDealer has the {house_card_1}.")
            print(f"\nYou are dealt the {card_strs}. Your total is {p1_sum}.")
            status = "tbd"
            while status not in ["stand","hit"]:
                status = input("\nWould you like to hit or stand?").lower()
                if status not in ["stand","hit"]:
                    print("This is an invalid input.")
            if status == "hit":
                while True:
                    new_card = deck_.deal()
                    p1.receive(new_card)
                    p1_sum = p1.total()
                    print(f"You drew {new_card}. Your total is now {p1_sum}.")
                    if p1_sum > 21:
                        p1_winnings -= bet_amt
                        print("You busted! Total winnings: $" + str(p1_winnings))
                    if p1_sum >= 21:
                        break
                    status = input("\nWould you like to hit or stand?").lower()
                    if status == "stand":
                        break
            if status == "stand":
                house_sum = house.total()
                house_strs = house.show_cards()
                print(f"\nThe dealer has the {house_strs}. The dealer's total is {house_sum}.")
                while house_sum < 17:
                    new_card = deck_.deal()
                    house.receive(new_card)
                    house_sum = house.total()
                    print(f"Dealer hits and draws {new_card}. Total is now {house_sum}.")
                if house_sum > 21 or house_sum < p1_sum:
                    p1_winnings += bet_amt
                    print("\nYou win! Total winnings: $" + str(p1_winnings))
                elif house_sum > p1_sum:
                    p1_winnings -= bet_amt
                    print("\nDealer wins. Total winnings: $" + str(p1_winnings))
                else:
                    print("\nIt's a tie! Total winnings: $" + str(p1_winnings))
    net_winnings = p1_winnings - p1_init_amt
    if net_winnings >= 0:
        print("\nYou won $" + str(net_winnings) + "!")
    else:
        print("\nYou lost $" + str(abs(net_winnings)) + ".")
    return
