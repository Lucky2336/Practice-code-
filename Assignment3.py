"""
John is trying to solve the arithmetic series(AP). He wants to find two things in the series
1. He wants to find nth terms in the series
2. He wants to find the sum up to the nth term.
"""

first=float(input("Enter the first term of the AP: "))
diff=float(input("Enter the common difference between terms : "))
n=int(input("Enter the no. of terms : "))

nthTerm=first + (n-1) * diff
sum=(n / 2) * (2 * first + (n - 1) * diff)

print("The nth term  is : ", nthTerm)
print("The sum of the AP of nth term is : ",sum)