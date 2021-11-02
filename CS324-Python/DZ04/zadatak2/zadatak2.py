n = int(input("Unesite broj clana čiju vrednost želite da vidite : "))

broj1 = 0
broj2 = 1
sum = 0
for i in range(0, n):
    sum = broj1 + broj2
    broj1, broj2 = broj2, sum
    
#1. rekurzivno resenje
def fibonacci(a,b,n):
    if(n <= 1):
        print(a)
        return a
    return fibonacci(b,a+b,n-1)
#2. resenje zadatka rekurzivnim postupkom
#def fibonacciRek(n):
#    return n if n <= 1 else fibonacciRek(n - 1) + fibonacciRek(n - 2)

a = fibonacci(0,1,n)
print(a)