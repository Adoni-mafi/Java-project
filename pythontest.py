# # a=int(input("inter your age"))
# # b=input("inter your name")
# # print("YOUR NAME IS:",b)
# # print("YOUR AGE IS :",a)
# x = "awesome"
# y = 1

# def myfunc():
#  global x 
#  x="i wanna to change the global variable"
#   print("Python is " + x)

# myfunc()
# print("Python is " + x)
# print(type(y))
# this code is generating bias number from the two unkown numbers by taking from the user
# import random
# x= int(input("ENTER THE NUMBER"))
# y=int (input("ENTER THE SECONDE NUMBER"))
# print(random.randrange(x,y))
# a="hello, world!"
# print(a[6])
# print(len(a))
# x=int(input("enter number"))
# if x<0:
#     print("THE NUMBER IS NEGATIVE")
# elif x==0:
#     print("THE NUMBER IS ZERO")
# else: 
#     print('THE NUMBER IS POSETIVE')
# this code is checking the user name and password if it's memeber it says welcome and if it's not didn't accepted to the member of the club
# userName=input("EINTER YOUR USER NAME\n")
# password=int(input("ENTER YOUR PASSWORD\n"))
# if password== 123:
#     if userName=='aron':
#         print('WELCOME')
        
# else:
    # print('your are not admin')

#this is exception handling using try and except system 


# try :
#     a=int(input("ENTER ORDER NUMBER"))
# except:
#     print("PLEASE ENTER NUMBER ONLY!!")

#write a program that prints from 1-5

# for i in range (1,6):
#     print (i)
#write a program that prints "hello youtube" 10 times

# for i in range (10):
#     print("Hello YouTube")
# write a program that tells the list even and odd numbers
# a=[1,2,3,4,5,6,7,8,9]
# for num in a:
#     b=num%2
#     if b==0:
#         print("even numbers")
#     else:
#         print("odd numbers")
#write a program that accept name from the user and search's for student name and is the name is found it will print the average. else it will print "there is no student found by the name"
# S_name=['aron','amare','jembere','mamo','abebe']
# S_avarage=[78,99,89,88,98]
# acceptedName=input("ENTER NAME")
# for i in S_name:
#     if i==acceptedName:
#         print("the name is found",S_avarage[i])
#     else:
#         print("There is no studnet found by the name")
#correction
# db={'aron':98,'amare':99}#dictionary
# user=input('ENTER NAME ')
# for studnet in db:
#     if user==studnet:
#         print("your avarage us :", db[studnet])
#         break
# else:
#     print("There is no studnet found by the name ",user) 

#write a program which list number until 3000 and when it's 2012 it will stop
# i=0
# while i<=3000:
#     print(i)
#     if i==2012:
#         break
#     i=i+1
#counting tehnique the excution is horizontally
# print(5*"hello world")
#write a program that accept a pin number only and output your have entered...if letters added makek the error disappeared
# try:
#     num=int(input("ENTER PIN NUMBER")) 
#     print("your enter is:",num)
# except:
#     print("please enter number only!!")
#write a program that have [a,0,9] list and it divide it to 1 and it have ton make out put without error
#function in python
#create a function that prints name and by using an argument
# def FName():
#     name=input("ENTER NAME:")
#     print(name)
# def LName(name):
#     print(name)
# FName()
# LName('aron')
#create a function that repeats name. based on the number given in the argument
# def Nrepeated(a):
#     for i in range(a):
#         print("ARON AMARE")
# Nrepeated(10)
#creare a addition function that used to add numbers given inthe arguments
# def sum( a, b):
#      # return a+b 
#      c=int(a)+int(b)
#      print(c)
     
# sum(10,20)

#recursion and creating module importing 
#write a program which repeats output without using loops
# def name():
#     print("ARON AMARE")
#     name()
# name()
#write a program tha can output factorial of a number 
# def factorial(a):
#     if a==0:
#         return 1
#     else:
#         return a*factorial(a-1)   
# print(factorial(5))
#pip turiral 
# from colorama import *
# print(fore.GREEN"this is the first colorama color")

#object orianted programming side of python
# class Firstclass:
#     pass
# channel=Firstclass()
#methis are function defined inside the boby of a class
# class Firstclass:
#     def display(Self):
#         print("THE GIRL WHO INFRONT OF ME IS CUTE")
# d1=Firstclass() 
# d1.display()
# #inheritance
# class ethiopia(Firstclass):
#     def hello(Self):
#         print("this is the inheritance concept")
# d2=ethiopia()
# d2.display()
# d2.hello()
# class person:
#     def __init__ (Self, name, age):
#         Self.name=name
#         Self.age=age
#     def display(Self):
#         print("HELLO GUYS MY NAME IS :"+ Self.name)
# p1=person("Aron",23)
# p1.display()
#mosh python project for beginners
#dice_rolling game 
#Ask: rll the dice?
#if user enter y
#   generate two random numbers 
#   print them 
#if user enter n 
#    print thnak you message
#   temrminate the program 
#else
#   print invalid choice
# import random
# while True:
#     choice=input("Roll the dice?(y/n)").lower()
#     if choice=='y':
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)
#         print(f'({die1},{die2})')
#     elif choice=='n':
#         print('Thanks for playing!')
#         break
#     else:
#         print('Invalid choice!')
#create a youtube class and accept channel name from the user and print the country of the channel 
# user=input('ENTER CHANNEL NAME')
# data={'geez tech':'ethiopia','mosh':'united state'}
# class Youtube:
#     def __init__(Self,countryName):
#         Self.countryName=countryName
#     def cout (Self):
#         for i in data:
#             if Self.countryName==i:
#                 print('Accepted')
#             else:
#                 print("didn't accepted")           
# y=Youtube(user.lower())#used to change the user input into lower case
# y.cout()
#number gussing game
 
#file handling program in python
#python file handling (file input and output )
"""var=open("filename or filepath ",mode)
modes:
write =w
read=r
append=a
create=x
text mode=t
binary mode=b"""
#write a program that can create and write "This is My file"text
# f=open("E:\Desktop\python\MyData.txt",'w')
# f.write("This is My file")
# f.close()
#to read the file 
# fr=open("E:\Desktop\python\MyData.txt",'r')
# print(fr.read())
#write a program that can delete the file if it exist
# import os
# os.remove('"E:\Desktop\python\MyData.txt"')

#convert python file to exe(using py installer(it's a module))
#mini python project
#qr code genrator
#first we need to create venv enviroment then in that enviroment we must to install pip install qr code. after that we improt the library
import qrcode
data = input('Enter the text or URl: ').strip()
filename = input('Enter the filename: ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color="white")
image.save(filename)
print(f'QR code saved as {filename} ')



    








