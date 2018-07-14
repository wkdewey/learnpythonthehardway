#define variable cars with number of cars
cars = 100
#define variable "space_in_a_car" with the number of people who can go in each car
space_in_a_car = 4.0
#define variable "drivers" with number of drivers
drivers = 30
#define variable "passengers" with number of passengers
passengers = 90
#define variable cars_not_driven calculated by subtracting number of cars from drivers
cars_not_driven = cars - drivers
#define variable cars_driven as equal to the number of drivers (also a variable)
cars_driven = drivers
#define variable carpool_capacity by multiplying cars driven and space in a car
carpool_capacity = cars_driven * space_in_a_car
#define variable average_passenger_per_car by dividing passengers by the number of cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."