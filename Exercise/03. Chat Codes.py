length = int(input())

for _ in range(0, length):
    code = int(input())

    if code == 86:
        print('How are you?')
    elif code == 88:
        print('Hello')
    elif code > 88:
        print('Bye.')
    elif code < 88:
        print('GREAT!')
