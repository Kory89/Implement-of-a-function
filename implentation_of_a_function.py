#-------------------------------------------------------------------------
# Implement a function that takes an array of integers and returns the 
# second largest element.
# Create a simple program that takes a string input and outputs the number
# of occurrences of each letter.
#-------------------------------------------------------------------------


def second_largest(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    # Return the second element of the sorted array
    return arr[1]

# Test the function
numbers = [4,2,9,7,5,1]
print(second_largest(numbers)) # Output = 7

def letter_count(string):
    return{letter:string.count(letter) for letter in set(string)}
string = "hello world"
print(letter_count(string)) # Output {'e': 1, 'r': 1, 'o': 2, 'w': 1, 'l': 3, ' ': 1, 'd': 1, 'h': 1}