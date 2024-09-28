a = input()
list1 = list(map(int, a.split()))
primes = []
def filter_prime(list1):
    for num in list1:
        if num > 1:
            prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                 prime = False
                 break
            if prime:
                primes.append(num)
    return primes

f = filter_prime(list1)     
print(f)       
    
