#Functions 

'''x=0
import math
print(math.sin(x))
print(math.sin(math.pi/2))
print(math.cos(x))
print(math.cos(math.pi/2))
print(math.exp(2))
print(math.sqrt(16))
print(math.pi)
print(math.e)'''

#Factorial problem by creating function of it

'''def fact(n):
    ''''''The following program is related to Factorial function of a number created by Aman Gupta on 25th April 2024 during the Nut and bolths of python programming course.''''''
    p=1
    for i in range(1,n+1):
        p=p*i
    return(p)

n=int(input('Enter value of n= '))
r=int(input('Enter value of r= '))
print('The nCr=',fact(n)/(fact(r)*fact(n-r)))

#output
Enter value of n= 5
Enter value of r= 2
The nCr= 10.0
print(fact.__doc__)
The following program is related to Factorial function of a number created by Aman Gupta on 25th April 2024 during the Nut and bolths of python programming course.'''

#function without parameter and return
'''def f_without_para_return():'''
    '''This function illustrates the program is without parameter and without return'''
   ''' print('Welcome to the world of programming.')'''
'''f_without_para_return()'''

#Function without parameter but with return value.
def fixed_prime_check():
    '''The program illustrates the function is without parameter and with return value.'''
    isprime=True
    for i in range(2,int(99**0.5)+1):
        if(99%2==0):
            isprime=False
            break
    return isprime
if(isprime==True):
    print(' 99 is prime')
    else:
        print('99 is composite number')
