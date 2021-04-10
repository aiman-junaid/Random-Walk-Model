import random
import turtle
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


def task1(steps, prob, move):
    x = 0
    if not move:
        return x
    for _ in range(steps):
        if random.random() < prob:
            x -= 1
        else:
            x += 1
    return x

# Task 1
# expected1 = 0
# walks1=[]
# for i in range(1000):
#     walks1.append(task1(100, 0.5, True))
# expected1= sum(walks1)/1000
# print(expected1)
# plt.title('Distances travelled')
# plt.hist(walks1, bins=50, color='blue')
# plt.xlabel('Distance from starting point')
# plt.ylabel(' Frequency')
# plt.grid(True)
# plt.show()

# pyplot.plot(random_walk(100, 50))
# pyplot.plot(random_walk(100, 20))
# pyplot.legend(["Walk1", "Walk2"])
# pyplot.show()


def task2(prob, move1, move2):
    x, y = 0, 50
    steps = 0
    while x != y:
        if random.random() < prob:
            x -= 1
            x*= move1
            y += 1
            y *= move2
        else:
            x += 1
            x *= move1
            y -= 1
            y *= move2
        steps += 1
    return steps


# Task 2
expected2 = 0
walks2 = []
for i in range(100):
    # We assume the speed of a random walk to be 1.4 m/s
    walks2.append(task2(0.5, True, False))
expected2 = sum(walks2)/100
print(walks2)
plt.title('Time taken')
plt.hist(walks2, bins=50, color='blue')
plt.xlabel('Time to meet')
plt.ylabel(' Frequency')
plt.grid(True)
plt.show()


def task3(steps, p1, p2):
    orientation_prob = [1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]
    step_prob = [1/3, 1/3, 1/3]
    orientation = [0, 45, 90, 135, 180, 225, 270, 315]
    step_size = [0, 0.5, 1]
    # if prob of each orientation isn't equally likely
    if not p1:
        orientation_prob = [0.3, 0.2, 0.1, 0.4]
    # if prob of each step isn't equally likely
    if not p2:
        step_prob = [1/2, 0.2, 0.3]
    for _ in range(steps):
        # if turtle goes out or circle's boundary, it sends it back
        # choosing turtle's orientation and steps using thier prob, randomly
        angle = np.random.choice(orientation, p=orientation_prob)
        dist = np.random.choice(step_size, p=step_prob)
        # 1 cm = approximately 38 pixels
        dist *= 38
        if angle == 0:
            path.forward(dist)
        elif angle == 90:
            path.right(90)
            path.forward(dist)
        elif angle == 180:
            path.backward(dist)
        elif angle == 270:
            path.left(90)
            path.forward(dist)
        if path.distance(0, 0) >= 100:
            # path.setheading(path.towards(0,0))
            path.penup()
            path.goto(0, 0)
            path.pendown()


# Task 3
# circle = turtle.Turtle()
# circle.penup()
# circle.sety(-100)
# circle.pendown()
# circle.circle(100)
# path = turtle.Turtle()
# path.color("red")
# task3(100, True,True)

def task4(steps, prob, move):
    x = 0
    if not move:
        return x
    for _ in range(steps):
        if random.random() < prob:
            x -= np.random.uniform(0, 1)
        else:
            x += np.random.uniform(0, 1)
    return x

# Task 4
# expected3 = 0
# walks3=[]
# for i in range(1000):
#     walks3.append(task4(100, 0.5, True))
# expected3= sum(walks3)/1000
# print(expected3)
# plt.title('Distances travelled')
# plt.hist(walks3, bins=50, color='blue')
# plt.xlabel('Distance from starting point')
# plt.ylabel(' Frequency')
# plt.grid(True)
# plt.show()


def task5(steps, p1, p2):
    orientation_prob = [0.25, 0.25, 0.25, 0.25]
    step_prob = [1/3, 1/3, 1/3]
    orientation = [0, 90, 180, 270]
    step_size = [0, 0.5, 1]
    # orientation_prob =
    # if prob of each orientation isn't equally likely
    if not p1:
        orientation_prob = [0.3, 0.2, 0.1, 0.4]
    # if prob of each step isn't equally likely
    if not p2:
        step_prob = [1/2, 0.2, 0.3]
    for _ in range(steps):
        # if turtle goes out or circle's boundary, it sends it back
        # choosing turtle's orientation and steps using thier prob, randomly
        angle = np.random.choice(np.random.uniform(0, 360), p=orientation_prob)
        dist = np.random.choice(step_size, p=step_prob)
        # 1 cm = approximately 38 pixels
        dist *= 38
        if angle == 0:
            path.forward(dist)
        elif angle == 90:
            path.right(90)
            path.forward(dist)
        elif angle == 180:
            path.backward(dist)
        elif angle == 270:
            path.left(90)
            path.forward(dist)
        if path.distance(0, 0) >= 100:
            # path.setheading(path.towards(0,0))
            path.penup()
            path.goto(0, 0)
            path.pendown()
