import math
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
'''
#Problem 3
check = True
a = 600851475143
i = 2
while check:
    if a % i == 0:
        print "yeah"
        print i
        a = a / i
        if i >= a:
            print i
            check = False
    else:
        i = i + 1
