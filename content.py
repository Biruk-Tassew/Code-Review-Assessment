# function to calculate area of a circle
def calculateArea(radius):
    return 3.14 * radius ** 2

# function to divide numbers
def divide_numbers(a, b):
    return a / b

# This function returns the product of the two numbers given
def multiply(x, y):
    return x * y

# This function will increament the global variable count
def increment_count():
    global count
    count += 1

increment_count()
print(count)

# This function should verify if a given string with parenthesis id a valid one
def is_valid_parenthesis(s):
    dc = {
        '(': ')',
          "{": "}",
         '[': ']'

    }
    stack = []
    for i in s:
        if i in dc.keys(): stack.append(i)
        else:
            if len(stack) == 0:
                return False
            

            op = stack.pop()
            if dc[op] != i:
                return False
    if len(stack) != 0:
        return False
    
    return True
