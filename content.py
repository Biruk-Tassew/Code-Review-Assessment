# This is the count that will be increamented by increment_count function.
count = 0

# This function returns the product of the two numbers given
def multiply(x, y):
    return x * y

# This function will increament the global variable count
def increment_count():
    global count
    count += 1

increment_count()
print(count)
