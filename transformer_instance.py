class Bot:
    def walk(self): print("I walk.")


class SuperBot(Bot):
    def fly(self): print("I fly!")


b = Bot()
b.walk()

b.__class__ = SuperBot   # Mutation
b.walk()
b.fly()
