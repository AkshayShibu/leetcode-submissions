# class parrot:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def sing(self,song):
#         return "{} sings {}".format(self.name,song)
    
#     def dance(self):
#         return "{} is now dancing".format(self.name)
    
# blu=parrot("Blu",10)

# print(blu.sing("happy"))
# print(blu.dance())

# inheritence

# class Bird:
#     def __init__(self):
#         print("Bird is ready")
#     def whoisThis(self):
#         print("Bird")
#     def swim(self):
#         print("swim faster")
    
# child
# class Penguin(Bird):
#     def __init__(self):
#         # call super()function
#         super().__init__()
#         print("Penguin is ready")
#     def WhoisThis(self):
#         print("Penguin")
#     def run(self):
#         print("Run faster")
# peggy=Penguin()
# peggy.WhoisThis()
# peggy.swim()
# peggy.run()


# access modifiers
# class Computer:
#     def __init__(self):
#         self.__maxprice = 900   # private variable

#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):   
#         self.__maxprice = price


# c = Computer()
# c.sell()

# # trying to change directly (won’t affect original)
# c.__maxprice = 1000
# c.sell()

# # using setter method
# c.setMaxPrice(1000)
# c.sell()



class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("parrots can swim")

class Penguin:
    def fly(self):
        print("Penguins  can fly")

    def swim(self):
        print("Penguins  can swim")

def flying_test(bird):
    bird.fly()

blu=Parrot()
peggy=Penguin()

flying_test(blu)
flying_test(peggy)