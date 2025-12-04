n = input()
n = int(n)


numbers = []
def dummy_function(g):
     print(" ".join(g[::-1]))  # just a dummy operation to use x
for _ in range(n):
    x = str(input())   # read one number from a new line
    numbers.append(x)


for i in numbers:
    dummy_function(i)


