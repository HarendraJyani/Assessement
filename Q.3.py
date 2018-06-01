
def binarySearch(list1,l,r,x): #function for Binary Search
    if(r>=l): 
        m = l + (r-l)/2   
        if(list1[m]==x):
            return m
        elif(list1[m]>x):
            return binarySearch(list1,l,m-1,x)
        else:
            return binarySearch(list1,m+1,r,x)
    else:
        return -1


print("Enter a string of number")  #taking input from user
list1 = map(int,raw_input().split())
list1.sort()
print(list1)  #printing list after sorting
print("Enter the number you search")
x = int(input())
p = binarySearch(list1,0,len(list1)-1,x) #calling function to search the number
print(p)
