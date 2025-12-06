# Question: Given three numbers find the maximum of three numbers using the ternary operator.

num1=input("Enter num1: ")
num2=input("Enter num2: ")
num3=input("Enter num3: ")
max= num1 if (num1>num2 and num1>num3) else (num2 if (num2>num3) else num3)
print("Maximum number is ", max)
