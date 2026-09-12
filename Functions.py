def usdToInr(USD):
    inr = USD*90
    return inr

print(usdToInr(90))

print("------------------------------------------------ Recursion ----------------------------------------------------")

def printnum(n):
    if n == 0:
        return
    print(n,end=" ")
    printnum(n-1)

printnum(5)
