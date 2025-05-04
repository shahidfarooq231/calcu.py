# def hello_world():
#     print('Hello, world!')

# hello_world()    


# def hello_name(name):
#     print(f'hello,{name}')  

# hello_name("shahid") 


# Exercise  no. 3.2 -> polynomial

# x = int(input("enter the value of x : "))
# def eval_poly(x):    
#     return( 3* x**2 - x + 2)       # we are taking X = 2.

# print(eval_poly(x)) 


# Exercise 3.3 -> Maximum

# def my_max_if_else(x, y):
#     if x > y:
#         return x
#     else:
#         return y
    
# print(my_max_if_else(11,22))    


#  (b) Using if_only

# def my_max_if_only(x, y):
#     if x > y:
#         return x
#     return y

# print(my_max_if_only(1,5))

# Exercise 3.5 -> Primes


 #  write a Function is_prime that returns True only if n is prime




# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

 # # Print all primes from 1 to 29
# for n in range(1, 30):
#     if is_prime(n):
#         print(n, "is prime")


# Anothe way to find prime.

# num = int(input("enter a number :"))

# for i in range(2,num):
#     if num % i == 0:
#         print("Not prime")
#         break
# else:
#     print("prime")


#  find primes upto n

# def primes_up_to(n):
#     if n < 2:
#         return []
#     primes = []
#     for num in range(2, n + 1):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes


# print(primes_up_to(20))  


 # Function for first n numbers

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

print(first_n_primes(10))        


