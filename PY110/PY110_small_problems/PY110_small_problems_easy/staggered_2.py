def staggered_case(s):
    result = []
    upper_flag = True

    for char in s:
        if char.isalpha():
            if upper_flag == True:
                result.append(char.upper())
            else:
                result.append(char.lower())
            upper_flag = not upper_flag
        else:
            result.append(char)
    
    return ''.join(result)

print(staggered_case("I Love Launch School!") == "I lOvE lAuNcH sChOoL!")
print(staggered_case("ALL CAPS") == "AlL cApS")
print(staggered_case("ignore 77 the 444 numbers") == "IgNoRe 77 ThE 444 nUmBeRs")