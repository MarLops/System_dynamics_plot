from __future__ import division
import matplotlib.pyplot as plt
import numpy as np



def Solution_discrete_system(Function,Initial_position,Parameters,Steps):
	
	#Return the value of system in each step and time
	#Return Array NxM. N = dimensional of system. M = number of steps.
	#Function = Array
	#Initial_position = Array
	#Parameters = Array of array. Each Parameters'function need to be array. In funciton, need separete with parameters will be used
	#Steps = Int

	

	if len(Function) != len(Initial_position):
		print ("No corret")
		return 0

	Position = [[]]
	Future = []

	for i in Initial_position:
		Position[0].append(i)
		Future.append(0)


	
	for i in range(Steps):
		Position.append([])
		for j in range(len(Function)):
			Future[j] = Function[j](Position[i],Parameters)
			Position[i + 1].append(Future[j])

	
	
	Time = range(Steps + 1)

	return Time, Position

def plot_all_X(X,Y,labels,Title,xlim=0,ylim=0,lim=False,loc=4,save=False,missplot=False,number_plot_miss=0):

	#Plot all the variables with labels
	#missplot = ignore one of variable
	#number_plot_miss = the number of variable will be ignore
	



	Separete_Y = []
	for i in range(len(Y[0])):
		y = [ j[i] for j in Y ]
		Separete_Y.append(y)

	
	if not missplot:
		for y,la in zip(Separete_Y,labels):
			plt.plot(X,y,label=la)

	else:
		for n_y,n_la in zip(range(len(Separete_Y)),range(len(labels))):
			if n_y not in number_plot_miss:
				plt.plot(X,Separete_Y[n_y],label=labels[n_la])
	try:
		if not lim:
			if len(xlim) == 2:
				plt.xlim(left=xlim[0])
				plt.xlim(right=xlim[1])
			else:
				plt.xlim(left=xlim[0])

			if len(ylim) == 2:
				plt.xlim(bottom=ylim[0])
				plt.xlim(top=ylim[1])
			else:
				plt.xlim(bottom=ylim[0])		
	except:
		pass
		


	plt.title(Title)
	plt.legend()

	if save:
		plt.savefig(Title + ".png")
	else:
		plt.show()


def main_example():
	
	#Define the function
	def Logistic_equation(X,Parameters):
		x = X[0]
		R = Parameters[0]
		return R*x*(1-x) 

	#Create the inputs
	Function = [Logistic_equation]
	Initial_position = [0.1]
	Parameters = [2]
	Steps = 1000
	labels = [r'$x_t$']
	Title = "logistic_map"

	Time, Solution = Solution_discrete_system(Function,Initial_position,Parameters,Steps)
	plot_all_X(Time,Solution,labels,Title)

