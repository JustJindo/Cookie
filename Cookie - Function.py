fridge = ['onions', 'potatoes']

def inventory(ingredient):
	if ingredient == []:
		print('Starve.')
	else:
		for i in range(len(ingredient)):
			print(f"{i + 1}. {ingredient[i]}")
			i += 1

inventory(fridge)