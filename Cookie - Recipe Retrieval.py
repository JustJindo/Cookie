def inventory(ingredient):
	if ingredient == []:
		print('Starve.')
	else:
		for i in range(len(ingredient)):
			print(f"{i + 1}. {ingredient[i]}")
			i += 1

open_recipes = ['aglio.txt', 'carbonara.txt', 'chicknoodle.txt']

number = 1
for recipe in open_recipes:
	print(str(number) + '.', recipe[:-4])
	number += 1

inventory(open_recipes)

choice = input()
with open(open_recipes[choice - 1], 'r') as f:
	print(f.read())