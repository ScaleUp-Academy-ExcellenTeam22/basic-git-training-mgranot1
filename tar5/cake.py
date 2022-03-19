
def get_recipe_price(d, optionals=[], **ingredients):
    sum_all = 0
    for ingredient in ingredients:
        price_100_gr = d[ingredient]
        price = price_100_gr / 100
        amount = ingredients.get(ingredient)
        sum_all += amount * price
    return sum_all


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
# 44
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
# 54
print(get_recipe_price({}))
#  0
