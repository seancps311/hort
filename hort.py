# hort.py
# Program to flip a coin

import random

numFlips = int(input("How many flips? "))

flipCount = 0
while (flipCount < numFlips):

	flip = random.randint(0, 1)
	if (flip == 0):
    		flipWord = "heads"
	else:
    		flipWord = "tails"

	print("I flipped a coin and got ", flipWord, ".")

	flipCount += 1

