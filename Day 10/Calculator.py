def calculator():
    operations = {"+" : (lambda a, b: a + b), "-" : (lambda a, b: a - b), "*": (lambda a, b: a * b), "/": (lambda a, b: a / b)}

    #User input num1, operation, num2
    num1 = float(input("First Number? "))
    for operation in operations.keys():
        print(operation)
    operation_symbol = input("What type of operation do you want to use? ")
    num2 = float(input("Second Number? "))

    #Calculate the answer
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    #Ask if they want to do multiple calculation
    check = input("Do you want to continue? ")
    run = (lambda x: True if x == "y" else False)(check)

    #Next calculation
    while run:
        num1 = answer
        operation_symbol = input("Pick another operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        check = input("Do you want to continue? ")
        run = (lambda x: True if x == "y" else False)(check)
        if not run:
            calculator()

calculator()

