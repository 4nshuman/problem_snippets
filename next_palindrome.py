num = raw_input()

if(len(num)%2 == 0):
    chnge = int(num[len(num)/2])+1
    new_num=""
    for i in range(0,len(num)):
        if (i==len(num)/2 or i==(len(num)/2)-1):
            new_num+= str(chnge)
        else:
            new_num+= num[i]
else:
    chnge = int(num[len(num)/2])+1
    new_num=""
    for i in range(0,len(num)):
        if (i==len(num)/2):
            new_num+= str(chnge)
        else:
            new_num+= num[i]

print(new_num)
