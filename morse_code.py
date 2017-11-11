morse_dict = {
'A':'.-',
'B':'-...',
'C':'-.-.',
'D':'-..',
'E':'.',
'F':'..-.',
'G':'--.',
'H':'....',
'I':'..',
'J':'.---',
'K':'-.-',
'L':'.-..',
'M':'--',
'N':'-.',
'O':'---',
'P':'.--.',
'Q':'--.-',
'R':'.-.',
'S':'...',
'T':'-',
'U':'..-',
'V':'...-',
'W':'.--',
'X':'-..-',
'Y':'-.--',
'Z':'--..'
}

txt = raw_input()
morse_txt = ''
for ch in txt:
    morse_txt+=morse_dict[ch.upper()]+" "

arr=[]
for mch in morse_txt:
    if(mch!=' '):
        arr.append(mch)

space_positions = ""
for i in range(0,len(arr)-1):
    space_positions+="1"
space_positions=int(space_positions,2)

bin_table=[]
for position in range(0,space_positions+1):
    tmp=str(bin(position))[2:]
    while(len(tmp) != (len(arr)-1)):
        tmp = "0"+tmp
    bin_table.append(tmp)

possibilities={}
for code in bin_table:
    i=0
    new_morse_txt = arr[i]
    for bit in code:
        i+=1
        if(int(bit)==1):
            new_morse_txt+=" "+arr[i]
        else:
            new_morse_txt+=arr[i]
    new_txt=""
    for element in new_morse_txt.split(" "):
        flg=0
        for key,value in morse_dict.iteritems():
            if(value == element):
                new_txt+=key
                flg=0
                break
            else:
                flg=1
        if(flg==1):
            new_txt=""
            break

    if(len(new_txt)==len(txt)):
        possibilities[new_txt]=new_morse_txt

#print(possibilities)
print(len(possibilities))
