### Reverse the given number


number=int(input("Enter a number= "))
rev=0
while(number>0):
    rem=number%10
    rev=(rev*10)+rem
    number=number//10

print("Reverse of  a number: ",rev)
