budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = (price_flour * 1.25) / 4
price_bread = price_flour + price_eggs + price_milk

loaves_made = 0
colored_eggs_collected = 0

while budget >= price_bread:
    budget -= price_bread
    loaves_made += 1
    colored_eggs_collected += 3
    if loaves_made % 3 == 0:
        colored_eggs_collected -= loaves_made - 2

print(f'You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs_collected} eggs and {budget:.2f}BGN left.')
