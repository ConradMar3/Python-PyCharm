from plotly import offline
from plotly.graph_objs import Bar, Layout

from die import Die

# Create TWO D6 dice.
die_1 = Die()
die_2 = Die(10)

# Roll, and store results in a list.
results = []

# for roll_num in range(1000):
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    # result = die.roll()
    results.append(result)

# print(results)

# Analyzing the results.
# for roll_num in range(1000):
# result = die.roll()
# results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    # for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
# x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

# my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
# my_layout = Layout(title='Results of rolling one D6 1000 times',
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
