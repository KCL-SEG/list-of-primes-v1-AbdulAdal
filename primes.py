"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    for num in range(2,101):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime and len(list)<number_of_primes:
                list.append(num)
    return list