print("Welcome to the pattern generator and number analyzer!")

print("select an option:")
print("1.generate a pattern")
print("2.Analyze a range of numbers")
print("3.Exit")

choice=int(input("Enter your choice"))
 
rows=(input("enter the numbers of rows for the pattern"))

print("\nPattern:")
rows=5
if rows==1:
    print("*")
elif rows==2:
    print("*")
    print("**")
elif rows==3:
    print("*")
    print("**")
    print("***")
elif rows==4:
    print("*")
    print("**")
    print("***")
    print("****")
elif rows==5:
    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")
else:
    print("not printing pattern")
 
print("select an option:")
print("1.generate a pattern")
print("2.Analyze a range of numbers")
print("3.Exit")

choice=int(input("Enter your choice"))
 
start=int(input("enter the start of your range:"))
end=int(input("enter the end of the range:"))

start = 10
end = 15
total = 0

num=10
if num%2==0:
    print(f"Number{num}is even")
else:
    print(f"number{num}is odd")
total += num


num=11
if num%2==0:
    print(f"Number{num}is even")
else:
    print(f"Number{num}is odd")
total += num


num=12
if num%2==0:
    print(f"Number{num}is even")
else:
    print(f"Number{num}is odd")
total += num

num=13
if num%2==0:
   print(f"Number {num} is even")
else:
    print(f"Number{num}is odd")
total += num

num=14
if num%2==0:
    print(f"Number{num}is even")
else:
    print(f"Number{num}is odd")
total += num

num=15
if num%2==0:
   print(f"Number{num}is even")
else:
    print(f"Number{num}is odd")
total += num

print (f"sum of all numbers from{start}to{end}is:{total}")

print("select an option:")
print("1.generate a pattern")
print("2.Analyze a range of numbers")
print("3.Exit")
 
choice=int(input("enter your choice"))
print("Exiting the programe Goodbye!!")