def PrintArray(x,y,arr):
    k = 0
    l = 0
    while(k < x and l < y):
        for i in range(l,y):
            print arr[k][i],
        k+=1
        for i in range(k,x):
            print arr[i][y-1],
        y-=1
        if(k<x):
            for i in range(y-1,(l-1),-1):
                print arr[x-1][i],
            x-=1
        if(l < y):
            for i in range(x-1,k-1,-1):
                print arr[i][l],
            l+=1
arr = [[1,2,3],[4,5,6],[7,8,9]]
x = 3
y = 3
PrintArray(x,y,arr)
                       
