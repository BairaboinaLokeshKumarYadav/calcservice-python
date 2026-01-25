import math

while True:
    print("1.Basic Calculator")
    print("2.Scientific Calculators")
    print("3.Programmer Calculators")
    print("4.Financial Calculators")
    a=int(input("Enter your choice: "))
    if a==1:
        print("Basic Calculator")
        try:
            exprision = input("Enter the expression (e.g., 2 + 3 * 4): ")
            evaluate = eval(exprision)
            print("The result is: ", evaluate)
        except:
            print("Invalid input. Please enter a valid mathematical expression.")