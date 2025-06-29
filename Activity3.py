n=int(input("enter a number"))
sum=0
t=n
while t>0:
    digit=t%10
    sum=sum+digit**3
    t=t//10
if n==sum:
    print(" its an armstrong number")
else:
    print("Its not an armstrong number")