import random
import os

ALIVE = 1
DIE = 0
def amount_of_lives(dict,i,j):
	dx = [-1,-1,-1,0,1,1,1,0];
	dy = [-1,0,1,1,1,0,-1,-1];
	s = 0;
	for k in range(8):
		if dict.get(i+dx[k], j+dy[k])==1:
			++s;
	return s;
	
def output_matrix(map,n,m):
	for i in xrange(n):
		strLine="";
		for j in xrange(m):
			strLine = strLine + str(map[i,j]) + " " 
		print strLine;
		

def generate(n, m, prob):
	map = {}
	for i in xrange(n):
		for j in xrange(m):
			piv = random.random()
			if piv < prob:
				map[i,j] = ALIVE
			else:
				map[i,j] = DIE

	return map

def main() :
	n = 10
	m = 10
	map = generate(n,m, 0.3)
	while True:	
		output_matrix(map, n, m)
		os.system('cls')

if __name__ == '__main__':
    main()

