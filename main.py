def amount_of_lives(dict,i,j):
	dx = [-1,-1,-1,0,1,1,1,0];
	dy = [-1,0,1,1,1,0,-1,-1];
	s = 0;
	for k in range(8):
		if dict.get(i+dx[k], j+dy[k])==1:
			++s;
	return s;
	
def output_matrix(dict,n,m):
	for i in range(n):
		var strLine="";
		for j in range(m):
			strLine+=dict.get(i,j);
		print str;
		
