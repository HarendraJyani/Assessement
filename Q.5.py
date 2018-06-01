n = int(input()) #reading input from user
while (n != 1):  #while loop until 1 is reached
    if(n%2==0):  #If n is even 
        n = n/2
    else:         # if n is odd
        n = 3*n + 1
    print(n)      # printing value of n in each step
