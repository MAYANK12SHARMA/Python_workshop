# #  function
# x = 20
# def my_fun():
#     # x = 10   # x is a local variable
#     print(x)
    
# my_fun()

x = 10

def modify():
    global x    # using global keyword
    x = 20

modify()

print(x)
