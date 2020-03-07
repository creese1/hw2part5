def getNum():
    needNum = True
    while needNum:
        value = int(input("Enter a number: "))
        if (value > 0):
            needNum = False
    return value


num1 = getNum()
num2 = getNum()

if(num1 > num2):
    print("num 1 is bigger than num 2")
elif(num2 > num1):
    print("num 2 is bigger than num 1")