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
    print("Number 1 is bigger than Number 2.")