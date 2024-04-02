def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

# print(leading_substrings('abc'))      # ['a', 'ab', 'abc']
# print(leading_substrings('a'))        # ['a']
# print(leading_substrings('xyzzy')) 

def substrings(string):
    substrings = []
    for idx in range(len(string)):
        substrings.append(leading_substrings(string[idx:]))
    
    return substrings

def substrings_c(string):
    return [leading_substrings(string[idx:])
            for idx in range(len(string))]

def is_palindrome(string):
    return string == string[::-1]

def palindromes(string):
    return [substring for lst in substrings_c(string)
            for substring in lst
            if is_palindrome(substring)
            if len(substring) > 1]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True
print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True