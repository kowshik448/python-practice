class Person:
    def __init__(self,name):
        self.ame=name
    def talk(self):
        print(f"hi ,i am  {self.ame} ")
name= input("what is your name? ")
p1=Person(name)
p1.talk()