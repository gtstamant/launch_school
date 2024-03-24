## Problem ##

Inputs: a list of strings
Outputs: a new list of string sorted based on the highest number of adjacent consonants


Explicit rules:
- If two strings contain the same highest number of adjacent consonants, they should retain their original order
- Consonants are considered adjacent if they are next to each other or if there is a space between two consonant in adjacent words
    - In other words, spaces are not considered in determining whether consonants are adjacent

Implicit rules:
- Strings may contain single or multiple words delimited by spaces
- Strings may not be empty
- Strings may have no adjacent consonants
- Strings should be sorted in descending order
- Case is not relevant
- Single consonants in a string do not affect sort order in comparison to strings with no consonants. Only adjacent consonants affect sort order.

Questions:
- Is the set of letters limited to the standard 26 of the Roman script?
- How do we handle inputs that fall outside of the alphabetic range?
- What do we do with an empty list as input?
- Do strings always contain multiple words?
    - Can strings e a single word?
    - Can strings be empty?
- Should the strings be sorted in ascending or descending order (what is the sort?)
- Is case important?

## Examples and Test Cases ##

- Sorted from highest number of adjacent consonants to lowest number
- A 'word' is a set of characters delimited by a space
- Strings can be one or multiple words
- No non-Roman characters expected
- Unknown whether strings can be empty
- Unknown whether case matters

<!-- my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa'] -->

## Data Structure ##

List as basic data structure
- Dict to count number of adjacent consonants per string?

## Algorithm ##

High level:

1. Consider each string one at a time, counting the number of adjacent consonants in each
2. Generate a new list of strings in descending order based on the number of adjacent consonants
3. Return new list of strings

More detail:

1.  Start with a list of strings as input

2. Consider each word in the string
    - determine how many adjacent consonants (sub-process)
    - store string name and number of adjacent consonants in 'results' data structure

3. Sort 'results' data structure in descending order (sub-process 2) and store in new list 'sorted strings'

4. Return 'sorted strings'

**Subprocess 1** 

Determine number of adjacent consonants:
Input: a string
Output: an integer representing a count of the highest number of adjacent consonants in the string

Remove spaces/whitespace from input string
Set 'current counter' equal to 0
Set 'highest adjacent' equal to 'current counter'
Cycle through string characters
    - if char is a consonant
        - add 1 to 'current counter'
        - if 'current counter' is greater than 'highest adj'
            - 'highest adj' = "current counter'
    - if char is a vowel
        - set 'current counter' equal to 0
return 'highest adj' if 'highest adj' is greater than 1

Test subprocess:

Input: 'algorithm'

counter = 0
highest_adj = counter

a > counter = 0
l > counter = 1, highest = 1
g > couner = 2, highest = 2
o > counter = 0, highest = 2
r > counter = 1, highest = 2
i > counter = 0, highest = 2
t > counter = 1, highest = 2
h > counter = 2, highest = 2
m > counter = 3, highest = 3

Further subprocess:

Check consonant:
- Check not vowel

**Subprocess 2**

Sort result structure:
1. Take data structure with strings and number adjacent consonants as input
2. Initialize an empty list 'sorted list'
3. Sort list:
    - Save the first item in the data structure to variable 'highest'
    - Walk through the data structure, comparing each consonant number to the consonant number of 'highest'
    - if a consonant number is higher than 'highest', save the item to 'highest'
        - NOT equal to, though
    - Once at the end of the list, append 'highest' to 'sorted list'
    - Delete 'highest' from data structure
    - Continue until all items have been deleted from data structure is 
4. Return list
