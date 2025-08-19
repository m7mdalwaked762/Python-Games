logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

calculation ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
while True:
    print(logo)
    num1 =int(input("What is the first number?:"))
    operation =input("""+
-
*
/
Pick an operation:""")
    num2=int(input("What is the next number?:"))

    if operation=="+" :
        result =calculation["+"](num1,num2)
        print(f"{num1} + {num2} = {result}")
    elif operation=="-":
        result = calculation["-"](num1,num2)
        print(f"{num1} - {num2} = {result}")
    elif operation=="*":
        result = calculation["*"](num1,num2)
        print(f"{num1} * {num2} = {result}")
    elif operation=="/":
        result = calculation["/"](num1,num2)
        print(f"{num1} * {num2} = {result}")
    else:
        print("invalid operation !")

    UserChoice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if UserChoice=="y":
        while True:
            num1 = result
            operation = input("""+
-
*
/
Pick an operation:""")
            num2 = int(input("What is the next number?:"))

            if operation == "+":
                result = calculation["+"](num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif operation == "-":
                result = calculation["-"](num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif operation == "*":
                result = calculation["*"](num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif operation == "/":
                result = calculation["/"](num1, num2)
                print(f"{num1} * {num2} = {result}")
            else:
                print("invalid operation !")

            UserChoice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
            if UserChoice == "n":
                break
    if UserChoice=="n":
        continue
    else:
        print("\n"*1000)
        continue
