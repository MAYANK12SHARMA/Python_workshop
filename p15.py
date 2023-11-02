# WAP to map to list in a dictonary 

list1 = ["data1","data2","data3","data4",]
list2 = [1,2,3,4]

n = {}
for i in list1:
    for j in list2:
        n[list1[i]] = list2[j]
    
print(n) 