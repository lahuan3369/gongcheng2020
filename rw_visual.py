import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
	rw=RandomWalk(70000)
	rw.fill_walk()
	
	plt.figure(figsize=(10,6))
	point_numbers=list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,
	cmap=plt.cm.Oranges,edgecolor='none',s=1)
	plt.show()
	
	keep_running=input("再来一次?(y/n):")
	if keep_running=='n':
		break
