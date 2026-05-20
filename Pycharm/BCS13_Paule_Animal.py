class Animal:
    def __init__(self, animal, breed, sound, food):
        self.animal = animal
        self.breed = breed
        self.sound = sound
        self.food = food

    def display(self):
        return f"\nYour chosen pet for two weeks: {self.animal}\n\tBreed: {self.breed}\n\tSound: {self.sound}\n\tFood: {self.food}"

animal1 = Animal("Dog", "Golden Retriever", "Arf Arf", "Bones")
animal2 = Animal("Bird", "Eagle", "Chirp", "Worm")
animal3 = Animal("Cat", "Siamese", "Meow Meow", "Fish")
animal4 = Animal("Snake", "Python","Sssss", "Meat")

while True:
    pet = int(input("Welcome to the Vet Academy!!!\nKindly chose your animal to take care for two weeks as your assignment!\n\tAnimal 1: Dog\n\tAnimal "
                      "2: Bird\n\tAnimal 3: Cat\n\tAnimal 4: Snake\n\nYour chosen enemy number: "))
    if pet == 1:
        print(animal1.display())
        break
    elif pet == 2:
        print(animal2.display())
        break
    elif pet == 3:
        print(animal3.display())
        break
    elif pet == 4:
        print(animal4.display())
        break
    else:
        print("Please enter the number of your chosen animal 1-3:")