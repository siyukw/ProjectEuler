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
'''

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



print num
