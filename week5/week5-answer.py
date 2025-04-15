# QUESTION 1: 

class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self.alias = alias
        self._power_level = power_level 

    def get_identity(self):
        return f"{self.alias} is the secret identity of {self.name}"

    def use_power(self):
        return f"{self.alias} uses a mysterious power!"

    def get_power_level(self):
        return self._power_level

    def set_power_level(self, new_level):
        if 0 <= new_level <= 100:
            self._power_level = new_level
        else:
            print("Power level must be between 0 and 100.")


class FlyingHero(Superhero):
    def __init__(self, name, alias, power_level, flight_speed):
        super().__init__(name, alias, power_level)
        self.flight_speed = flight_speed  # in km/h

    def use_power(self):
        return f"{self.alias} soars through the skies at {self.flight_speed} km/h!"

    def boost_speed(self, amount):
        self.flight_speed += amount
        return f"{self.alias}'s flight speed is now {self.flight_speed} km/h."



class StrengthHero(Superhero):
    def __init__(self, name, alias, power_level, strength_rating):
        super().__init__(name, alias, power_level)
        self.strength_rating = strength_rating  # e.g., tons lifted

    def use_power(self):
        return f"{self.alias} lifts {self.strength_rating} tons with ease!"

    def train(self):
        self.strength_rating += 10
        return f"{self.alias}'s strength increased to {self.strength_rating} tons."



skybolt = FlyingHero("Amara Chen", "Skybolt", 85, 700)
titan = StrengthHero("Leo King", "Titan", 90, 50)


print(skybolt.get_identity())
print(skybolt.use_power())
print(skybolt.boost_speed(100))

print(titan.get_identity())
print(titan.use_power())
print(titan.train())







# QUESTION 2
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclasses with unique implementations of move()
class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road."


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying in the sky."


class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing across the water."


# polymorphism
def travel(vehicle):
    print(vehicle.move())


# vehicle objects
my_car = Car("Tesla")
my_plane = Plane("Boeing 747")
my_boat = Boat("Sea Breeze")

# Using the same interface (move) for different vehicle types
travel(my_car)
travel(my_plane)
travel(my_boat)
