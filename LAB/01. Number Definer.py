number: float = float(input())
result: str = ''
if number < 0:
    if number > -1:
        result += 'small '
    elif number < -1000000:
        result += 'large '
    result += 'negative'
elif number > 0:
    if number < 1:
        result += 'small '
    elif number > 1000000:
        result += 'large '
    result += 'positive'
else:
    result = 'zero'

print(result)
