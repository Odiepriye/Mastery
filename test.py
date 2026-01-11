import array

def add(a):
    global x
    print(a + x)

x = 5
add(10)
# y = x
# print(id(x))  # Shows memory address
# print(id(y))  # Shows memory address
# print(id(x) == id(y))  # Are they the same object in memory
# print(5/0)