import time
import math

def is_prime_number(n):
    result = True
    print("solution 1")
    t1 = time.time()
    if number <= 1:
        result = False
    else:
        for i in range(2,n):
            if n % i == 0:
                result = False
    t2 = time.time()
    print('required time for solution 1 is : {}'.format(t2 - t1))
    print('----------------------------------------------------')

    print("solution 2")
    t1 = time.time()
    if number <= 1:
        result = False
    else:
        for i in range(2, 1 + math.floor(math.sqrt(n))):
            if n % i == 0:
                result = False
    t2 = time.time()
    print('required time for solution 1 is : {}'.format(t2 - t1))
    print('----------------------------------------------------')

    if result:
        print('{} is prime'.format(number))
    else:
        print('{} is not prime'.format(number))



number = int(input('please input your number : '))
is_prime_number(number)
