

class Animal:
    species = "Generic Animal"

    @classmethod
    def sound(cls):
        return "Some generic sound"

class Dog(Animal):
    species = "Dog"

    @classmethod
    def sound(cls):
        return "Bark!"

# Call the class method on both the base class and subclass
print(Animal.sound())  # Output: Some generic sound
print(Dog.sound())  # Output: Bark!
