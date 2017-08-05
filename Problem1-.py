import math

def is_prime(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False

'''
#Problem 1
sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
ptint sum
[Finished in 0.124s]

#Problem 2
sum = 2
s = True
i = 1
j = 2
count = 1
while s is True:
    n = i + j
    if n % 2 == 0:
        sum = sum + n
    if n >= 4000000:
        s = False

    if count == 1:
        count = count + 1
        i = n
    elif count == 2:
        count = count - 1
        j = n
print sum[Finished in 0.086s]

#Problem 3
check = True
a = 600851475143
i = 2
while check:
    if a % i == 0:
        a = a / i
        if i >= a:
            print i
            check = False
    else:
        i = i + 1
[Finished in 0.082s]

# Problem 4
a = 999
b = 999
hold = 0
for i in range(100, 999):
    a = i
    for j in range(100, 999):
        b = j
        result = a * b
        if result > 100000:
            if (result // 100000 == result % 10) and ((result % 100000 / 10000 == result % 100 / 10) and (result % 10000 / 1000 == result % 1000 / 100)):
                if result > hold:
                    hold = result
        else:
            if (result // 10000 == result % 10) and (result % 10000 / 1000 == result % 1000 / 100):
                if result > hold:
                    hold = result

print a, b
print hold[Finished in 0.408s]


# Problem 5
primeAll = 1

for i in range(2, 21):
    if is_prime(i):
        check1 = True
        a = 1
        while check1:
            num = math.pow(i, a)
            if num >= 20:
                check1 = False
            else:
                a = a + 1
        primeAll = primeAll * math.pow(i, a - 1)
print primeAll[Finished in 0.072s]


# Problem6
sum = 0
for i in range(1, 101):
    sum = sum + i
sum = sum * sum
square = 0
for i in range(1, 101):
    square = square + i * i
print square - sum

# Problem7
count = 0
check = True
num = 2
while check:
    if is_prime(num):
        count = count + 1
        if count == 10001:
            check = False
        else:
            num = num + 1
    else:
        num = num + 1

print num[Finished in 45.539s]

# Problem8
s ="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

maxPro = 0
for i in range(0, 999 - 13):
    temp = 1
    for j in range(i, i + 13):
        temp = temp * int(s[j])
    if temp > maxPro:
        maxPro = temp
print maxPro[Finished in 0.101s]

# Problem9
a = 1
for i in range(1, 500):
    a = i
    for j in range(i, 500):
        b = j
        if math.sqrt(a * a + b * b) + a + b == 1000:
            print a * b * math.sqrt(a * a + b * b)
            break[Finished in 0.129s]
'''

# Problem10
sum = 0
for i in range(1, 2000001):
    if is_prime(i):
        sum = sum + i
print sum 
