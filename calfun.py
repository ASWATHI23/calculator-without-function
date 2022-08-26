print("enter the number1:")
num1=int(input())
print("enter the number2:")
num2=int(input())
print("these are the operators you can use:")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
result=0
operator=input("these are the operator u can use(1,2,3,4,5):")
def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def mul(num1,num2):
    return(num1*num2)
def div(num1,num2):
    return(num1//num2)
def mod(num1,num2):
    return(num1%num2)
if operator=="1":
    result=add(num1,num2)
    print(result)
if operator=="2":
    result=sub(num1,num2)
    print(result)
if operator=="3":
    result=mul(num1,num2)
    print(result)
if operator=="4":
    result=div(num1,num2)
    print(result)
if operator=="5":
    result=mod(num1,num2)
    print(result)