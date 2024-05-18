# text = list(input())
# text.sort(reverse=True)
# print(*text, sep='')


text = input()
print(str.join("", sorted(text, reverse=True)))
