budget = float(input())

while budget >= 0:
    text = input()
    if text == 'End':
        print('You bought everything needed.')
        break
    else:
        purchase = float(text)
        budget -= purchase

if budget < 0:
    print('You went in overdraft!')
