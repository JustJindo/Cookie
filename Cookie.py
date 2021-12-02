ingredient_selection = ['1. onions', '2. garlic', '3. olive oil', '4. eggs', '5. chicken stock']
ingredients = []

print("""Of these ingredients, which ones do you currently have?
________________________________________________

If you have an ingredient, type the number associated with it ('1' for onions).
If you're done listing ingredients, type 'Done'.
________________________________________________
""")
for ingredient in ingredient_selection:
	print(ingredient)