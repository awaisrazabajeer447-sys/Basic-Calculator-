    simple calculator 
while True:
    print("1. Add")
    print("2. Sub ")
    print("3. Multipy ")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice : ")
    if choice == "5":
        print("the program EXIT.")
        break
    num1 = float(input("enter num1: "))
    num2 = float(input("enter  num2: "))

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        print("Result:", num1 // num2)

    else: 
        print("Invalid! Please choose a valid choising.")


