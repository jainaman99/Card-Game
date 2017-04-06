import random
class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def _convertToFaceValue(self,value):
        d = {1:"Ace",
             2:"Two",
             3:"Three",
             4:"Four",
             5:"Five",
             6:"Six",
             7:"Seven",
             8:"Eight",
             9:"Nine",
             10:"Ten",
             11:"Jack",
             12:"Queen",
             13:"King"
             }
        return d[value]
    def __str__(self):
         return self.suit + " " + self._convertToFaceValue(self.value)