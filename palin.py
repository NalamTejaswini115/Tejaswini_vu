def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]

# Input from the user
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
