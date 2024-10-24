import random as rng

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    def value(self):
        if self.rank > 10:
            return 10
        else: 
            return self.rank
        
    def __str__(self):
        suit = {"d" : "diamonds", "c" : "clubs", "h" : "hearts", "s" : "spades"}
        rank = {1 : "Ace", 11 : "Jack", 12 : "Queen", 13 : "King"}
        
        rank_str = rank.get(self.rank, str(self.rank))
        suit_str = suit[self.suit]

        return f"{rank_str} of {suit_str}"
        

def main():
    total_draws = int(input("How many cards do you want to draw?: "))
    for i in range(total_draws):
        rank = rng.randrange(1,14)
        suit_dic = {1 : "d", 2 : "c", 3 : "h", 4 : "s"}
        suit = suit_dic[rng.randrange(1,5)]
        card = Card(rank, suit)
        print(f"{card}")
        
    
if __name__ == "__main__":
    main()