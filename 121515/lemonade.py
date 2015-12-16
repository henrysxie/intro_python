# Set variables, e.g. lemonade_num
# Use the input function, cast as integers

lemonades_sold = int(input("How many cups of lemonades did you sell? "))
num_hours = int(input("How many hours did you work? "))

price = 5
lemons_per_lemonade = 4
cost_per_lemon = 0.5

revenue = price * lemonades_sold
expenses = lemonades_sold * lemons_per_lemonade * cost_per_lemon

profit = revenue - expenses
profit_per_hour = profit / num_hours

print("You made ${}, or ${} per hour".format(
    profit, profit_per_hour
))