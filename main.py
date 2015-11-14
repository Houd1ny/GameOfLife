import random

ALIVE = 1
DIE = 0

def generate(n, m, prob):
	map = {}
	for i in xrange(n):
		for j in xrange(m):
			piv = random.random()
			if piv > prob:
				map[i,j] = ALIVE
			else:
				map[i,j] = DIE

	return map
