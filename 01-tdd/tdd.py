# Write a function that takes in a string and returns its length
def check_length(our_string=""):
    return len(our_string)

# Write a funtion that takes in a list of integers and returns the product of every item in list
def check_product(our_list=[]):
    product = 1

    if len(our_list) == 0:
        return 0
    else:
        for num in our_list:
            product *= num 
    
    return product


# Write a function that takes in a string and returns a new string with only the letters in the starting letter and all odd indicies
def odd_string(our_string):
    result = []
    if len(our_string) == 0:
        return ""
    
    result.append(our_string[0])

    for letter in range(1,len(our_string), 2):
           result.append(our_string[letter])

    result = "".join(result)
    return result
