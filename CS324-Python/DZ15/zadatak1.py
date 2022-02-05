from numpy import number


def isPrime(number):
    if number < 0:
        number *= -1

    if number >= 2:
        for i in range(2, number):
            if number % i == 0:
                return False        

        return True
    return False

def primes_interval(a, b):
    if(a < b):
        return [number for number in range(a, b) if isPrime(number)]
    
    return [number for number in range(b, a) if isPrime(number)]

def squared(numbers):
    return [number * number for number in numbers]

primes_list = primes_interval(-300, -12)
print(primes_list)

squared_list = squared(primes_list)
print(squared_list)