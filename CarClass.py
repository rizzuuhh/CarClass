class Car:
    def __init__(self, year_model, make):
     # Initialize data attributes
     self.__year_model = year_model
     self.__make = make
     self.__speed = 0

     # Increase the speed by 5
    def accelerate(self):
      self.__speed += 5

     # Decrease the speed by 5
    def brake(self):
      self.__speed -= 5

     # Ensure speed is not negative
      if self.__speed < 0:
        self.__speed = 0

     # Return the current speed
    def get_speed(self):
      return self.__speed

# Create a Car object
car = Car(2021, "Toyota")

# Call the accelerate method five times and display current speed
for _ in range(5):
    car.accelerate()
    current_speed = car.get_speed()
    print("Current speed of the car:", current_speed)


# Call the brake method five times and display current speed