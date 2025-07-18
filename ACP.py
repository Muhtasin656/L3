n=int(input("enter a number"))
if n==0:
    print("number of  digits are 1")
else:
    if n>0:
        n=abs(n)
    count=0
    while n>0:
        n//=10
        count+=1
    print(f"The number of digits is {count}")