MyListK=["key1","key2","key3"]
MyListV=["Value1","Value2","Value3"]
count =len(MyListK)
print(range(count))

listas=[]
for i in range(count):
    sublista=[]
    for j in range(count):
        sublista.append((i,j))
    listas.append(sublista)
  
#for item in items:
#    print(item)
print(listas)

