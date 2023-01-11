import time

#END OF IMPORTS

class Pet():
  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.weight = weight

  def info(self):
    print("Here is your pet's information.")
    print("NAME: "+self.name.title())
    print("AGE: "+self.age)
    print("WEIGHT: "+self.weight)

  def eat(self):
    print(self.name.title()+" is now eating.")

#END OF PARENT CLASS

class Dog(Pet):
  def __init__(self, name, age, weight):
    super().__init__(name, age, weight)

  def bark(self):
    print("BARK!")

  def sit(self):
    print(self.name.title()+" is sitting still.")

  def RollOver(self):
    print(self.name.title()+" has rolled over.")

#END OF DOG SUBCLASS

class Cat(Pet):
  def __init__(self, name, age, weight):
    super().__init__(name, age, weight)

  def meow(self):
    print("MEOW!")

  def laser(self):
    print(self.name.title()+" is trying to catch the laser's dot.")

  def Catsleep(self):
    print(self.name.title()+" is now asleep")

#END OF CAT SUBCLASS AND ALL SUBCLASSES

print("""Welcome to Pet Simulator!

Today you will create a Dog and a Cat.

""")
time.sleep(2)

print("""Let's start with a Dog

What is your Dog's name?
""")

DogName = input()
print("""
How old are they? (In years)
""")

DogAge = input()
print("""
What is the their weight? (In pounds)
""")
DogWeight = input()

UserDog = Dog(DogName, DogAge, DogWeight)

print("""
Now you can create your Cat!

What is the your Cat's name?
""")
CatName = input()

print("""
How old are they? (in years)
""")
CatAge = input()

print("""
What is their weight? (In pounds)
""")
CatWeight = input()

UserCat = Cat(CatName, CatAge, CatWeight)

#END OF COLLECTING CLASS INFORMATION

print("""
Now you can play with your pets!
""")

while True:
  print(" ")
  print("""If you want to play with your Dog enter 1, if you want to play with your Cat enter 2, or if you are done playing enter 'Done'. """)
  PetAnswer = input()
  if PetAnswer == "1":
    print("""
You Have decided to play with your Dog.
Type 1, to get their basic information
Type 2, for them to eat.
Type 3, for them to bark.
Type 4, for them to sit.
Or
Type 5, for them to roll over""")
    DogAction = input()
    if DogAction == "1":
      print(" ")
      UserDog.info()
    elif DogAction == "2":
      print(" ")
      UserDog.eat()
    elif DogAction == "3":
      print(" ")
      UserDog.bark()
    elif DogAction == "4":
      print(" ")
      UserDog.sit()
    elif DogAction == "5":
      print(" ")
      UserDog.RollOver()
  elif PetAnswer == "2":
    print("""
You Have decided to play with your Cat.
Type 1, to get their basic information
Type 2, for them to eat.
Type 3, for them to meow.
Type 4, for them to chase a laser pointer.
Or
Type 5, for them to sleep.""")
    CatAction = input()
    print(" ")
    if CatAction == "1":
      UserCat.info()
    elif CatAction == "2":
      UserCat.eat()
    elif CatAction == "3":
      UserCat.meow()
    elif CatAction == "4":
      UserCat.laser()
    elif CatAction == "5":
      UserCat.Catsleep()
  elif PetAnswer.title() == "Done":
    print("""
    You have finished playng with your pets.""")
    break