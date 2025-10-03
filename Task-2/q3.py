
# Improve the hashing implemented in Q2. When inserting a new number in the sublist, insert it so that the sublist is always sorted. Do not sort the list after insertion. (Hint: When inserting a new number, find the correct index where the number should be inserted in the sublist using binary search.). Input numbers similar to Q2 and print the hash table. 

n=int(input("Enter number of elements: "))
L=[]
for i in range(n):
    L.append(int(input("Enter value:")))



def doHash(l):
    hashedList = [[] for _ in range(2)]
    for i in l:
        k = i % 10
        if k<2:
            l = 0
            h = len(hashedList[k]) - 1

            while l <= h:
                mid = (l + h) // 2
                if hashedList[k][mid] < i:
                    l = mid + 1
                else:
                    h = mid - 1 
            

            
            hashedList[k].insert(l, i)
            
    return hashedList
print(doHash(L))


while True:
    c=int(input("Enter additional number: "))
    L.append(c)
    print(doHash(L))


