# Мое решение 
def square_digits(num):
    
    arr = []
    
    s = ""
    
    if num == 0:
        
        return num
    
    while num > 0:
        
        arr.append(num % 10)
        
        num //= 10    
    
    for i in range(len(arr)):
        
        s += str(arr[-(i + 1)] ** 2)
    
    return int(s)

#Нормальное решение
def ssquare_digitss(num):
    
    ret = ""
    
    for x in str(num):
        
        ret += str(int(x)**2)
    
    return int(ret)



print(square_digits(9119))
print(square_digits(0))