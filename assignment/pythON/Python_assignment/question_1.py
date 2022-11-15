num=int(input())
lst=[]
for i in range(num):
    i=input()
    lst.append(i)
sort=sorted(lst)
file=sort.pop(1)
sort.insert(0,file)
print(sort)
