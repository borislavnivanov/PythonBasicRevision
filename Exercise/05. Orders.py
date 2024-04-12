orders = int(input())
total = 0

for _ in range(0, orders):
    coffee_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if coffee_price <= 0 or coffee_price > 100:
        continue

    if days <= 0 or days > 31:
        continue

    if capsules_per_day <= 0 or capsules_per_day > 2000:
        continue

    order_amount = (capsules_per_day * days) * coffee_price
    total += order_amount
    print(f'The price for the coffee is: ${order_amount:.2f}')

print(f'Total: ${total:.2f}')
