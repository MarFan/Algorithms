#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
	tots_batch = None

	for key in recipe:
		if key not in ingredients:
			tots_batch = 0 # missing an ingredient, can make the dish
			return tots_batch	
		elif key in ingredients and tots_batch == None or ingredients[key] // recipe[key] < tots_batch:
				tots_batch = ingredients[key] // recipe[key]

	return tots_batch

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))