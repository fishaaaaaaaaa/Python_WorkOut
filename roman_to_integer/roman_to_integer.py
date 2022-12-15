def roman_to_integer(s):
    
    dc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    n = dc[s[-1]]
    
    for i in range(len(s) - 2, -1, -1):
        
        if dc[s[i]] >= dc[s[i + 1]]:
            
            n += dc[s[i]]
        
        else:
            
            n -= dc[s[i]] 
    
    return n


print(roman_to_integer("MCMXCIV"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("IV"))