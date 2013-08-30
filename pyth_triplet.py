import math

def isPythTriplet (a, b, c):
	if (a**2 + b**2 == c**2):
		return True

def tripletSums (a, b, c, sum):
	if (a + b + c == sum):
		return True

def findPythTriplet (c):
	a = 0
	b = 0
	for i in range (1, c):
		b = i
		for j in range (1, b):
			a = j
			if isPythTriplet (a, b, c):
				return (a, b)

def locatePythTripletSum (sum):
	for i in range (1, sum):
		c = i
		value = findPythTriplet (c)
		if tripletSums (*args, c, sum):
			return (*args, c)

def productOfTriplet (a, b, c):
	return (a * b * c)

