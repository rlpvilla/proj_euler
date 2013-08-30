from operator import mul

def isPythTriplet (a, b, c):
	if (a**2 + b**2 == c**2):
		return True


def findPythTriplet (c):
	a = 0
	b = 0
	for i in range (1, c):
		b = i
		for j in range (1, b):
			a = j
			if isPythTriplet (a, b, c):
				return (a, b, c)
	return False

def pythTripletOfSum (s):
	g = 0
	for i in range (1, s):
		value = findPythTriplet(i)
		if value != False:
			if (s % sum(value)) == 0:
				g = (s/sum(value))
				return (value[0]*g, value[1]*g, value[2]*g)
	return False

def listProduct(list):
	p = 1
	for i in list:
		p *= i
	return p

s = int(raw_input ('sum = '))
value = pythTripletOfSum(s)
print listProduct(value)
