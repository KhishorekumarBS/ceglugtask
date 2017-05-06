#function
def add(p,q):
    return p+q
    
def subtract(p,q):
    return int(p)-int(q)

def multiply (p,q):
    return p*q

def divide (p,q):
    return float(p)/float(q)


print(add(int(input("Enter a number")),int(input("Enter a number"))))
print(subtract(float(input("Enter a number")),float(input("Enter a number"))))
print(multiply(int(input("Enter a number")),int(input("Enter a number"))))
print(float(divide(int(input("Enter a number")),int(input("Enter a number")))))

