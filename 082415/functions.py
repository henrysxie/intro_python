"""
Write a function that takes a list of food orders as input
e.g. ["burger", "fries", "burger", "ice_cream"]

It should return a tally of your food orders
e.g.
{
    "burger": 2,
    "fries": 1,
    "ice_cream": 1
}
"""

def tally_food_orders(food_orders):
    # create empty dictionary
    tally = {}

    # unique_food_orders = list(set(food_orders))

    for food_order in unique_food_orders:
        tally[food_order] = food_orders.count(food_order)

    return tally



def tally_food_orders(food_orders):
    # create empty dictionary
    tally = {}

    for food_order in food_orders:
        if not "food_order" in tally:
            tally[food_order] = 1
        else:
            tally[food_order] += 1

    return tally



def add(term_1, term_2):
    return term_1 + term_2


def evenly_divisible_by(divisor, max_number=100):
    """
    Prints all numbers from zero up until `max_number`
    that are evenly divisble by `divisor`.
    """
    for number in range(max_number):

        # Remainder is zero when evenly divisible
        if not number % divisor:
            print number
