print('filter')
def is_even(x):
    return x % 2 == 0  # чётное число

nums = [1, 2, 3, 4, 5]
result = filter(is_even, nums)
print(list(result))  # [2, 4]

print('lambda')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = filter(lambda x: x % 2 != 0, nums)
print(list(result))  # [1, 3, 5]

print('1 task')

num = [10, 15, 20, 25,]
res = filter(lambda x: x % 5 == 0, num)
print(list(res))

print('2 task')

lak =  [3, 8, 12, 17, 21, 30, 35]
lok = filter(lambda x: x > 15 and x % 2 == 0, lak)
print(list(lok))

print('3 task')

lat = [5, 10, 15, 20, 25, 30, 35, 40]
lot = filter(lambda x: x % 5 == 0 and x < 30, lat )
print(list(lot))

print('4 task')

nums = [3, 9, 14, 18, 21, 25, 30, 33, 40]
nams = filter(lambda x: x % 3 == 0 and x % 5 != 0, nums)
print(list(nams))

print('5 task')

noms = [2, 7, 14, 21, 28, 35, 42]
nyms = filter(lambda x: x % 7 == 0 and x % 2 != 0, noms)
print(list(nyms))
