
sum_two_values=lambda first_value, second_value: first_value + second_value
print(sum_two_values(10,15))

multiply_two_values=lambda first_value, second_value: first_value * second_value
print(multiply_two_values(10,15))

def suma_three_values(values):
    return lambda first_value, second_value, third_value: first_value + second_value + third_value
print(suma_three_values(10)(10,15,20))