# List example
li = [1, 2, 3, 4, 5]
li.append(6)
print(li)  # Output: [1, 2, 3, 4, 5, 6]

# Dictionary example
_dict1 = {'a': 1, 'b': 2, 'c': 3}
_dict1['d'] = 4
print(_dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Immutable data types: tuple, string, frozenset
# They create a new object in memory when modified rather than changing the original object.
tuple_data = (1, 2, 3, 4, 5)
print(tuple_data)  # Output: (1, 2, 3, 4, 5)

string_data = 'Hello, World!'
print(string_data)  # Output: Hello, World!

set_data = frozenset([1, 2, 3, 4, 5])
print(set_data)  # Output: frozenset({1, 2, 3, 4, 5})

# For loop example
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Lambda function example
# A lambda function is an anonymous function with any number of arguments and only one expression.
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Docstring example
def example_function():
    """This is an example function that demonstrates the use of a docstring."""
    return "Docstring example"

print(example_function())

# Exception handling example
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")


