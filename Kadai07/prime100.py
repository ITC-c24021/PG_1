import math
prime_list = []
for i in range(2,101):
    isPrime = True
    for n in range(2,int(math.sqrt(i) + 1)):
        if i % n == 0:
            isPrime = False
            break
    if isPrime:
        prime_list.append(i)

for i in range(0,len(prime_list),10):
    print(",".join(str(n) for n in prime_list[i:i+10]))
