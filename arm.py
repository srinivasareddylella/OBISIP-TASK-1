def armstrong_number(num):
    n=str(num)
    sum=0
    for i in n:
        sum += int(i)**len(n)

        
    return sum
    

n=int(input("Enter a number: "))
if armstrong_number(n) == n:    
    print(f"{n} is an armstrong number")        
else:
    print(f"{n} is not an armstrong number")



