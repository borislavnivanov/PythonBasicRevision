cups = 0

while True:
    text = input()
    if text == "END" or text == "End" or text == 'end':
        break

    if text == 'coding' or text == 'dog' or text == 'cat' or text == 'movie':
        cups += 1
    elif text == 'CODING' or text == 'DOG' or text == 'CAT' or text == 'MOVIE':
        cups += 2

if cups <= 5:
    print(cups)
else:
    print('You need extra sleep')
