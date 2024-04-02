# def reverse_string(s):
#     for char in s:
#         s = char + s
#     return s

# print(reverse_string("hello"))

# def reverse_string(s):
#     result = ''
#     for idx in range(len(s)):
#         result += s[-(idx + 1)]
#     return result

# def reverse_string(s):
#     reverse = ''
#     for char in s:
#         reverse = char + reverse
#     return reverse

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))