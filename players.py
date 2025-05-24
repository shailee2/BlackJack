class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def receive(self, card):
        self.cards.append(card)
        return

    def clear(self):
        self.cards = []
        return

    def total(self):
        total = 0
        aces = 0
        for card in self.cards:
            total += card.value
            if card.rank == "Ace":
                aces += 1
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def show_cards(self):
        card_str = ""
        for card in self.cards:
            card_str += str(card) + " and "
        return card_str.strip(" and ")
        
class House(Player):
    def __init__(self):
        super().__init__("House")

    
