## higher order functions ##

from functools import reduce


def sum_one(values):
    return sum(values) + 1

def sum_five(values):
    return sum(values) + 5

def sum_two_values_and_one(fist_value, second_value):
    return fist_value + second_value + 1

print(sum_two_values_and_one(6, 2))
print(sum_two_values_and_one(10,20)+5)

## clasures ##

def sum_ten():
    def add(value):
        return value + 10
    return add
add_clasures = sum_ten()
print(add_clasures(5))
print((sum_ten()(5)))

## build-in higher order functions ##

numbers=(10,20,30,40,50)
#map
def multiply_by_two(value):
    return value * 2
print(list(map(multiply_by_two, numbers)))

## filter ##

def filter_greater_than_25(value):
    if value > 25:
        return True
    return False
print(list(filter(filter_greater_than_25, numbers)))

## reduce ##

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))
