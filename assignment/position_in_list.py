a=list(map(int,input("Give No.: ").split()))
key=int(input("Enter the Key : "))
c=1
l=len(a)
for i in range(l):
    if(key==a[i]):
        print(i)
        c=1
        break
    else:
        c=0
if(c==0):
    print("Not Found")
