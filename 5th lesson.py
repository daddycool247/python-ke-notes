#Function without parameter but with return value.
'''def fixed_prime_check():
    ''''''The program illustrates the function is without parameter and with return value.''''''
    isprime=True
    for i in range(2,int(99**0.5)+1):
        if(99%i==0):
            isprime=False
            break
    return isprime
if(fixed_prime_check()==True):
    print(' 99 is prime')
else:
    print('99 is composite number')'''

#for any number
'''def fixed_prime_check(n):
    ''''''The program illustrates the function is without parameter and with return value.''''''
    isprime=True
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            isprime=False
            break
    return isprime
n=int(input('Enter an Integer= '))
if(fixed_prime_check(n)==True):
    print(n,' is prime')
else:
    print(n,' is composite number')'''

#Function with default argument
def printinfo(name,Age=20):
    '''This program illustrates the Function with default argument .'''
    '''print('Name is : ',name)
    print('Age is : ',Age)
name=input('Enter your name = ')
Age=int(input('Enter your age= '))
printinfo(name)
printinfo(name,Age)'''



# Function with more than one return values:
'''m1=int(input('Enter the marks of first subject: '))
m2=int(input('Enter the marks of second subject: '))
m3=int(input('Enter the marks of third subject: '))
def result(m1,m2,m3):
    return m1+m2+m3,(m1+m2+m3)/3
tot,avg=result(m1,m2,m3)
print('The total marks=',tot,'and the average marks=',avg)'''

#Function returning list values:
'''s=input('Enter a string:')
def returnlist(str):
    return list(str)
print('The list value is',returnlist(s))'''

#Variable-lenght argument:
'''def print_info(arg1,*vartuple):
    print(arg1)
    for var in vartuple:
        print(var)
    return'''

#Lambda Function
#1
'''sq=lambda x:x*x
print(sq(2))
print(sq(4))'''

#2
'''oddeven=lambda x:'Even' if(x%2==0) else 'Odd'
print(oddeven(3))
print(oddeven(4))'''

#3
'''minimum=lambda x,y:x if x<y else y
print('Min is ',minimum(10,16))'''

#4
'''prime=lambda p:'Not prime' if(p%2==0) else 'prime'
print(prime(33))
print(prime(4))
print(prime(546454534899))'''

#5
'''lis=[1,2,3,4]
mapped=map(lambda x:x*x,lis)
for k in mapped:
    print(k,end =' ')'''

#6
students=[('aman',20),('aryan',19),('rohan',21)]
students.sort(key=lambda student:student[1])
