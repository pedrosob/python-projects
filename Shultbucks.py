# The Starbucks Simulator

# Bruno's Menu
espresso_price = 0.50
flat_white_price = 1.50
macchiato_price = 1.25
nutella_crossiant_price = 1.75

print("Welcome to Starbucks in 1980! What would you like today?" )
drink = input("Espresso,Flat White, or Macchiato? ")
nutella_crossiant = input("Do you want to try our Nutella Crossiant?,It's really good! (Yes/No) ")
if drink == "Espresso":
    price = espresso_price
elif drink == "flat white":
    price = flat_white_price
else:
    price = macchiato_price
if nutella_crossiant == "Yes":
    price += nutella_crossiant_price

sales_tax = 0.05
total_price = price * (1 + sales_tax)

print("Here's the", drink)
if nutella_crossiant == "Yes":
    print("You're really going to love this Nutella Crossiant!")
else:
    print("You know, you're really missing out on the crossiant bud.")
print("Alright you owe us $%.2f" % total_price)
