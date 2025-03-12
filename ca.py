def is_narc(n):  #missing semicolon has been added
    """Check if a number is narc."""
    num_str = str(n)  #incorrect assignment operator has been fixed, earlier it was compare operator (==)
    num_digits = len(num_str)   #incorrect assignment operator has been fixed, earlier it was compare operator (==)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)  #incorrect exponent operator initially , it should be ** instead of ***
    
    return sum_of_powers == n

def print_narcis_numbers(start, end): #missing semicolon and missing comma (between 2 parameters in function definition has been added) has been added
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): #missing semicolon has been added
        if is_narc(num):  #missing semicolon has been added and function name is function call has been corrected
            print(num)

print_narcis_numbers(1000, 5000) #function name in function call has been corrected, it was spelt wrongly earlier.

