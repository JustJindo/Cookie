# Takes in a list and displays a numbered inventory of its elements.
def inventory(ingredient):
	if ingredient == []:
		print('I got nothing, sorry.')
	else:
		for i in range(len(ingredient)):
			print(f"{i + 1}. {ingredient[i]}")
			i += 1

# A master list of recipes in .txt files.
recipes = ['aglio.txt', 'stir_fry.txt', 'carbonara.txt', 'chicken_noodle.txt']
names = ['Pasta Aglio e Olio', 'Stir Fry', 'Pasta Carbonara', 'Chicken Noodle Soup']
# A master list of ingredients.
ingredient_selection = ['onions', 'garlic', 'olive oil', 'eggs', 'stock', 'chicken', 'pasta', 'vegetables', \
'bacon', 'parmesan', 'soy sauce']
# A list to store ingredients on hand.
ingredients = []

# Display instructions for how to use Cookie.
print("""Of these ingredients, which ones do you currently have?
________________________________________________

If you have an ingredient, type the number associated with it ('1' for '1. [ingredient]').
If you're done listing ingredients, type 'Done'.
________________________________________________
""")

# Call on 'inventory' to list ingredients.
inventory(ingredient_selection)
print('')

# Record known ingredients here.
known = []

# Take in and store ingredients on hand.
check = ''
# Parameter only serves to enable while loop.
while check != 'Done':
	check = input("... ")
	# This check breaks the loop.
	if check == 'Done':
		break
	else:
		check = int(check)
		if check not in known:
			known.append(check)
			item = ingredient_selection[check - 1]
			ingredients.append(item)

# Store cookable recipes in here.
cookable = []
# Use this list to record shared ingredients.
shared = []

# Takes in two lists and determines if they're the same.
# Our lists are recipe ingredients and shared ingredients.
def compare(first, second):
	first.sort()
	second.sort()
	if first == second:
		return 'Equal'
	if first != second:
		return 'Unequal'

# Giant lists of recipe ingredients (same order as recipes list).
cookbook = [['garlic', 'olive oil', 'pasta'], ['olive oil', 'stock', 'chicken', 'vegetables', 'soy sauce'], \
['eggs', 'pasta', 'bacon', 'parmesan'], ['onions', 'garlic', 'olive oil', 'stock', 'chicken', 'vegetables']]

# Go through each ingredient list in cookbook.
for entry in cookbook:
	# Reset the shared list for every iteration.
	shared = []
	# Retrieve the index of the ingredient list.
	reference = cookbook.index(entry)
	# Use the index to find the associated recipe name.
	recipe = names[reference]
	# Go through each ingredient in the ingredient list.
	for requirement in entry:
		# If the ingredient is in the user's list of ingredients, add it to shared list.
		if requirement in ingredients:
			shared.append(requirement)
	# Compare recipe's ingredient list with shared list.
	cookability = compare(entry, shared)
	if cookability == 'Equal':
		cookable.append(recipe)

print("""________________________________________________

These are the recipes you can make with what you have.
To choose a recipe, type the number associated with it ('1' for '1. [recipe]').
________________________________________________
""")

# Call on 'inventory' to list cookable recipes.
inventory(cookable)
print('')

# Display user's choice of recipe .txt file.
choice = int(input("... "))
print("________________________________________________\n")
with open(recipes[choice - 1], 'r') as f:
	print(f.read())