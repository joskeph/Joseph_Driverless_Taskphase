#Create a class and create a function inside this class for binary search in a list of strings. Input a list similar to Q1, and use the sort function from the class created in Q2 to sort the list. Input a string, and perform binary search on this string.
from q2 import Sort

class Search:
    def binary(self,L,f):
        l=L
        n=len(l)
        low=0
        high=n-1

        while high>=low:
            mid=(high+low)//2
            if (l[mid]==f):
                return mid
            elif l[mid]<f:
                low=mid+1
            else:
                high=mid-1

        

        return -1 
    


L=[]
n=int(input("Enter number of strings: "))
for i in range(n):
    t=input("Enter string: ")
    L.append(t)

sort=Sort()
sorted=sort.selection(L)
print (sorted)
s=input("Enter string to find: ")
search=Search()
index=search.binary(L,s)

if(index==-1):
    print("Element not found")
else:
    print(f"Element found at index {index}")