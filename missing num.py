## prime numbers of N digits

num=int(input("Enter the initial value "))
value=int(input("Enter the value of num "))
prime=[]
for num1 in range(num,100):
    for num2 in range(2,num1):
        if(num1%num2==0):
            break
    else:
        prime.append(num1)
    if len(prime)==value:
        break
print("prime numbers are: ",prime[:])
  
