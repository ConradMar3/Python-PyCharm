from car import Car as C 
from electric_car import ElectricCar as EC 
from battery import *

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_nissan = C('nissan','gtr', 2020)
print(my_nissan.get_descriptive_name())