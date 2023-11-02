# WAP a python program to iterate over dictonary using for loops.

dict = {
    "x":10,
    "y":20,
    "z":30
}


# add the keys of dictonary 
for key,value in dict.items():
    print(f"{key}:{value}")
 
   
# check the key exist or not.


a = input("enter the key : ")

if a in dict.keys():
    print("it exist")
else:
    print("nikal yaha se")
    
