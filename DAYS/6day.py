def say_hello():
    print('Привет!')
say_hello()

def good_job(name):
    print(f'great, {name}')
good_job('Kyaz')
good_job('Aybiyke')
good_job('Alikhan')

def number(a, b):
    return a - b
print(number(5, 3))

def rectangle_area(width, height):
    return width * height
print(rectangle_area(5, 10))

def is_even(number):
    return number % 2 == 0
print(is_even(4))
print(is_even(5))

def power(number, degree=2):
    return number ** degree
print(power(3))
print(power(3, 3))

