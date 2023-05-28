#! /usr/bin/python3

import random,argparse,sys
parser = argparse.ArgumentParser()
import numpy as np

class Decoder():
	def __init__(self,grid_path,mdp_path):
		with open(mdp_path,'r') as f:
			lines
	






if __name__ == "__main__":
	parser.add_argument("--grid")
	parser.add_argument("--value_policy")
	args = parser.parse_args()
	#print(args)
	grid_decoder=Decoder(args.grid,args.value_policy)
	grid_mdp.construct_ans()