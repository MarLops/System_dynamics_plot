
import numpy as np
import matplotlib.pyplot as plt


def bisection_2_order(Coefi,error_want = 0.00000000001,i_max=100000,mod=False):
	
	#Resolve second order polynomial using bisection method
	#Coefi = array with coefficients.
	#error_want = int. 
	#mod = True to return only the module of root (in case of complex number) 



	a,b,c = Coefi

	def function(x,a=a,b=b,c=c):
		f  = a*x**2 + b*x + c
		return f

	def sign(x,a=a,b=b,c=c):
		s = function(x)
		
		if s < 0.0:
			return (-1)
			
		if s > 0.0:
			return (1)
		
		if s == 0:
			return (0)

	if len(Coefi) != 3.0:
		return ['ERROR','ERROR']
		 

	Delta = b**2 - 4*c*a
	Delta_p = round(Delta,5)
	
	if Delta_p < 0.0 and mod==True:
		return [c,c]
	if Delta_p< 0.0 and mod==False:
		return ["not root","not root"]

	if Delta_p == 0:
		x_1 = -b/(2*a)
		x_2 = -b/(2*a)
		return [x_1,x_2]
	

	x_start_1 = float(-b/(2*a))
	x_start_2 = x_start_1 - 5

	while sign(x_start_1) == sign(x_start_2):
		x_start_2 = x_start_2 - 2


	x_start_1 = x_start_2 + 5
	media = float((x_start_2 + x_start_1)/2)
	error = function(media)
	i = 0
	continue_calcule = True



	while continue_calcule:	
		

		if error < error_want and error > -error_want :
			x_1 = media
			x_2 = c/(a*x_1)
			res = False
			return (x_1,x_2)
			break

		if sign(x=media) != sign(x=x_start_1):
			x_start_2 = media
		
		else:
			x_start_1 = media

		media = float((x_start_2 + x_start_1)/2)
		error = function(media)

		i = i + 1
		if i > i_max:
			
			return ["not value","not value"]

def bisection_3_order_module(Coefi,error_want = 0.000000000001,i_max=100000,first_step=0.000001,mod=False):
	
	#Resolve third order polynomial using bisection method
	#Coefi = array with coefficients.
	#error_want = int. 
	#mod = True to return only the module of root (in case of complex number) 


	a,b,c,d = Coefi
	a = float(a)
	b = float(b)
	c = float(c)
	d = float(d)
	def function(x,a=a,b=b,c=c,d=d):
		f  = a*x**3 + b*x**2 + c*x + d
		return f

	def sign(x,a=a,b=b,c=c,d=d):
		s = function(x)
		
		if s < 0.0:
			return (-1)
			
		if s > 0.0:
			return (1)
		
		if s == 0:
			return (0)

	if len(Coefi) != 4:
		return 0 

	Delta = 18*a*b*c*d - 4*d*b**3 + (b**2)*(c**2) - 4*a*c**3 - 27*(a**2)*d**2 

	


	x_start_1,x_start_11 = bisection_2_order(Coefi=[3*a,2*b,c],mod=mod)
	x_start_2_1 = x_start_1 - 1
	x_start_2_2 = x_start_1 + 1

	
	while sign(x_start_1) == sign(x_start_2_1) and sign(x_start_1) == sign(x_start_2_2):
		x_start_2_1 = x_start_2_1 - first_step
		x_start_2_2 = x_start_2_2 + first_step
	
	if sign(x_start_1) != sign(x_start_2_1):
		x_start_2 = x_start_2_1
	else:
		x_start_2 = x_start_2_2

	
	
	media = float((x_start_2 + x_start_2 - 1)/2)
	error = function(media)
	i = 0
	continue_calcule = True



	while continue_calcule:	
		

		if error < error_want and error > -error_want :
			x_1 = media
			continue_calcule = False
			break

		if sign(x=media) != sign(x=x_start_1):
			x_start_2 = media
		
		else:
			x_start_1 = media

		media = float((x_start_2 + x_start_1)/2)
		error = function(media)

		i = i + 1
		if i > i_max:
			print(i_max)
			x_1 = media
			continue_calcule=False
			break


	
	if Delta < 0:
		D = -d/x_1
		return [x_1,D,D]
	else:
		a_2 = float(a)
		c_2 = float(-d/x_1)
		b_2  = float(b + x_1*a)
	
		Coe = [a_2,b_2,c_2]
		
		x_2,x_3 = bisection_2_order(Coefi = Coe)

		return [x_1,x_2,x_3]

def matrix_dete_poli(Matrix):
		
	#Return the coefficient of characteristic polynomial (3X3 Matrix)

	A_1,B_1,C_1 = Matrix[0]
	A_2,B_2,C_2 = Matrix[1]
	A_3,B_3,C_3 = Matrix[2]
	a = -1
	b = A_1 + B_2 + C_3
	c = -1*C_3*(A_1 + B_2) -1*A_1*B_2 + A_3*C_1 + B_3*C_2 + A_2*B_1
	d =  A_1*B_2*C_3 + B_1*C_2*A_3 + C_1*A_2*B_3 -1*B_2*A_3*C_1 -1*B_3*C_2*A_1 -1*C_3*A_2*B_1	
	return [a,b,c,d]

def eigvalues_bisection_method(Matrix,mod = False):

	#Calculate eigvalues of Matrix 3x3 . In caso complex number, need change mod to return module of complex number

	Coefi = matrix_dete_poli(Matrix)
	x_1,x_2,x_3 = bisection_3_order_module(Coefi=Coefi)
	return [x_1,x_2,x_3]

def main_example_bisection_second_order():

	#Resolvi 3x^2 + 6x - 18
	Coefi = [3,6,-18]
	x_1,x_2 = bisection_2_order(Coefi=Coefi)
	print(x_1,x_2)

def main_example_bisection_third_order():

	#Resolvi x^3 + 60x^2 - 316x - 3840 
	Coefi = [1,60,-316,-3840]
	x_1,x_2,x_3 = bisection_3_order_module(Coefi=Coefi)
	print(x_1,x_2,x_3)



