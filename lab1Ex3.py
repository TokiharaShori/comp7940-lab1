def get_factor(x):
	for i in x:
		print('The factors of %d:' %i)
		for j in range(1, i+1):
			if i % j == 0:
				print(j)
l =  [52633, 8137, 1024, 999]
get_factor(l)