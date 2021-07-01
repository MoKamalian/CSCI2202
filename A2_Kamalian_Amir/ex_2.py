# Amir Kamalian - CSCI 2202 - A2
# Problem 2 - This program simulates a game of choosing a door with a car behind it. In one scenario only one door is
#             chosen, in the second scenario a new door is chosen after the first choice randomly from the remaining
#             doors. Success probability of choosing the correct door with the car are then printed.

from random import randrange, choice

simulations = int(input('Enter number of simulations: '))
door_with_car = randrange(1, 3, 1)


# Not switched doors
door_choice = []
for s in range(simulations):
    door_choice.append(randrange(1, 3, 1))

success_probability = door_choice.count(door_with_car) / len(door_choice)
print(success_probability)


# Door switched
door_choice2 = []
for s in range(simulations):
    doors = [1, 2, 3]
    door_chosen = choice(doors)
    doors.remove(door_chosen)
    new_choice = choice(doors)
    door_choice2.append(new_choice)

success_probability2 = door_choice2.count(door_with_car) / len(door_choice2)
print(success_probability2)






