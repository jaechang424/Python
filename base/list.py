import random

lst = [10, 20, '안녕', True]
lst.append('추가')

# 1
for i in lst: print(lst[random.randint(0, len(lst) - 1)], end=' ')
print()

# 2
arr = [[1, 2], [3, 4], [5, 6]]
for (a, b) in arr:
    print(a + b, end=" ")
print()

# 3
t1 = [1, 2]
t2 = t1
t2[0] = 10
print("t2: " + str(t2))
print("t1: " + str(t1))

# 4
result = [i * 3 for i in range(0, 11) if i % 2 == 0]
print(result)

