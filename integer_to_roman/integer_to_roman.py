def integer_to_roman(num):
    
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    
    rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

    s = ""

    for i in range(len(rom)):
        
        while num >= val[i]:
            
            s += rom[i]
            
            num -= val[i]
    
    return s


print(integer_to_roman(1994))
print(integer_to_roman(3999))
print(integer_to_roman(4000))