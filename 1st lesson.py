#My contacts
'''Name='Aman Gupta'
Mobile_number='9930537446'
Address='Sion Koliwada'

print('My name is',Name,'\nAnd my Mobile number is',Mobile_number,'\nAnd I live in',Address)'''

'''#2nd question (Area of circle)
r=int(input('Enter the value of radius= '))
import math
print('The area of circle is',math.pi*r**2)'''

'''#mean
x=int(input('x='))
y=int(input('y='))
z=int(input('z='))

import math
mean=(x+y+z)/3
print('mean of',x,y,'and',z,'is',mean,end='.')'''

'''#hour to minutes and seconds
hours=int(input('No. of hours= '))
minutes=hours*60
second=hours*3600

print(hours,'hour is equal to',minutes,'minutes and',second,'seconds')'''

'''#temperature- celius to fahrenheit
celius=float(input('Temperature in celcius= '))
fahrenheit=celius*9/5+32

print('The temerature',celius,'degree celius is equal to',fahrenheit,'degree fahrenheit')'''


'''#Area of rectangle
Lenght=10
Breadth=8
print('Area of the rectangle=',Lenght*Breadth,'cm',end='.')'''

'''#BMI
Weight=85
height=1.75
import math
print('The BMI Index=',Weight/height**2,end='.')'''

'''#Cube
a=3
import math
print('Cube of',a,'=',a**3,end='.')'''

'''#Swaping two number
x=2
y=3
print(x,y)
x,y=y,x
print(x,y)'''

'''#Kilometeres to miles
k=10
miles=k*0.621371
print('10 kilometers=',miles,end='miles.')'''

'''#tonnes to quintals and kilogram
t=3
quintal=t*10
kilogram=quintal*100
print('3 tonnes =',quintal,'quintal and',kilogram,'kilogram',end='.')'''

'''First_name='Aman '
Middle_name='Tarachand '
Last_name='Gupta '
Age=20
Full_name=First_name+Middle_name+Last_name
#print(Full_name)
#print(Full_name.upper())
#print(First_name*3)
print(Middle_name.count('a'))
print(Full_name[0:8])
print(Full_name[7])
print(First_name[0],Last_name[0],Middle_name[0])
print(Full_name[1:8])'''

'''#new problem
p=float(input('Enter the principle amount in rupees= '))
n=float(input('Enter the no. of year= '))
r=float(input('Enter the rate of interest= '))
simple_interest=(p*n*r)/100
print('Simple interest is= ',simple_interest,end='Rs.')
Final_amount=p*(1+r/100)**n
compound_interest=Final_amount-p
print('And the compound interest is',compound_interest,end='Rs.')'''

'''#New problem
x='He is'
y='telling truth'
z='telling lie'
#print(x,y)
#print(x,z)
print(y*3)
print(x[0:2],y[0:2],z[0:2])
print(len(y))
print(y[0:13:2])
print()
print(len(y))
print()

#Assignment 4
slogen='We are Khalsite.'
print(slogen.lower())
print(slogen.upper())
print(slogen.find('r'))
print(slogen.replace('We','You'))
print(slogen.count('e'))
print(len(slogen))
print(slogen[0:16:2])
print()

#Assignment 5
L1=[10,20,30,40,50,60]
L2=['Doctor','Engineer','Plumber','Police']
L3=L1+L2
print(L3)
L3[2]=47
print(L3)
sublist=L3[2:5]
print(sublist)

l1=[10,2,1,10,4,5]
print(max(l1))
print(min(l1))
print(len(l1))
print(l1.count(10))
l1.extend([7,8])
print(l1)
del l1[1:3]
print(l1)'''

'''#Dictionary problem
maths_dept={'calculus':'Ms. Lata Mohan','algebra':'Ms. Dipali Sawant','Differential_equation':'Dr. Rakesh Barai'}
print(maths_dept.keys())
print(maths_dept.values())
print(maths_dept['calculus'])
maths_dept['calculus 2']='Ms.Archana singh'
print(maths_dept)
maths_dept['Differential_equation']='Dr. Mittu Bhatacharya'
print(maths_dept)

#Set problem
set1=set([1,2,3,4,5])
print(set1)
set2=set([5,6,7])
print(set2)
set3=set1|set2
print(set3)
set4=set1&set2
print(set4)
set5=set([4,6,7])
print(set5)
set6=set1-set5
print(set6)
set7=set1^set6
print(set7)

# new set problem
fruits=set(['apple','mango','orange','tomato'])
vegetables=set(['potato','tomato','onion','ginger'])
food_items=fruits|vegetables
print(food_items)'''


#Data type

      

'''#new assignment (use of arithmetic operators)
a=20
b=2
c=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b%a)
print(b%c)'''

'''#input function
Name=input('Enter your name: ')
Mobile_number=input('Enter your Mobile name: ')
Address=input('Enter your Address: ')
Age=int(input('Enter your Age: '))
College_name=input('Enter your college name: ')'''

'''Scores=input('Enter the score of Virat kohli in each match= ')
Scores=Scores.split(',')
Scores=[int(value) for value in Scores]
print("Virat Kohli's score in each match",Scores)'''

'''#1. Write a program that takes the length of an edge (an integer) as input and pirnts the cube's surface area as output.
lenght=int(input('Enter the lenght of the edge= '))
cube=6*lenght**2
print("Then the cube's surface ares is",cube,end='sq units.')'''

'''#2. Write a program to find the sqaure root of a number by inputting the number through key board.
x=float(input('x= '))
print('Therefore the sqaue value of x is',x**2,end='.')'''

'''#3. Write a program to find the area of a Rectangle by inputting the edge through key board.
lenght=float(input('Enter the lenght of the rectangle= '))
breadth=float(input('Enter the breadth of the rectangle= '))
print('Therefore, the area of rectangle is',lenght*breadth,end='sq unit.')'''

'''#4. Write a program to swap the values of two variables using third variable by inputting the values of the variable through key board.
x=int(input('x= '))
y=int(input('y= '))
x,y=y,x
print('Then y is',y)'''

'''#6. Write a program to convert kilogram into pound.(1 kg=2.20462)
kg=float(input('Enter the weight in kilograms= '))
print('Then the weight in pound will be',kg*2.20462,end='pound.')'''

'''#7. Write a program that takes the radius of a sphere (a floating-point number)as input and then outputs the sphere's diameter, circumference, surface area, and volume.
import math
R=float(input('Enter the radius of the sphere= '))
print('The diameter of the sphere= ',2*R,'units.')
print('The circumference of the sphere= ',2*math.pi*R,'units.')
print('The surface area of the sphere= ',4*math.pi*R,' sq. units.')
print('The volume of the sphere= ',(4/3)*math.pi*R**3,'cu. units.')'''

'''#8. An object's momentum is its mass multiplied by its velocity. Wirte a program that accepts an object's mass (in kilograms) and velocity (in meters per second ) as input and then outputs its momentum.
mass=float(input('Enter the mass of an objects in kilograms= '))
velocity=float(input('Enter the velocity in meters per second= '))
print('Momentum of the object is',mass*velocity,'.')'''

'''#9. The kinetic energy of a moving object is given by the formula where m is the object's mass and v is its velocity. Modify the previous program you created so that is prints the objects's kinetic energy as well as its momentum.
mass=float(input('Enter the mass of an objects in kilograms= '))
velocity=float(input('Enter the velocity in meters per second= '))
print('Then the kinetic energy of an object is',(1/2)*mass*velocity**2,'and its momentum is',mass*velocity)'''

'''#10. Write a program that calculates and prints the number of minutes in a year.
Year=int(input('Enter the number of year= '))
print('The number of minutes in',Year,'years is',Year*365*24*60)'''

'''#11. Light travels at 3*10^8 meters per second. A light-year is the distance a light beam travel in one year. Write a program that calculates and displays the value of a light year
light_years=float(input('Enter the number light years= '))
print('The distance travelled in',light_years,'light_years= ',light_years*365*24*60*60*(3*10**8))'''


'''# If,elif and else
x=int(input('Enter a number= '))
if x==0:
    print("It's a zero")
elif x>0:
    print('The number is positive')
else:
    print('The number is negative')
print('The program is over')'''




'''#Write a program to determine whether the person is eligibe to vote or not
x=int(input('Enter the age of the candidate= '))
if x>18:
      print('The candidate is eligible to vote.')
elif x==18:
     print('The candidate is eligible to vote.')
else:
    print('The candidate is not eligible to vote.')
    print('The candidate will be eligible to vote in',18-x,'years')'''

'''#Write a program to input a number and check whether it is even or odd.
n=int(input('Enter the number= '))
if n%2==0:
    print('The number is even')
else:
    print('The number is odd')'''

'''#4. Enter gender and salary of an employee. A male gets 10% and female gets 15% of their salary as bonuns. Also if the salary is less than 10000/-,he/she gets 2% of salary as extra bonus. Find total bonus.
Gender=input('Enter your Gender(Male/Female)= ')
Salary=int(input('Enter your salary in Rs.= '))
if Gender=='Male':
    bonus=0.1*Salary
else:
    bonus=0.15*Salary
print('Bonus= ',bonus)

if Salary<10000:
    extra_bonus=0.02*Salary
print('The extra bonus= ',extra_bonus)
print('The total bonus= ',extra_bonus+bonus)'''

'''#5. Write a program to find whether an entered year is leap year or not
year=int(input('Enter the year= '))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')'''

'''#Write a program to input two numbers and find the largest
x=float(input('Enter the 1st number= '))
y=float(input('Enter the 2nd number= '))
if x>y:
    print(x,'is the largest number')
else:
    print(y,'is the largest number')'''


    






               


