"""
## Problem:

Write a function that implements a stack-and-register based
programming language that has a number of commands.

Input: A program represented by a 'string'
Output: Depends on the command:
- n: place a value, n, in the register without modifying the stack
- PUSH: push the register value onto the stack, do not modify the register
- ADD: Pop a value from the stack and add it to register value
- SUB: Pop a value from the stack and subtract it from the register
- MULT: Pop a value from the stack and multiply it by the register
- DIV: Pop a value from the stack and divide the register value by it
storign the integer result back in the register
- REMAINDER: Pop a val from the stck, divide the register by it, store
the integer remainder in the register
- POP: Remove the topmost item from the stack, place it in the register
- PRINT: Print the register value

Explicit rules:
- All operations are integer operations (DIV, remainder)
- Function may assume all arguments are valid programs

Implicit rules:
- Programs are ordered from left to right
- Each command will be separated by a space

Questions:
- How are programs structured?
    - How will the string be organized?
- Do we need to worry about negative numbers for % operation?

## Examples:
- See problem description

## Data structure
- Stack implemented as a list

## Algorithm:
- Not really an algorithm problem
- Just need to loop through the commands

Implementation notes:
- Match/case statement, I think

"""

def minilang(program):
    register = 0
    stack = []

    for command in program.split():
        if command.isdigit() or command[0] == '-':
            register = int(command)
            continue
        try:
            match command:
                case 'PUSH':
                    stack.append(register)
                case 'ADD':
                    register += stack.pop()
                case 'SUB':
                    register -= stack.pop()
                case 'MULT':
                    register *= stack.pop()
                case 'DIV':
                    register //= stack.pop()
                case 'REMAINDER':
                    register %= stack.pop()
                case 'POP':
                    register = stack.pop()
                case 'PRINT':
                    print(register)
                case _:
                    print('Bad command')
                    return TypeError
        except IndexError:
            print('Empty stack')
            return IndexError

# minilang('PRINT')
# # 0

# minilang('3 MULT PRINT')
# # 15

# minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # # 5
# # # 3
# # # 8

# minilang('5 PUSH POP PRINT')
# # # 5

# minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # # 5
# # # 10
# # # 4
# # # 7

# minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # # 6

# minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # # 12

# minilang('-3 PUSH 5 SUB PRINT')
# # 8

minilang('6 PUSH')