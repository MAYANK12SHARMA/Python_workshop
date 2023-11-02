# sets
# ? .remove = removing element from the set
# ! .discard = safely remove an element even if iti doesn't exist
my_set = {1,2,3,45,"Mayank sharma"}
my_set.add("radhe radhe")
my_set.remove(3)
print(my_set)


#  union 
m = {1,2,3,4,5,6,7}
a = my_set.union(m)
print(a)

#  intersection
b= my_set.intersection(m)
print(b)

# difference 
c = my_set.difference(m)
print(c)
