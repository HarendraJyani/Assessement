list1 = map(int,raw_input().split())
valid = 1
for i in range(len(list1)-2):
    if(list1[i] + list1[i+1] != list1[i+2]):
        valid = 0
if(valid==1):
    print("Valid additive sequence")
else:
    print("Invalid Sequence")
    
    
