
print(3+1)
print(3*3)
print(2**3)
print("hello, world")


# Exercise 1.3

print('py' + 'thon')  #concatenation
print('py' * 3 + 'thon')
print('py' - 'py')  # - operand is not used in string concatenation
print('3' + 3) # Error can only concatenate str to str.
print(3 * '3')
print(a) # we don't assign any value  'a' to before.it will show NameError.
a = 3
print(a)

# Exercise 1.4 -> Booleans
print(1 == 1)     # in boolean values 1 = true and 0 = false.         
print(1 == True)          
print(0 == True)           
print(0 == False)         
print(3 == 1 * 3)         
print((3 == 1) * 3)        
print((3 == 3) * 4 + 3 == 1) 
print(3**5 >= 4**4)


# Exercise 1.5 -> Integers

print(5 / 3)    # In python / is used for floating-point division
print(5 % 3)     
print(5.0 / 3)  
print(5 / 3.0)   
print(5.2 % 3)
print(2001 ** 3)

# Exercise 1.6 -> floats

# print(2000.1 ** 200) it will not provide output because floating-point have limited range
print(1.0 + 1.0 - 1.0)
print(1.0 + 1.0e20 - 1.0e20) # 1.0e20 is 1 x 10*20.(scientific notation).

# Exercise 1.7 -> variables.
   # write a script where variable name hold a string with your name.then output "Hello, name!" 

name = "shahid"
print("Hello, " + name + "!")

# Exercise 1.8 -> Typecasting 

print(float(123))         # converting integer to floating number
print(float('123'))        # converting str to floating number
print(float('123.23'))     # Converting str to float.
print(int(123.23))         # converting floating to integer.it will cut the decimal part. print(int('123.23'))
#print(int('123.23'))        # Error because we cannot convert str to integer directly.
print(int(float('123.23'))) 
print(str(12))       # converting integer to str.but vice versa is not possible.       
print(str(12.2))        #converts floats to string.   
print(bool('a'))        # any non empty strng is considered as true
print(bool(0))           # 0 is considered as False.  
print(bool(0.1))   # non zero is also considered as True.

# Exercise 2.1 -> Range
range(5)
print(range)
type(range(5))

# Exercise 2.2 -> For loops

 # Print numbers from 0 to 100?
for i in range(0, 101):
    print(i)
  
  # print numbers from 0 to 100 that are divisible by 7?
for i in range (0, 100):
    if i % 7 == 0:
        print(i)

# Print numbers from 1 to 100 that are divisible by but not 3?

for i in range (1, 101):
    if i % 5 == 0 and i % 3 != 0:
        print(i)
 
# Print for each of the number x = 2,....20, all numbers that divide x, excluding 1 and x.Hence,for 18, it should print 2,3,6,9.


for x in range(2, 21):
    divisors = []
    for i in range(2, x):
        if x % i == 0:
            divisors.append(i)
            print(divisors)

# Exercise 2.3 -> simple  while loops

i = 0               # printing numbers from0 to 100.
while i <= 100:
    print(i)
    i += 1


i = 0           # printing numbers from 0 to 100 which are divisible by 7.
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1


# Exercise 2.5 -> WHILE LOOPS

number_found = 0     # first 20 numbers which are divisible by 5, 7, and 11.
x = 11
while number_found < 20:
    if x % 5 == 0 and x % 7 == 0 and x % 11 == 0:
        print(x)
        number_found += 1
    x += 1
 
# Exercise 2.6 More while loops.

x = 1                  # Smallest number divsible between 1 to 10.
while True:
    divisible = True
    for i in range(1, 11):
        if x % i != 0:
            divisible = False 
            break
    if divisible:
        print(x)
        break
    x += 1
       


x = 103
while x != 1:
    print(x, end=' ')
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
print(x)







