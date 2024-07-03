numbers_list = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list comprehension
even_numbers_comprehension = [num for num in numbers_list if num % 2 == 0]

# lambda function
is_even = lambda num: num % 2 == 0
even_numbers_lambda = list(filter(is_even, numbers_list))

print("list comprehension results:", even_numbers_comprehension)
print("lambda function results:", even_numbers_lambda)
