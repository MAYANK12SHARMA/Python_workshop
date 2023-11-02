# dictonary 
 
# Creating dictonary
student = {
    "name": "alice",
    "Age": 45,
    "grade": "A"
}

# printing the dictonary

print(student)

# accessing the value of dictonary 

name = student["name"]
age = student["Age"]
grade = student["grade"]

# modifing the element of dictonary

student["name"] = "RADHE"
student["Age"] = "48"
student["grade"] = "B"


# itreating through a dictonary 

for key,value in student.items():
    print(f"{key}:{value}")
    
    
# checking if a key is exist 

if "age" in student:
    print("Age exist in dictonary")

for value in student.values():
    print(f"{value}")
    

# dictonary comprehson

squares = {num: num**2 for num in range (1,6)}
print(squares)


# cube
cube = {num1: num1**3 for num1 in range(1,6)}
print(cube)


del student["grade"]
print(student)


grade = student.get("phone", "N/A")
print(grade)




