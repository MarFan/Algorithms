#!/usr/bin/python

import argparse

def find_max_profit(prices):
	min = None # Get the min price
	max = None # Get the max price

	profit = None

	for i in range(0, len(prices)):
		for j in range(i, len(prices)):
			if i != j:
				if profit == None or -prices[i] + prices[j] > profit:
					profit = -prices[i] + prices[j]

	# for i in range(len(prices)-1,0,-1):
	# 	for j in range(i-1, 0, -1):
	# 		if i != j:
				#print(prices[i], prices[j], prices[i] - prices[j])
	# 			if profit == None or prices[i] - prices[j] > profit:
	# 				profit = prices[i] - prices[j]
	# # for i in range(len(prices)):	
	# 	for j in range(len(prices)):
	# 		# print(i, j, prices[j], prices[i], (prices[j]- prices[i]))
	# 		if mr_profit == 0 or prices[j] - prices[i] > mr_profit:
	# 			mr_profit = prices[j] - prices[i]
	# 			# print(prices[j], prices[i], (prices[j]- prices[i]))
		
		# if min == 0 or prices[i] < min:
		# 	min = prices[i]
		# if max == 0 or prices[i] > max:
		# 	max = prices[i]
		# print(min, max)
	return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))