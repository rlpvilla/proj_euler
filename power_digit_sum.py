def bin_pow (n):
	value = 2 << (n-1)
	return value

def sum_digits (num):
	s = 0
	for i in str(num):
		s += int(i)
	return s

n = int(raw_input ('n = '))
print sum_digits (bin_pow (n))
