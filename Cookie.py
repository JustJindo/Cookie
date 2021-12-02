# Takes in a list and displays a numbered inventory of its elements.
def inventory(ingredient):
	if ingredient == []:
		print('Starve.')
	else:
		for i in range(len(ingredient)):
			print(f"{i + 1}. {ingredient[i]}")
			i += 1

# A master list of recipes in .txt files.
recipes = ['aglio.txt', 'stir_fry.txt', 'carbonara.txt', 'chicken_noodle.txt']
# A master list of ingredients.
ingredient_selection = ['onions', 'garlic', 'olive oil', 'eggs', 'chicken stock', 'chicken (breast/thighs)', 'pasta', 'vegetables', \
'bacon', 'parmesan', 'honey', 'soy sauce']
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