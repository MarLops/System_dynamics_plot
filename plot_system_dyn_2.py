# Cobweb, bifurcation orbit,expoent Lyp

import numpy as np
import matplotlib.pyplot as plt
from decimal import *
#getcontext().prec = 10

#np.seterr(all='ignore')


def Logistic_equation(X,Parameters):
	x = X[0]
	R = Parameters[0]
	return R*x*(1-x)

def Logistic_equation2(X,Parameters):
	x = X[1]
	R = Parameters[0]
	return R*x*(1-x)

def Tend_equation(X,Parameters):
	R = Parameters[0]
	return R*(min(X,1-X))

def Line(Initial,Final,Point_continuoss):
	X = np.linspace(Initial,Final,Point_continuoss)
	return  X

def cobweb(X_o=[0.11],N_steps=200,func=[Logistic_equation],Parameters = [3.1],Initial_continuos=0,Final_continuos=1,N_steps_continuos = 20000,save=False,title_plot=False,xlab=False,ylab=False,s=False,export=False,title_file=False):

	""" Create cobweb to 1D system
	X_o = initial value. Need to be array 1D
	N_steps = number of X_n the program will calculate
	
	func = the function f(X_n) = X_{n+1}. Need to be array 1D
	Parameters = array with all Parameters func has.
	Initial_continuos = first point to construct the continuos function
	Final_continuos = final point to construct the continuos function
	N_steps_continuos = number of points in continuos function

	save = save the plot (option True) or just show (option False)
	title_plot = name of .png
	xlabel = name of x-axes
	ylabel = name of y-axes
	s = The marker size in points**2

	export = export datas as .txt (option True)
	title_file = name of .txt
	"""
 	#### Calculate #######
 	
	X_d = X_o
	
	for i in range(N_steps):
		X_d.append(func[0]([X_d[i]],Parameters))

	

	X_c = [np.linspace(Initial_continuos,Final_continuos,N_steps_continuos)]
	Y_c = []
	for j in X_c[0]:
		l = [j]
		Y_c.append(func[0](l,Parameters))
		
	
	X_line = Line(Initial_continuos,Final_continuos,2000)
	
	eixo_x = []
	eixo_y = []
	j = 0
	k = 0
	g = 0
	l = 1
	for i in range(2*N_steps):
		if j <= 1:
			eixo_x.append(X_d[k])
			j = j +1
		else:
			k = k + 1
			eixo_x.append(X_d[k])
			j = 1

		if i == 0:
			eixo_y.append(0)
		else:
			if g <= 1:
				eixo_y.append(X_d[l])
				g = g + 1
			else:
				l = l + 1
				eixo_y.append(X_d[l])
				g = 1
	

	#####PLOT######
	
	if s == False:
		s = [10*1**1 for j in range(len(eixo_x))]
	else:
		s = [s for j in range(len(eixo_x))]

	plt.plot(X_c[0],Y_c,color='red',label="continuos")
	plt.plot(X_line,X_line,color='blue',label="line")
	plt.plot(eixo_x,eixo_y,'-ro',color='green',label='cob')
	
	if ylab == False:
		ylab = r'$X_{n+1}$'
	if xlab == False:
		xlab = r'$X_n$'

	plt.ylabel(ylab)
	plt.xlabel(xlab)
	plt.legend()
	plt.title("Cobweb")
	
	###### Adjust plot name ######
	if save == False:
		plt.show()
	else:
		if title_plot == False:
			j = ""
			for i in Parameters:
				j = j + "_" + str(i)
			title_plot = str(func).split()[1] + "_Parameters_" + j + "_.png" 
		if '.png' in title_plot:
			title = title_plot
		else:
			title_plot = title_plot + ".png"
		
		plt.savefig(title_plot)

	#### Export #####
	if export:

		####Adjust file name######
		if title_file == False:
			title_file = "cobweb.txt"
		else:
			if ".png" in title_file:
				title_file=title_file
			else:
				title_file = title_file + ".txt"

		###### Write file ########
		with open(title_file,'w') as f:
			for i,j in zip(eixo_x,eixo_y):
				f.write(str(i) + "," + str(j) + '\n')

			
def orbit_diagram(X_o=[0.1],N_steps=3000,N_end_points=10,func=[Logistic_equation],Parameters=[[2]],Parameter_choose=[0,0],Orbit_choose=0,Initial_parameter=2.8,Final_parameter=4,N_points=1000,plot=True,save=False,ylab=False,xlab=False,title_plot=False,export=False,Point_data=1,title_file=False,ret=False):
	
	""" Create orbit_diagram 
	X_o = initial value
	N_steps = number of X_n the program will calculate
	N_end_points = number of X_n will use to plot Orbit
	
	func = the function f(X_n) = X_{n+1}
	Parameters = array with all Parameters func has
	Parameter_choose = the position of Parameter that will chance
	Initial_parameter = the first value of Parameter
	Final_parameter = the final value of Parameter
	N_points = number of times the Parameter will chance

	plt = True to create plot 
	save = save the plot (option True) or just show (option False)
	ylab = name of ylabel
	xlab = name of xlabel
	title_plot = name of plot if you save

	export = export data
	title_file = name of file export

	Point_data = number of points per Parameter in file and return

	ret = True to return two arrays: 1 - Array with value of Parameter. 2- Array with x_n 
	"""
	if len(X_o) != len(func) & len(X_o) != len(Parameters):
		print ("Error")

	Data_x = []
	Data_y = []

	equatio, param = Parameter_choose

	Parametro_variable = np.linspace(Initial_parameter,Final_parameter,N_points)

	###### Calculate ######

	print ("Start_diagram_orbit")
	
	for i in Parametro_variable:
		Parameters[equatio][param] = i
		
		X_d = []
		for o in X_o:
			X_d.append([o])
		
		for j in range(N_steps):
			
			position = []
			for d in X_d:
				position.append(d[-1])
			

			for h in range(len(func)):
				X_d[h].append(func[h](position,Parameters[h]))

	
		Points_want = X_d[Orbit_choose][-N_end_points:]
		
		x_axes =[i for j in range(len(Points_want))]
		
		s = [10*1**1 for j in range(len(x_axes))]
	
		if plot:
			plt.scatter(x_axes,Points_want,color='black',s=s)
		
		for h in range(Point_data):
			point = -1 -1*h
			Data_x.append(x_axes[point])
			Data_y.append(Points_want[point])
		


	print ("Finish_diagram_orbit")


	######PLOT######
	
	if plot:
		if xlab == False:
			xlab = "Parameter"
		if ylab == False:
			ylab = r'$x_n$'
		plt.xlabel(xlab)
		plt.ylabel(ylab)
		if save==False:
			plt.show()
		else:
			if title_plot == False:
				title =  "Parametro_" +"In_" + str(Initial_parameter) + "_Fi_" + str(Final_parameter)+  "_.png" 
			else:
				if ".png" not in  title_plot:
					title_plot = title_plot + ".png" 
			plt.savefig(title)
	
	##### export ######

	if export:
		if title_file == False:
			title_file = "TESTE.txt"
		with open(title_file,'w') as p:
			for i,j in zip(Data_x,Data_y):
				p.write(str(i) + "," + str(j) + '\n')

	###### return #######
	if ret:
		return Data_x,Data_y
	
def pertubation(x_1,deltaR_0,deltaR_1):
	x = x_1 + deltaR_0	
	return x
	
def deltaR(x_0,x_1):
	return x_1 - x_0

def Lambda(deltaR_0,deltaR_1):
	return round(np.log(abs(deltaR_1/deltaR_0)))

def Lyap(X_o=[0.1,0.1],deltaR_0=[0.001,0.001],func=[Logistic_equation,Logistic_equation2],Parameters=[[2],[3]],Parameter_choose=[0,0],N_steps=6000,Initial_parameter=2.8,Final_parameter=4,N_points=4000,save=False,export=False,graf=all):


	""" Calculate Lyapunov exponents to one-dimensional maps
	
	X_o = initial value
	deltaR_0 = pertubation fo X_o
	N_steps = number of X_n that will be calculate
	
	func = the function f(X_n) = X_{n+1}
	Parameters = array with all Parameters func has
	Parameter_choose = the position of Parameter that will chance
	Initial_parameter = the first value of Parameter
	Final_parameter = the final value of Parameter
	N_points = number of times the Parameter will chance
	
	save = save the plot (option True) or just show (option False)
	export = export datas as .txt (option True)
	"""

	if len(X_o) != len(func) or len(X_o) != len(Parameters):
		print ("Error")

	Lyap_global = []
	for i in X_o:
		Lyap_global.append([])
	
	Parametro_variable = np.linspace(Initial_parameter,Final_parameter,N_points)
	
	print ("Start")

	for variable in Parametro_variable:

		Parameters[Parameter_choose[0]][Parameter_choose[1]] = variable
	

		X_o_pertubado = []
		for position_ini,pertuba_ini in zip(X_o,deltaR_0):
			X_o_pertubado.append(position_ini + pertuba_ini)

		x_npertubado = []
		x_pertubado = []
		Lyp_local = []
		delta = []

		
		
		for i in range(len(X_o)):
			x_npertubado.append([func[i](X_o,Parameters[i])])
			x_pertubado.append([func[i](X_o_pertubado,Parameters[i])])
			Lyp_local.append([])
			delta.append([])
		


		
		for i in range(N_steps):
			
			
			position_npertubado = []
			position_pertubado = []

			for z,h in zip(x_npertubado,x_pertubado):
				position_npertubado.append(z[-1])
				position_pertubado.append(h[-1])

		
			new_distante = 0
			old_distante = 0
			delta = []
			for l in range(len(X_o)):

				a = float(position_npertubado[l])
				b = float(position_pertubado[l])
				delta.append(deltaR(a,b))
				
				
				
				Lyp_local[l].append(Lambda(deltaR_0[l],delta[l]))
				r = delta[l]
				new_distante = r**2 + new_distante
				old_distante = deltaR_0[l]**2 + old_distante


			new_distante = new_distante**(0.5)
			old_distante = old_distante**(0.5)
			
			try:
				new = old_distante/new_distante
			except:
				new = 1


			for l in range(len(X_o)):
				if delta[l] < 0.01:
					position_pertubado[l] = position_npertubado[l] + delta[l]*(new)			
				else:
					position_pertubado[l] = position_npertubado[l]
			for l in range(len(X_o)):
				x_npertubado[l].append(func[l](position_npertubado,Parameters[l]))
				x_pertubado[l].append(func[l](position_pertubado,Parameters[l]))
		
			
			
		for i in range(len(Lyp_local)):
			Lyap_global[i].append(np.mean(Lyp_local[i]))

	print("Finish")	

	
	if graf == all:
		for i in Lyap_global:
			plt.plot(Parametro_variable,i)
			plt.axhline(y=0,color='black')
			plt.xlabel("Parametro")
			plt.ylabel(r'$\lambda$')

			if save == False:
				plt.show()
			
	
			else:
				title = "Lyap_grafi_" + "Delta_" + str(deltaR_0[0]) + "_.png"
				plt.savefig(title)
				plt.clf()
	
	else:
		
		plt.plot(Parametro_variable,Lyap_global[graf])
		plt.axhline(y=0,color='black')
		plt.xlabel("Parametro")
		plt.ylabel(r'$\lambda$')

		if save == False:
			plt.show()
			plt.clf()
	
		else:
			title = "Lyap_grafi_" + "Delta_" + str(deltaR_0[0]) + "_.png"
			plt.savefig(title)
			plt.clf()

	if export != False:
		arquivo = "Lyap_" + "Delta_" + str(deltaR_0[0]) + "_.txt"
		with open(arquivo,'w') as f:
			for i,j in zip(Parametro_variable,media_l):
				f.write(str(i) + "," + str(j) + "\n")
	

