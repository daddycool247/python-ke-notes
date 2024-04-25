#Break
'''n=int(input('Enter how many pairs you want to divide = '))
for i in range(1,n+1):
    dis=int(input('Divisor= '))
    div=int(input('Dividend= '))
    if dis==0:
        print('Divisor cannot be zero')
        break
    else:
        print('quotient=',div//dis,'remainder= ',div%dis)
print('Program is over')

#output
Enter how many pairs you want to divide = 3
Divisor= 3
Dividend= 36
quotient= 12 remainder=  0
Divisor= 0
Dividend= 96
Divisor cannot be zero
Program is over'''

#Continue
'''n=int(input('Enter how many pairs you want to divide = '))
for i in range(1,n+1):
    dis=int(input('Divisor= '))
    div=int(input('Dividend= '))
    if dis==0:
        print('Divisor cannot be zero')
        continue
    else:
        print('quotient=',div//dis,'remainder= ',div%dis)
print('Program is over')

#output
Enter how many pairs you want to divide = 3
Divisor= 2
Dividend= 48
quotient= 24 remainder=  0
Divisor= 0
Dividend= 69
Divisor cannot be zero
Divisor= 0
Dividend= 35
Divisor cannot be zero
Program is over'''

#Prime number
'''isprime=True
n=int(input('Enter an integer= '))
for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        isprime=False
        break
if(isprime==True):
    print(n,'is a prime number')
else:
    print(n,'is not a prime number')
               

#output
Enter an integer= 43
43 is a prime number

Enter an integer= 10
10 is not a prime number'''

#Sorting with the help of nested loop 
'''num=[]
n=int(input('How many number do you want to enter: '))
for i in range(n):
    k=int(input('Enter the element'))
    num.append(k)
print('Original list: ',num)
for i in range(n):
    for j in range(i+1,n):
        if(num[i]>num[j]):
            k=num[i]
            num[i]=num[j]
            num[j]=k
print('Sorted list: ',num)

#output
How many number do you want to enter: 5
Enter the element6
Enter the element8
Enter the element-3
Enter the element9
Enter the element1
Original list:  [6, 8, -3, 9, 1]
Sorted list:  [-3, 1, 6, 8, 9]'''


#New problem for nested loops
'''n=int(input('How many lines to print= '))
for i in range(n+1):
    for j in range(i):
        print('*',end=' ')
    print('\n')

#output
    How many lines to print= 5


* 

* * 

* * * 

* * * * 

* * * * * '''

#reverse
n=int(input('How many lines to print= '))
for i in range(n+1):
    for j in range(i,n+1):
        print('*',end=' ')
    print('\n')

#output
How many lines to print= 5
* * * * * * 

* * * * * 

* * * * 

* * * 

* * 

* 




    
    






