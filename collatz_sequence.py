def collatzSequenceCount (n):
	m = 1
	while n > 1:
		if n & 1:
			n *= 3
			n += 1
			m += 1
		else:
			n /= 2
			m += 1
	return m

def maxCollatzCount (n):
	m = 0
	s = 0
	for i in range (1, n+1):
		g = collatzSequenceCount (i)
		if m <= g:
			m = g
			s = i
	return (s, m)
			
n = int(raw_input('n = '))
print maxCollatzCount (n)
