#! /usr/bin/python3

import random,argparse,sys
parser = argparse.ArgumentParser()
import numpy as np

class Encoder():
	def __init__(self,grid_path):
		with open(grid_path, 'r') as f:
			self.lines = f.readlines()
			self.side = len(self.lines)+2 # gives the side of the square grid with a additonal layer of 0 around it
			self.numActions = 4
			self.numStates = 0
			self.start = [0,0]
			self.end = [0,0]
			self.gridMatrix = np.zeros([self.side,self.side],dtype=int)
			#print(lines)
			#print(lines[1].strip().split())
			
	def construct_mdp(self):
		writefile = open("grid10.txt",'w')
		actions = ['1','2','3','0']
		for x in range(1,self.side-1):
			line = list(map(int,self.lines[x-1].strip().split()))
			#print(line[0])
			for y in range(1,self.side-1):
				if(line[y-1]==2):
					self.numStates+=1
					self.gridMatrix[x,y]=self.numStates
					self.start = self.numStates
				elif(line[y-1]==3):
					self.numStates+=1
					self.gridMatrix[x,y]=self.numStates
					self.end = self.numStates
				elif(line[y-1]==0):
					self.numStates+=1
					self.gridMatrix[x,y]=self.numStates
		#print(self.gridMatrix)
		self.numStates+=1
		writefile.write("numStates "+str(self.numStates)+"\n")
		writefile.write("numActions "+str(self.numActions)+"\n")
		writefile.write("start "+str(self.start)+"\n")
		writefile.write("end "+str(self.end)+"\n")
		for x in range(1,self.side-1):
			for y in range(1,self.side-1):
				if self.gridMatrix[x,y]!=0:
					#print(self.gridMatrix[x,y])
					if self.gridMatrix[x,y]==self.end:
						continue
					else:
						k=np.sign(self.gridMatrix[x+1,y])+np.sign(self.gridMatrix[x-1,y])+np.sign(self.gridMatrix[x,y+1])+np.sign(self.gridMatrix[x,y-1])
						if self.gridMatrix[x,y+1]==self.end:
							writefile.write("transition "+str(self.gridMatrix[x,y])+' '+'2'+' '+str(self.gridMatrix[x,y+1])+' '+'1000'+' '+'1'+"\n")
						elif self.gridMatrix[x,y-1]==self.end:
							writefile.write("transition "+str(self.gridMatrix[x,y])+' '+'0'+' '+str(self.gridMatrix[x,y-1])+' '+'1000'+' '+'1'+"\n")
						elif self.gridMatrix[x+1,y]==self.end:
							writefile.write("transition "+str(self.gridMatrix[x,y])+' '+'3'+' '+str(self.gridMatrix[x+1,y])+' '+'1000'+' '+'1'+"\n")
						elif self.gridMatrix[x-1,y]==self.end:
							writefile.write("transition "+str(self.gridMatrix[x,y])+' '+'1'+' '+str(self.gridMatrix[x-1,y])+' '+'1000'+' '+'1'+"\n")
						else:
							if self.gridMatrix[x,y+1]!=0:
								writefile.write("transition "+str(self.gridMatrix[x,y])+' '+'2'+' '+str(self.gridMatrix[x,y+1])+' '+'0'+' '+str(1/k)+"\n")
							if self.gridMatrix[x,y-1]!=0:
								writefile.write("transition "+str(self.gridMatrix[x,y])+' '+'0'+' '+str(self.gridMatrix[x,y-1])+' '+'0'+' '+str(1/k)+"\n")
							if self.gridMatrix[x+1,y]!=0:
								writefile.write("transition "+str(self.gridMatrix[x,y])+' '+'3'+' '+str(self.gridMatrix[x+1,y])+' '+'0'+' '+str(1/k)+"\n")
							if self.gridMatrix[x-1,y]!=0:
								writefile.write("transition "+str(self.gridMatrix[x,y])+' '+'1'+' '+str(self.gridMatrix[x-1,y])+' '+'0'+' '+str(1/k)+"\n")
		writefile.write("mdptype continuing \n")
		writefile.write("discount  0.99 \n")




				




		

									










if __name__ == "__main__":
	parser.add_argument("--grid")	
	args = parser.parse_args()
	#print(args)
	grid_mdp=Encoder(args.grid)
	grid_mdp.construct_mdp()
