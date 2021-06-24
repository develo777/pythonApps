_myList=[12,10,8,4,2,1]

flag=False
while flag==False:
    flag=True
    for i in range(len(_myList)-1): 
        if _myList[i] > _myList[i+1]:
            aux=_myList[i]
            _myList[i]=_myList[i+1]
            _myList[i+1]=aux
            flag=False

print(_myList)




    
