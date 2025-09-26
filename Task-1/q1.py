'''Input an integer n. Input n number of strings and create a list of strings. Create a dictonary
where key is an alphabet, and value is the number of �mes this alphabet is present in all the strings
in the list (Not case sensitve, i.e count both uppercase and lowercase).
For example: If the list is : ["Formula", "Manipal"], then the dic�onary output would look something
like: {'f': 1, 'o':1, 'a': 3 ...'''

L= []
n=int(input("Enter number of elements: "))
F={}
for i in range(n):
    t=input("Enter string: ")
    L.append(t.lower())
for i in range(n):
    for j in L[i]:
        F[j]=F.get(j,0)
        F[j]+=1

for i in F.keys():
    print(i,F[i])


