# def staggered_case(string):
#     new_str = ''

#     for idx in range(len(string)):
#         if idx % 2 == 0:
#             new_str += string[idx].upper()
#         else:
#             new_str += string[idx].lower()

#     return new_str

# def staggered_case(s):
#     result = []
#     for idx, char in enumerate(s):
#         if idx % 2 == 0:
#             result.append(char.upper())
#         else:
#             result.append(char.lower())
#     return ''.join(result)

# def staggered_case(string):
#     case_lst = [string[idx].upper() if idx % 2 == 0 else string[idx].lower()
#                 for idx in range(len(string))]
#     return ''.join(case_lst)

def staggered_case(s):
    return ''.join([char.upper() if idx % 2 == 0 else char.lower()
                    for idx, char in enumerate(s)])

print(staggered_case('I Love Launch School!'))        # "I LoVe lAuNcH ScHoOl!"
print(staggered_case('ALL_CAPS'))                     # "AlL_CaPs"
print(staggered_case('ignore 77 the 4444 numbers'))   # "IgNoRe 77 ThE 4444 nUmBeRs"