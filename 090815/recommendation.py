import random


# Define a function that takes a list as its only argument
# Have it return any element of that list


previously_recommended = []


def recommend(restaurants):
    random.shuffle(restaurants)
    candidate = restaurants.pop()

    if candidate in previously_recommended:
        candidate = restaurants.pop()
        return candidate
    else:
        previously_recommended.append(candidate)
        return candidate
