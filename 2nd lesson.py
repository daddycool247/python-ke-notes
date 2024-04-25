
#23/4/2024 Rakesh Sir lecture on python
#While and For Loops

#Q1.Print all natural number from 1 to n
#For
'''n=int(input('Enter an Integer= '))
for i in range(1,n+1,1):
    print(i)'''
    
#While
'''n=int(input('Enter an integer= '))
i=1
while(i<=n):
    print(i,end=' ')
    i=i+1

#Output
Enter an integer= 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'''

#Q2. Print all elements of a list using for loop.
'''L1=[10,20,30,40,50,60,'Doctor','Engineer','Plumber','Police']
for i in L1:
    print(i,end=' ')

#output
10 20 30 40 50 60 Doctor Engineer Plumber Police'''

#Q3. Print all natural numbers in reverse (from n to 1).-using while loop
'''n=int(input('Enter an integer= '))
i=n
while (i>=1):
    print(i,end=' ')
    i=i-1

#output
Enter an integer= 5
5 4 3 2 1 '''

#Q4. print all alphabets from A to Z.-using while loop.
'''for i in range(65,91,1):
    print(chr(i),end=' ')'''

#while
'''i=65
while(i<=91):
    print(chr(i),end=' ')
    i=i+1
#output
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'''

#Q5. Print all even numbers between 1 to 100.-using while loop
'''i=2
while(i<=101):
    print(i,end=' ')
    i=i+2

#output
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100'''

#Q6. Print all odd number between 1 to 100

'''for i in range(1,101,2):
    print(i,end=' ')

#while
i=1
while(i<=101):
    print(i,end=' ')
    i=i+2

#output
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99'''

#Q7. Find sum of all natural numbers betwwn 1 to n.
'''sum=0
n=int(input('Enter an integer= '))
for i in range(n+1):
    sum=sum+i
print(sum)'''

#while
'''n=int(input('Enter an integer= '))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i=i+1
print('Sum of the number is= ',sum)

#output
Enter an integer= 5
15'''

#Q8. Find sum of all even number between 1 to n
'''n=int(input('Enter an integer number= '))
sum=0
for i in range(0,n+1,2):
    sum=sum+i
print('Sum of the even numbers from 1 to',n,'=',sum)'''

#while
'''n=int(input('Enter an integer number= '))
sum=0
i=2
while(i<=n):
    sum=sum+i
    i=i+2
print('Sum of the even numbers from 1 to',n,'=',sum)
    
#output
Enter an integer number= 5
Sum of the even numbers from 1 to 5 = 6'''

#Q9. Find sum of all odd numbers between 1 to n
'''n=int(input('Enter an integer number= '))
sum=0
for i in range(1,n+1,2):
    sum=sum+i
print('Sum of all the odd numbers from 1 to',n,'=',sum)'''

#while
'''n=int(input('Enter an integer number= '))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i=i+2
print('Sum of all the odd numbers from 1 to',n,'=',sum)

#output
Enter an integer number= 5
Sum of all the odd numbers from 1 to 5 = 9'''

#Q10. Print multiplication table of any number
#For
'''product=1
n=int(input('Enter an integer number= '))
for i in range(1,11):
    print(n,'*',i,'=',n*i)

#output
    Enter an integer number= 2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20'''

#Q11. Count number of digits in a number
'''n=int(input('Enter an integer= '))
i=0
while(n>0):
    r=n%10
    n=n//10
    i=i+1
print(i)

#output
Enter an integer= 325496465
9'''

#Q12.Find first and last digit of a number.
'''n=int(input('Enter a number= '))
K=n
digit=[]
i=0
while(n>0):
    r=n%10
    n=n//10
    digit.append(r)
print(len(digit))
print(digit)
print('First digit of ',K,'=',digit[0])
print('Last digit of ',K,'=',digit[-1])'''

#@13. Find sum of first and last digit of a number.
n=int(input('Enter a number= '))
K=n
digit=[]
i=0
while(n>0):
    r=n%10
    n=n//10
    digit.append(r)
print(len(digit))
print(digit)
print('The sum of first and last digit of',K,'is',digit[0]+digit[-1])

#@14.Swap first and last digits of a number.
n=int(input('Enter a number= '))
K=n
digit=[]
i=0
while(n>0):
    r=n%10
    n=n//10
    digit.append(r)
print(len(digit))
print(digit)
First_digit=digit[0]
Second_digit=digit[-1]
Middle_digit=digit[1:-1]
print('After swapping the first and the last digit of',k,'we got',First_digit+Middle_digit+Last_digit)







    



