text = input()
positions = list()
for i in range(len(text)):
    if str.isupper(text[i]):
        positions.append(i)
print(positions)
