#Learn open hashing. Implement a hash table using 2D lists. Input a number n, and input nnumber of integers and create a list of integers. All numbers where (num % 10 == 0) should be placed in the 1st sublist (index 0). Similarly, all numbers where (num % 10 == 1) should be placed in the 2nd sublist (index 1). Print the hash table.


n=int(input("Enter number of elements: "))
L=[]
for i in range(n):
    L.append(int(input("Enter value:")))


def doHash(l):
    hashedList=[[]for _ in range(10)]
    for i in l:
        key= i%10
        hashedList[key].append(i)

    return hashedList

print(doHash(L))




# h(k,i)=h'(k)+i % m
# h(k)=k % m

# size = 10

# class Hashing():
#     def __init__(self):
#         self.size = 10
#         self.hashTable = [[]]*10
#     def hashing(self,list):
#         n=len(list)
#         for i in range(n):
#             hV=list[i]%10
#             self.hashTable[hV].append(list[i])
        
#         return self.hashTable
