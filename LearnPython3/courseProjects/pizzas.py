# Your code below:
toppings = ["pepperoni", "pineeapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")
pizza_and_prices = [[prices[0], toppings[0]], [prices[1], toppings[1]], [prices[2], toppings[2]], [prices[3], toppings[3]], [prices[4], toppings[4]], [prices[5], toppings[5]], [prices[6], toppings[6]]]
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()
pizza_and_prices.insert(2, [2.5, "peppers"])
#print(priciest_pizza)
print(pizza_and_prices)
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
