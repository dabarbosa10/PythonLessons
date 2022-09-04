import math

class Cereal:
    """Create a class called Cereal that accepts three inputs: 2 string
    and 1 integer, and assigns them to three instance variables in the constructor:"""
    
    def __init__(self, nam, bran, fibe):
        self.name=nam
        self.brand=bran
        self.fiber=fibe
    
    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand, 
                                                                                                self.fiber)
    
    
class Fruit():
    
    def __init__(self, name, price):
        self.name=name
        self.price=price
    
    def sort_priority(self):
        print("------- Sorted by price: -------")
        return self.price
        
        