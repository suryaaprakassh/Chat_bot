with open('test.txt','r') as f:
    ff=f.read()
    l,c,w=1,0,1
    for i in ff:
        if i=='\r' or i=='\n': l+=1
        if i==' ': w+=1
        if i!=' ': c+=1
    print("No words:%d\nNo lines:%d\nNo characters:%d"%(w,l,c))
