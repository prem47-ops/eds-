l1=list(map(int,input("Enter the Numbers for List 1 : ").split()))
print(l1[::])    #For all
print(l1[2:9])   #for 2 to 9 index values
print(l1[2:9:2]) #for 2 to 9 index values by interval of 2s
l2=l1
a=len(l1)
print(a)
b=len(l2)
print(b)
c=l1+l2
print(c)
d=l1*2
print(d)
e=18 in l1
print(e)
f=18 not in l1
print(f)
g=max(l1)
print(g)
h=min(l1)
print(h)
i=sum(l1)
print(i)
j=all(l1)
print(j)
k=sorted(l1)
print(k)
l=list("SUJAL")
print(l)

print(l1.append(10))
print(l1.count(18))
print(l1.index(18))
print(l1.insert(4,100))
print(l1.pop(4))
print(l1.remove(18))
print(l1.reverse())
print(l1.sort())
