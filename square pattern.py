num=int(input("enter the number for the pattern:-"))
i=0
while i<num:
    if i==0:
        j=0
        while j < num:
            print(j+1,end=" ")
            j+=1
        print()
    elif i==num-1:
        j=0
        while j<num:
            print(num-j,end=" ")
            j+=1
    else:
        print(i+1,end=" ")
        j=0
        while j<num-2:
            print(" ",end=" ")
            j+=1
        print(num-i)
    i+=1
