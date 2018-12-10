from rank import rank
from suit import suit

class card():
    def __init__(self,parameter_suit,parameter_rank):
        r = rank()
        valid_rank = r.validate(parameter_rank)

        s = suit()
        valid_suit = s.validate(parameter_suit)
        
        if(valid_rank and valid_suit):
            self.suit = parameter_rank
            self.rank = parameter_rank
        else:
            raise ValueError("Ivalid Rank or Suit")
            self.suit = "invalid"
            self.rank = "invalid"
                
    def display(self):
        print(self.rank + " of " + self.suit)