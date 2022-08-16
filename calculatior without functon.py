print("zodiac calculator")
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
operator=input("please choose an option from these (1,2,3,4,5):")
if operator=="1":
    result=num1+num2
    print("The result of a addition of ",num1,"and",num2,"is",result)
if operator=="2":
    if num1<num2:
        print("cannot substract because the first number is less than second number")
    else:
        result=num1-num2
        print("The result of substraction of",num1,"and", num2,"is",result)
if operator=="3":
    if num2==0 or num1==0:
        print("cannot multiply by zero")
    else:
        result=num1*num2
        print("The result of multiplication of",num1,"and",num2,"is",result)
if operator=="4":
    if num2==0:
        print("cannot divide by zero")
    else:
        result=num1//num2
        print("The result of division of",num1,"and",num2,"is",result)
if operator=="5":
    if num2==0:
        print("cannot modulo by zero")
    else:
        result=num1%num2
        print("The result of modulus of",num1,"and",num2,"is",result)