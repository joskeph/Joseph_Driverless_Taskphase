import csv

F=open("names.csv","w",newline='')
W=csv.writer(F)
W.writerow(["Number","Name"])
n=int(input("Enter number of rows: "))
for i in range(n):
    t1=int(input("Enter number: "))
    t2=input("Enter name: ")
    W.writerow([t1,t2])
F.close()

F=open("names.csv","r+",newline="")
R=csv.reader(F)
L=[]
next(F)
for i in R:
    L.append([int(i[0]),i[1]])
print("origignal :",L)
#sort

for i in range(0,n):
    p=i
    for j in range(i+1,n):
        if L[j][0]<L[p][0]:
            p=j
    L[i],L[p]=L[p],L[i]
print("sorted: ",L)

#remove odd rows
t=[]
for i in range(n):
    if L[i][0]%2==0:
        t.append(L[i])
L=t
print("no odd: ",L)

F.seek(0)
W=csv.writer(F)
W.writerows(L)

F.close()

Names="".join(((i[1]).strip()for i in L))
print("strings:",Names)

sL=[]
for i in Names:
    sL.append(i)
for i in range(len(Names)):
    p=i
    for j in range(i+1,len(Names)):
        if ord(sL[j])<ord(sL[p]):
            p=j
    sL[p],sL[i]=sL[i],sL[p]
print("sorted string",sL)
min=ord(sL[1])-ord(sL[0])
x=0
for i in range(1,len(sL)-1):
    if ord(sL[i+1])-ord(sL[i])<min:
        min=ord(sL[i+1])-ord(sL[i])
        x=i
print(f"minimum ascii difference in characters is {min}")