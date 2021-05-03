import datetime
import random

file = open("events.txt", "r")

for line in file:
    values = line.splitlines()
    print(values)

file.close()