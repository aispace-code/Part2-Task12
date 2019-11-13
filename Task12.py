a = input("Write any word: ")
if a.count('b') == 1:
    print(-1)
elif a.count('b') < 1:
    print(-2)
else:
    print(a.find('b', a.find('b') + 1))
