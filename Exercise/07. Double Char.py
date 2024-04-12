while True:
    text = input()
    if text == 'End':
        break
    if text == 'SoftUni':
        continue

    for i in range(0, len(text)):
        if i == len(text) - 1:
            print(f'{text[i] * 2}')
        else:
            print(f'{text[i] * 2}', end='')
