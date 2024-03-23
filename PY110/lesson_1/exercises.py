'''
input: string
output: list, each element a string

rules:
    explicit requirements:
        - Return every palindromic substring in list
        - Must include all palindromes, including
        those contained in longer palindromes
        - Palindromes should be case sensitive, abBA is not a palindrome
    
    implicit requirements:
        - an empty string should return an empty list
        - A string with no palindromes returns empty list

data structure:
    - list (desired output)

algorithim:
    - Declare a result variable and initialize to an empty list
    - Create a list called substr_lst that contains all substrings
    of the input str that are > 1 char long
    - Loop through substr_lst
    - Check if each substr is a palindrome
    - If yes, append to result list
    - Return result list

Substring generating procedure: 
    - initialize results and set to empty list
    - loop through each character of string
        - for each character, excluding the final one:
            - loop through chars from index char + 1 to end of string
            - append slice of string from char to loop position to results
    - return results

Palindrome checking procedure:
    - If str len == 0, return True
    - If str len == 1, return True
    - Check if str[0] and str[-1] are equal
        - if yes, call palindrome check on str[1:-1]
        - if no, return false

    (Or simply - if str = str in reverse, return true)
''' 

def substrings(string):
    result = []
    start_index = 0

    while start_index < len(string) - 1:
        num_chars = 2

        while num_chars <= len(string) - start_index:
            substring = string[start_index:start_index + num_chars]
            result.append(substring)
            num_chars += 1
        
        start_index += 1
    
    return result

# def is_palindrome(string):
#     reversed_string = string[::-1]
#     return string == reversed_string

def is_palindrome(string):
    if len(string) < 2:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False

def palindrome_substrings(string):
    result = []
    substrings_list = substrings(string)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)
    
    return result

print(palindrome_substrings("supercalifragilisticexpialidocious"))