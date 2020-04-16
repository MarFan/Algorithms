#!/usr/bin/python

import argparse

def find_max_profit(prices):
	min = None # Get the min price
	max = None # Get the max price

	profit = None

	for i in range(len(prices)-1,0,-1):
		for j in range(i-1, 0, -1):
			if i != j:
				#print(prices[i], prices[j], prices[i] - prices[j])
				if profit == None or prices[i] - prices[j] > profit:
					profit = prices[i] - prices[j]
	# for i in range(len(prices)):	
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

print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([100, 90, 80, 50, 20, 10]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))
print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))