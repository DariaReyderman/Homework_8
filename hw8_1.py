# a
list_1: list[int] = []
for i in range(0, 100):
    list_1.append(i + 1)
print(list_1)
# b
print('b')
print(f'the first number is {[list_1[0]]}')
# c
print('c')
print(f'the last number is {[list_1[-1]]}')
# d
print('d')
print(f'total entered numbers {len(list_1)}')
# e
print('e')
list_2: list[int] = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list_2[:10])
# f
print('f')
print(list_1[-21:])
# g
print('g')
print(list_1[:17])
# h
print('h')
print(list_2[::-1])
# i
print('i')
print(list_1[1:100:2])
# j
print('j')
print(list_1[2:100:3])
# k
print('k')
print(list_1[6:100:7])
# l
print('l')
print(list_1[9:100:10])
# m
print('m')
print(list_1[98:64:-3])
# n
print('n')
list_2.insert(5, 999)
print(list_2)
# o
print('o')
list_2.append(100)
print(list_2)
list_2.pop(11)
print(list_2)
