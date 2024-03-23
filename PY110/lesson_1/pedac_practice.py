# 1. Start with
#     - 'num blocks' is equal to input
#     - Set 'squares' to empty list
#     - Set 'layer' equal to 1

# 2. While sum of 'squares' is less than 'num blocks'
#     - Append 'layer' * 'layer' to 'squares'
#     - Increment 'layer' by plus one

# 3. Check:
#     - if sum of 'squares' is equal to 'num blocks'
#         - return 0
#     - if sum of 'squares' does not equal 'num blocks'
#         - return 'num blocks' - (sum of 'squares' excluding the final member)

def calculate_leftover_blocks(num_blocks):
    squares = []
    layer = 1

    while sum(squares) < num_blocks:
        squares.append(layer ** 2)
        layer += 1
    
    if sum(squares) == num_blocks:
        return 0
    else:
        remainder = num_blocks - sum(squares[:-1])
        return remainder

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True