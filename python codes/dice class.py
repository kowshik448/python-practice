import random
class dice:
    def roll(self):
        x=random.randint(1,6)
        y=random.randint(1,6)
        return (x,y)

d1=dice()
print(d1.roll())