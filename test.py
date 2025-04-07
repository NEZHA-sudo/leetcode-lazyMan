left = 600000000 
right = 2147483647

ret = left
for i in range(left, right+1):
    ret &= i
    print(i, ret)
    if ret==0:
        break
    
