#PROBLEM 3
#NATALEE DESOTELL

n = 100 #for both functions, testing when n=100

#ITERATIVE FUNCTION
x = 0 #initialize
for i in range(1, n):
    x += i
print(x)

#RECURSIVE FUNCTION
def sum(n): #define function
    if not n:
        return 0
    else:
        return n + sum(n-1)
print(sum(n))

print("The iterative function evaluates to", x, "and the recursive function evaluates to", sum(n))
difference = abs(x - sum(n))
print("The difference between the two answers is", difference, ". These functions return different answers because range counts until n-1, or", n-1, "while the recursive function counts all the way to", n)
