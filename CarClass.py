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
# Create a Car object
# Call the accelerate method five times and display current speed
# Call the brake method five times and display current speed