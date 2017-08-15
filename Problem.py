import math

def is_prime(n):
    if n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

    return True;


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

print num[Finished in 0.284s]

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


# Problem10[Finished in 14.544s]
sum = 2
for i in range(3, 2000000):
    if is_prime(i):
        sum = sum + i
print sum

'''

# Problem11
s = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
temp = 0
l = []
for i in range(0, len(s)):
    if s[i] != " ":
        temp = temp * 10 + int(s[i])
    else:
        l.append(temp)
        temp = 0

l.append(48)
max = 0
i = 0
while i < len(l) - 2:
    if (i + 3) % 20 != 0:
        #print i
        curr = l[i] * l[i + 1] * l[i + 2] * l[i + 3]
        if curr > max:
            max = curr
        i = i + 1
    else:
        #print "o"
        i = i + 3

for j in range(0, 320):
    curr = l[j] * l[j + 20] * l[j + 40] * l[j + 60]
    if curr > max:
        max = curr

n = 0
while n < 336:
    if (n + 3) % 20 != 0:
        curr = l[n] * l[n + 21] * l[n + 42] * l[n + 63]
        if curr > max:
            max = curr
        n = n + 1
    else:
        n = n + 3

m = 0
while m < 340:
    if m % 20 > 2:
        curr = l[m] * l[m + 19] * l[m + 2 * 19] * l[m + 3 * 19]
        if curr > max:
            max = curr
        m = m + 1
    else:
        m = m + 1

print max
