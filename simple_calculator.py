def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b
def calculator():
    print(  "1- add\n"
            "2-sub\n"
            "3-mul\n"
            "4-divide")
    num1=float(input("Enter number 1: "))
    num2=float(input("Enter number 2: "))
    choice=input("enter your choice: ")
    if choice=='1':
        print(sum(num1,num2))
    elif choice=='2':
        print(sub(num1,num2))
    elif choice=='3':
        print(mul(num1,num2))
    elif choice=='4':
        print(divide(num1,num2))
calculator()
    
 