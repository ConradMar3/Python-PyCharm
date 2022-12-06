# Create a D6.
from Rolling_Dice.die import Die

die = Die()

# Roll, and store results in a list.
results = []

# for roll_num in range(100):
result = die.roll()
results.append(result)

print(results)

# Analyzing the results.
for roll_num in range(1000):
    result = die.roll()
results.append(result)

frequencies = []

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
frequencies.append(frequency)

print(frequencies)
