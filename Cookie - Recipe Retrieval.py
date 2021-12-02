open_recipes = ['aglio.txt', 'carbonara.txt', 'chicknoodle.txt']

number = 1
for recipe in open_recipes:
	print(str(number) + '.', recipe[:-4])
	number += 1

choice = input()
with open(open_recipes[choice - 1], 'r') as f:
	print(f.read())