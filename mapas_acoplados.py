import numpy as np

def map_aco_1D(System,Function_time,Paramets_time,Function_space,Parats_space,Sequence=1):

	if Sequence == 1:

		System_space = []		
		for i in range(len(System)):	
			System_space.append(Equation_space(i,System,Function_space,Parats_space))
		System = System_space

		System_time = []
		for i in System:
			System_time.append(Equation_time(i,Function_time,Paramets_time))
		System = System_time
		
	if Sequence == 2:

		System_time = []
		for i in System:
			System_time.append(Equation_time(i,Function_time,Paramets_time))
		
		System = System_time

		System_space = []		
		for i in range(len(System)):	
			System_space.append(Equation_space(i,System,Function_space,Parats_space))
		System = System_space
	
	return System

def Equation_time(variables,Function_time,Paramets_time):

	Position = []
	for i in variables:
		Position.append(i)

	Position_f = []
	for j in range(len(Function_time)):
		x = Function_time[j](Position,Paramets_time)
		Position_f.append(x)

	return Position_f

def Equation_space(space_po,System,Function_space,Parats_space):

	Position_f = []
	for i in range(len(Function_space)):
		Position_f.append(Function_space[i](space_po,System,Parats_space))


	return Position_f

def Create_system_1D(N_space,Position_center,Conditional_ncenter,Conditional_center):
	System = []

	for i in range(N_space):
		if i != Position_center-1:
			lattice = []
			for i in Conditional_ncenter:
				lattice.append(i)
			System.append(lattice)
		else:
			lattice = []
			for i in Conditional_center:
				lattice.append(i)
			System.append(lattice)

	return System

def Create_Paramets_space_1D(N_space,Values_nborder,Values_border):
	par = [0.1]
	for i in range(N_space):
		if i == 0 or i == N_space-1:
			par.append(Values_border)
		else:
			par.append(Values_nborder)

	return par

def map_aco_2D(System,Function_time,Paramets_time,Function_space,Parats_space,Sequence=1):

	if Sequence == 1:

		System_space = []		
		for j in range(len(System)):
			System_line_space = []
			for i in range(len(System[j])):	
				System_line_space.append(Equation_space([i,j],System,Function_space,Parats_space))
			System_space.append(System_line_space)

		System = System_space


		System_time = []
		for j in range(len(System)):
			System_line_time = []
			for i in System:
				System_line_time.append(Equation_time(i,Function_time,Paramets_time))
		
			System_time.append(System_line_time)
		System = System_time

		
	if Sequence == 2:


		System_time = []
		for j in range(len(System)):
			System_line_time = []
			for i in System:
				System_line_time.append(Equation_time(i,Function_time,Paramets_time))
		
			System_time.append(System_line_time)
		System = System_time

		System_space = []		
		for j in range(len(System)):
			System_line_space = []
			for i in range(len(System[j])):	
				System_line_space.append(Equation_space([i,j],System,Function_space,Parats_space))
			System_space.append(System_line_space)

		System = System_space
		
	return System

def Create_system_2D(N_space,Position_center,Conditional_ncenter,Conditional_center):
	System = []

	for i in range(N_space[0]):
		System_line = []
		for j in range(N_space[1]):
			if i == Position_center[0] - 1 and j == Position_center[1] - 1:
				lattice = []
				for i in Conditional_ncenter:
					lattice.append(i)
				System_line.append(lattice)
			else:
				lattice = []
				for i in Conditional_center:
					lattice.append(i)
				System_line.append(lattice)

		System.append(System_line)

	return System

def Create_Paramets_space_2D(N_space,Values_nborder,Values_border):
	par = [0.1]
	for i in range(N_space[0]):
		par_line = []
		for j in range(N_space[1]):
			if i == 0 or i == N_space[0]-1:
				par_line.append(Values_border)
			else:
				if j == 0 or j == N_space[1] - 1:
					par_line.append(Values_border)
				else:
					par_line.append(Values_nborder)
		par.append(par_line)
	return par

