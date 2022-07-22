def sumofdigit(n):
    res=0
    rem=0
    while n>0:
      rem=n%10
      res=res+rem*rem
      n=n//10
    return res
num=int(input("enter the number"))
result=num
while result!=1 and result!=4:
    result=sumofdigit(result)
if result==1:
    print(num,"is a happy number")
else:
    print(num,"is not a happy number")

