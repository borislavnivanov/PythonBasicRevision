limit = int(input())

for _ in range(0, limit):
    text = input()
    is_pure = True
    for letter in text:
        if letter == '_' or letter == '.' or letter == ',':
            print(f'{text} is not pure!')
            is_pure = False
            break
    if is_pure:
        print(f'{text} is pure.')
