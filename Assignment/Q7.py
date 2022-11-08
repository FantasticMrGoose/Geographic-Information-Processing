#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      zhouzir1
#
# Created:     10/11/2019
# Copyright:   (c) zhouzir1 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# imports math module so we can use "pi" and "e" instead of typing out the integers
import math
# asks the users for their slope in degrees, float to ensure it is in numbers,
#can be positive or negative float, going uphill or downhill
degree = float(raw_input("What is your slope in degrees?"))
# converts degree entered into radians using the math module
radians = degree * math.pi / 180
# separate the exponent for easier implementation and understanding
exp_function = -3.5 * abs(radians + 0.05)
# putting together Tobler's equation to create walkspeed
W = 6 * math.e ** exp_function
# tells the user their estimated walk speed based on their input
print "Your walk speed on a slope of " + str(degree) + " degrees" + " is " + str(W) + " Km/H."
