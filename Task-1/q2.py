'''Q2. Create a class and create a func�on inside this class for selec�on sort of a list of strings. Input a
list of string similar to Q1 and call this sort func�on. Print the output. '''

class Sort:
    def selection(self,list):
        l=list
        n=len(l)
        
        for i in range(0,n-1):
            p=i
            for j in range(i+1,n):
                if (l[p]<l[j]):
                    p=j
                    
            l[p],l[j]=l[j],l[p]

        return(l)

if __name__=="__main__":
    L=[]
    n=int(input("Enter number of strings: "))
    for i in range(n):
        t=input("Enter string: ")
        L.append(t)

    sort = Sort()
    sorted=sort.selection(L)

    print (sorted)
