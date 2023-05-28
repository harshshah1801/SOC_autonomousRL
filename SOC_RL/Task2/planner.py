#! /usr/bin/python3

import random,argparse,sys
parser = argparse.ArgumentParser()
import numpy as np

class MDP():
	def __init__(self,mdp_path,algorithm):
		with open(mdp_path,'r') as f:
			lines = f.readlines() # We read all the lines over here
			self.numStates = int(lines[0].strip().split()[-1])
			self.numActions = int(lines[1].strip().split()[-1])
			self.mdptype = lines[-2].strip().split()[-1]
			self.gamma = float(lines[-1].strip().split()[-1])
			self.tMatrix = np.zeros((self.numStates,self.numActions,self.numStates)) #Transition matrix
			self.rMatrix = np.zeros((self.numStates,self.numActions,self.numStates)) #Reward Matrix
			for line in lines[4:-2]:
				x = line.strip().split()
				s1 = int(x[1]);s2 = int(x[3]);p = x[5];r = x[4];a = int(x[2])
				self.tMatrix[s1,a,s2] = p
				self.rMatrix[s1,a,s2] = r
			#self.terminalStates = [int(x) for x in lines[2].strip().split()[1:]] # If the MDP has a terminal states then add a self loop with zero rewards to make them continuing
			#print(self.terminalStates)
			# if self.mdptype == "epsiodic":
			# 	for i in self.terminalStates:
			# 		for j in range(self.numActions):
			# 			self.tMatrix[i,j,i] = 1
			# 			self.rMatrix[i,j,i] = 0
						#this will make them behave like continuous mdp
		if algorithm=="vi":
			self.planner_vi()
		
	def BStar(self,V):
		Vnew = np.zeros(self.numStates)
		x = np.zeros(self.numStates)
		y = np.zeros(self.numActions)
		
		for s in range(self.numStates):
			for a in range(self.numActions):
				for s1 in range(self.numStates):
					x[s1] =  self.tMatrix[s,a,s1] * (self.rMatrix[s,a,s1] + self.gamma * V[s1])
				y[a] = np.sum(x) 
			Vnew[s] = np.max(y) #improvement
			x = np.zeros(self.numStates)
			y = np.zeros(self.numActions)
		
		return Vnew

	def planner_vi(self):
		Vold = np.zeros(self.numStates)
		epsilon = 1e-7
		Vnew = self.BStar(Vold)
		while np.sum(Vnew - Vold) > epsilon:
			Vold = Vnew
			Vnew = self.BStar(Vnew)
		Qpi = np.zeros(self.numActions)
		x = np.zeros(self.numStates)
		policy = np.zeros(self.numStates)
		for s in range(self.numStates):
			for a in range(self.numActions):
				for s1 in range(self.numStates):
					x[s1] =  self.tMatrix[s,a,s1] * (self.rMatrix[s,a,s1] + self.gamma * Vnew[s1])
				Qpi[a] = np.sum(x)
			policy[s] = np.argmax(Qpi) 
		for s in range(self.numStates):
			print(str(Vold[s]) + ' ' + str(int(policy[s])))


if __name__ == "__main__":
	parser.add_argument("--mdp")
	parser.add_argument("--algorithm",type=str,default="vi")
	
	
	args = parser.parse_args()
	#print(args)
	planner  = MDP(args.mdp,args.algorithm)