#!/usr/bin/python

import sys

def rock_paper_scissors(n):
	actions = ['rock', 'paper', 'scissors']	
	tot_combos = []

	def helper(togo=n, result=[]):
		if togo < 1:
			tot_combos.append(result)
			return tot_combos

		for action in actions:
			helper(togo - 1, result + [action])

	helper()
	return tot_combos

print(rock_paper_scissors(2))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')