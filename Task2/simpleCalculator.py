def calculator(n1, n2, op):
    answer = 0

    if(op=='+'):
        ans = n1 + n2
    elif(op=='-'):
        ans = n1 - n2
    elif(op=='*'):
        ans = n1 * n2
    elif(op=='/'):
        ans = n1 / n2
    elif(op=='%'):
        ans = n1 % n2
    else:
        print("\nError: Invalid Operation")
        exit()
    
    return ans
        

#Main()_body:

num1, num2 = input("Enter two values: ").split()
num1 = float(num1)  # Convert to float
num2 = float(num2)  # Convert to float

operation = input("Enter the Operation (+, -, *, /, %): ")

answer = calculator(num1, num2, operation)

print("\n",num1,operation,num2,"=", answer)