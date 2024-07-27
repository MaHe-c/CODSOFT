
print("Simple Calculator : ")
print("--------------------")

def initial():  
    print("\nEnter the calculation you want :)\na.Addition \nb.Subtraction \nc.Multiplication \nd.Division \ne.Modulus")
    choice = input()
    return choice

value = initial()

def main_fun():
    num1 = int(input("\nEnter number 1 : "))
    num2 = int(input("\nEnter number 2 : "))

    def addition(num1,num2):
        print("\nAddition : ",(num1+num2))

    def subtraction(num1,num2):
        print("\nSubtraction : ",(num1-num2))

    def multiplition(num1,num2):
        print("\nMultiplition : ",(num1*num2))

    def division(num1,num2):
        print("\nDivision : ",(num1/num2))

    def modulus(num1,num2):
        print("\nModulus : ",(num1%num2))

    if value=="a" or value=="A":
        addition(num1,num2)

    elif value=="b" or value=="B":
        subtraction(num1,num2)

    elif value=="c" or value=="C":
        multiplition(num1,num2)

    elif value=="d" or value=="D":
        division(num1,num2)

    elif value=="e" or value=="E":
        modulus(num1,num2)

    else:
        print("Invalid input :)")

main_fun()

while True:
    another_round = int(input("\n\nYou want to calculate another mathematical operation  -  press 1..!"))

    if another_round==1:
        initial()
        main_fun()
    else:
        break