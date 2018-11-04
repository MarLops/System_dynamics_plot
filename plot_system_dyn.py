# Gráficos cobweb e diagrama de orbita

import numpy as np
import matplotlib.pyplot as plt

def Logistica(X,Parameters):
	R = Parameters[0]
	return R*X*(1-X)

def tend(X,Parameters):
	R = Parameters[0]
	return R*(min(X,1-X))

def reta(Inicial,Final,Point_continuos):
	X = np.linspace(0,1,Point_continuos)
	return  X

def cobweb(X_o=0.1,N_steps=500,func=Logistica,Parameters = [2],Inicial_continuo=0,Final_continuo=1,N_steps_continuo = 20000,save=False):

	""" Create cobweb 
	X_o = initial value
	N_steps = number of X_n the program will calculate
	
	func = the function f(X_n) = X_{n+1}
	Parameters = array with all Parameters func has
	Inicial_continuo = first point to construct the continuos function
	Final_continuo = final point to construct the continuos function
	
	save = save the plot (option True) or just show (option False)
	"""

	X_d = [X_o]
	for i in range(N_steps):
		X_d.append(func(X_d[i],Parameters))

	X_c = np.linspace(Inicial_continuo,Final_continuo,2000)
	Y_c = []
	for j in X_c:
		Y_c.append(func(j,Parameters))

	X_r = reta(Inicial_continuo,Final_continuo,2000)
	
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


	plt.plot(X_c,Y_c,color='black')
	plt.plot(X_r,X_r,color='blue')
	plt.plot(eixo_x,eixo_y,'-ro')
	plt.ylabel(r'$X_{n+1}$')
	plt.xlabel(r'$X_n$')
	plt.title("Cobweb")
	
	if save == False:
		plt.show()
	else:
		j = ""
		for i in Parameters:
			j = j + "_" + str(i)
		title = str(func).split()[1] + "_Parameters_" + j + "_.png" 
		plt.savefig(title)

def orbita_diagrama(X_o=0.1,N_steps=3000,N_end_points=1000,func=Logistica,Parameters=[2],Parameter_choose=0,Inicial_parameter=2.8,Final_parameter=4,N_points=2000,save=False):
	
	""" Create orbita_diagrama 
	X_o = initial value
	N_steps = number of X_n the program will calculate
	N_end_points = number of X_n will use to plot orbita
	
	func = the function f(X_n) = X_{n+1}
	Parameters = array with all Parameters func has
	Parameter_choose = the position of Parameter that will chance
	Inicial_parameter = the first value of Parameter
	Final_parameter = the final value of Parameter
	N_points = number of times the Parameter will chance

	save = save the plot (option True) or just show (option False)
	"""

	Parametro_variavel = np.linspace(Inicial_parameter,Final_parameter,N_points)

	for i in Parametro_variavel:
		Parameters[Parameter_choose] = i
		
		X_d = [X_o]
		for j in range(N_steps):
			X_d.append(func(X_d[j],Parameters))

		Pontos_desejado = X_d[-N_end_points:]
		R =[i for j in range(len(Pontos_desejado))]
		s = [1*1**1 for j in range(len(Pontos_desejado))]
		plt.scatter(R,Pontos_desejado,color='black',s=s)

	plt.xlabel(r'Paramêtro')
	plt.ylabel(r'$X_n$')
	
	if save==False:
		plt.show()
	else:
		title = "Parametro_" +"In_" + str(Inicial_parameter) + "_Fi_" + str(Final_parameter)+ "_.png" 
		plt.savefig(title)

def mudanca(x_1,deltaR_0,deltaR_1):
	x = x_1 + deltaR_0	
	return x
	
def deltaR(x_0,x_1):
	return x_1 - x_0

def labda(deltaR_0,deltaR_1):
	return np.log(abs(deltaR_1/deltaR_0))

def Lyap(X_o=0.1,deltaR_0=0.0000001,func=Logistica,Parameters=[2],Parameter_choose=0,N_steps=4000,Inicial_parameter=2,Final_parameter=4,N_points=2000,save=False,export=False):


	""" Calculate Lyapunov exponents to one-dimensional maps
	
	X_o = initial value
	deltaR_0 = pertubation fo X_o
	N_steps = number of X_n that will be calculate
	
	func = the function f(X_n) = X_{n+1}
	Parameters = array with all Parameters func has
	Parameter_choose = the position of Parameter that will chance
	Inicial_parameter = the first value of Parameter
	Final_parameter = the final value of Parameter
	N_points = number of times the Parameter will chance
	
	save = save the plot (option True) or just show (option False)
	export = export datas as .txt (option True)
	"""

	media_l = []
	
	Parametro_variavel = np.linspace(Inicial_parameter,Final_parameter,N_points)

	for j in Parametro_variavel:

		Parameters[Parameter_choose] = j

		X_o_p  = X_o + deltaR_0

		x_n_n = []
		x_n_p = []
		x_n_n.append(func(X_o,Parameters))
		x_n_p.append(func(X_o_p,Parameters))
		
		l = []
		delta = []
	
	
		for i in range(N_steps):

			x_p = x_n_n[i] + deltaR_0
			delta.append(deltaR(x_n_n[i],x_n_p[i]))
			l.append(labda(deltaR_0,delta[i]))

			x_n_n.append(func(x_n_n[i],Parameters))
			x_n_p.append(func(x_p,Parameters))


	
		media_l.append(np.mean(l))
		

	plt.plot(Parametro_variavel,media_l)
	plt.axhline(y=0,color='black')
	plt.xlabel("Parametro")
	plt.ylabel(r'$\lambda$')

	if save == False:
		plt.show()

	else:
		title = "Lyap_grafi_" + "Delta_" + str(deltaR_0) + "_.png"
		plt.savefig(title)

	if export != False:
		arquivo = "Lyap_" + "Delta_" + str(deltaR_0) + "_.txt"
		with open(arquivo,'w') as f:
			for i,j in zip(Parametro_variavel,media_l):
				f.write(str(i) + "," + str(j) + "\n")




