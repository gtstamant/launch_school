# Pseudocode 

## 1. Define a function that returns the sum of two numbers
### 1.a casual pseudocode

Given two numbers.
- save the sum of the two numbers to a variable
- return the variable

### 1.b formal pseudocode

START

SET num1 and num 2 to numbers passed into function
SET sum = sum of num1 and num2
RETURN sum

END

## 2. Define a function that takes a list of strings and returns a string that is all those strings concatenated together
### 2.a casual pseudocode

Given a list of strings.
Initialize an empty string to variable "new string"

Iterate through the list of strings one by one
- add each string to "new string"

After iterating through the list, return the saved value

### 2.b formal pseudocode

START

Given a list of strings.

SET new_string = ''
SET iterator = 1

WHILE iterator <= length of list
    concatenate new_string with string at space iterator in list of strings
    iterator  = iterator + 1

RETURN new_string

END

## 3. Define a function that takes a list of integers and returns a new list with every other element from the original list starting with the first element, e.g. every_other([1, 4, 7, 2, 5]); => [1, 7, 5]
### 3.a casual pseudocode

Given a list of integers.
Initialize an empty list named "new list"

Iterate through the original list of ints one by one.
- if the iteration number is odd
    - add the number indexed at iterator to new list
- if the iteration number is even
    - do nothing

After iterating through the original list, return the new list

### 3.b formal pseudocode

START

Given a list of intergers.

SET new_list = empty list
SET iterator = 1

WHILE iterator <= length of int list
    IF iterator is odd
        ADD int indexed at iterator to new_list
    ELSE
        skip to the next iterator
    
    iterator = iterator + 1

RETURN new_list

END

## 4. Define a function that determines the index of the 3rd occurence of a given character in a string
### 4.a casual pseudocode

Given a character and a string.
Initialize counter variable at 0

Iterate through the string, character by character.
- For each iteration, check if the character matches the given character
- if the two characters match
    - increment the counter variable by 1
    - check whether the counter variable equals 3
    - if the counter variable equals 3
        - return the iteration number

- if the counter never reaches 3, return none

### 4.b formal pseudocde

START

Given a character "ch" and string "input_string"
SET counter = 0
SET iterator = 0

WHILE iterator <= length of input_string
    IF input_string character indexed at iterator is = to ch
        counter = counter + 1
        IF counter = 3
            RETURN iterator
    iterator = iterator + 1

RETURN NONE

END

## 5. Define a function that takes a list of two numbers and returns the result of merging the lists, e.g. merge([1, 2, 3], [4, 5, 6])
### 5.a casual pseudocode

Given two lists, list a and list b.
Initialize an empty new list.

Iterate through list a one member at a time
- add a number "new num" from list a to the new list
- add the number from list b with the same index as list a's "new num" to new list

Once finished iterating, return new list

### 5.b formal pseudocode

START

Given two lists of same length, list a and list b.
SET new_list = empty list

SET iterator = 0
WHILE iterator <= length of list a
    ADD number indexed at iterator in list a to new_list
    ADD number indexed at iterator in list b to new_list
    iterator = iterator + 1

RETURN new_list

END