string_1 = input()
string_2 = input()
variants = list(string_1)

for let in range(len(string_1)):
    if variants[let] != string_2[let]:
        variants[let] = string_2[let]
        print(''.join(variants))
