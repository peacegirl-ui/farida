print("MENU")
print('---------------------' \
'------------------------')
print('-------------------' \
'--------------------------')
print("Welcome to multi-utility tooklist")
print('---------------------' \
'------------------------')
print('-------------------' \
'--------------------------')
print("Choose an option ")
print("1.Datetime & time operations")
print("2.mathematical operations")
print("Random data Generation ")
print("Generate unique Identifier (UUID)")
print("File operations")
print("Explore module")
print("Exit")
print('---------------------' \
'------------------------')
print('-------------------' \
'--------------------------')

choice=int(input("enter your choice:"))

print("Date & Time Operatioms:")
print("Display current data time") #datetime.now()
print("Calculate difference between two dates and time") #strptime(),difference.days()
print("Format date into costome format ") #strftime("%d-%y-%m %I:%M-%p")
print("Stopwatch ") #time.time()
print("Countdown timer") #sleep.time()
print("Back to main menu")

print(" 1.display current data time:") #datetime.now()
choice=int(input("enter your choice:"))
from datetime import datetime
print("Current date And Time",datetime.now())

# print("2.calculate difference between two dates and time")
# choice=int(input("enter your choice:"))
# print("___________________________")
date1 = datetime.strptime("2024-12-25" , "%Y-%m-%d")
date2= datetime.strptime("2025-01-04" , "%Y-%M-%d")
Difference=date2-date1
print("Difference:",Difference.days,"days")

print("3.Format date into costome format") #strftime()
choice=int(input("enter your choice:"))
today=datetime.now()
print(today.strftime("%d-%m-%Y %I:%M-%p")) #%i-hour(12hr format) #%h-hour(24hour format) %m-month(number)

print("4.Stopwatch ") #time.time()
import time
choice=int(input("enter your choice:"))
input("Press Enter to start stopwatch..")
start=time.time() # record start time
input("press Enter to stop stopwatch...")
stop=time.time() # record stop time
elapsed= stop-start  #Difference in seconds #elapsed= how much time has passed
print("elapsed time:", round(elapsed,2),"seconds")

print("5.Countdown timer") #time.sleep()
choice=int(input("enter your choice:"))
import time #step 1
def countdown(seconds):
    while seconds> 0: #step 2
        print(seconds) #step 3
        time.sleep(1)  #step 4
        seconds = seconds-1 # step 5

 
print("5.countdown Time")
seconds=int(input("enter time in seconds:"))

countdown(seconds)
print("Time's up!")
choice=int(input("enter your choice:"))

print("Mathematical operations:")
print("1.Calculate factorial")
print("2.Solve compound interest")
print("3.TRignometric calculations")
print("4.Area of geometic shapes")
print("Area of main menu")

choice=int(input("enter your choice:"))
number=int(input("enter your number:"))

n = 5
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print("Factorial =", factorial)
print('---------------------'
'------------------------')
choice=int(input("enter your choice:"))
P=int(input("Enter principal amount"))
R=int(input("Enter rate of interest(in %)")) /100
T=int(input("Enter time (in years):"))
A=P*(1+R)**T
CI=A-P

print("Compound Interest=" , round(A, 2))
print('---------------------'
'------------------------')


choice=int(input("enter your choice:"))
print("Random data Generation")
print("Generate random number")
print("Generate random list")
print("Create Random password")
print("Generate Random OTP")
print("Back to main menu")
choice=int(input("enter your choice:"))

import random
#random password 
character = "kd8@qP!"
Length = int(input("Enter password length: "))

password = "".join(random.choice(character) for _ in range(Length))

print("Generated password:", password)

#another example of password
char="farida@02"
lenght=int(input("enter lenght"))
password="".join(random.choice(char) for _ in range (lenght))
print("Generated_password:",password )
print('---------------------'
'------------------------')
choice=int(input("enter your choice:"))

print('---------------------'
'------------------------')
#random list 
items = [10, "apple", 3.14, "banana", True]
random_list = random.choices(items, k=3) 

print("Random list:", random_list)
choice=int(input("enter your choice:"))
print('---------------------'
'------------------------')
#generate random otp
otp = random.randint(1000, 9999)
print("Your OTP is:", otp)
print('---------------------'
'------------------------')
choice=int(input("enter your choice:"))

print("Generate Unique Identifiers:")

import uuid
unique_id=uuid.uuid4()
print("Generate UUID:",unique_id)
choice=int(input("enter your choice:"))

print("File Operations:")
print("1.Create a new file")
print("2.write to a file")
print("Read from a file")
print("Append to a file")
print("Back to main menu")


choice=int(input("enter your choice:"))
file_name=input("enter a file name:")
with open(file_name,"w") as f: #file_name,"w"Creates a new file
    pass
print("Filecreated successfully!")
print('---------------------'
'------------------------')

choice=int(input("enter your choice:"))
file_name=input("enter a file name:")
data=input("Enter data to write:")
with open(file_name,"w") as f:#w meams write mode
    f.write(data) #puts your msg into the file
print("Data written successfully!")
print('---------------------'
'------------------------')


choice=int(input("enter your choice:"))
file_name=input("enter a file name:")
with open(file_name,"r")as f: # r means read mode
   content= f.read()
print("File content:",content)
print('---------------------'
'------------------------')
choice=int(input("enter your choice:"))

file_name=input("enter a file name:")
data=input("Enter data to append:")
with open(file_name,"a")as f: #a means appened mode
    f.write("\n"+ data)
print("Data Appened successfully!")   
print('---------------------'
'------------------------')
choice=int(input("enter your choice:"))

print("Back to main menu")
choice=int(input("enter your choice:"))

import math
print("Explore module attributes")

name=input("Enter module name to explore")
print("Available Attributes in math module:")
print(dir(math)) #it shows all methords work under math module
print('---------------------'
 '------------------------')

print("6.Exit")
print("Thankyou for using the multi-utility tooklist")