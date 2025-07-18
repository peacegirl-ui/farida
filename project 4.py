print("Welcome to the data analyzer and transformer program")

choice=int(input("Enter your choice"))
data_str = input("Enter data for a 1D array (separated by spaces): ")
data_list = [int(x) for x in data_str.split()]
print("Data has been stored successfully! ")
        

# def display_summary(data): 
#     print(f"Total elements: {len(data)}")
#     print(f"Min value: {min(data)}")
#     print(f"Max value: {max(data)}")
#     print(f"Sum of all values: {sum(data)}")

#     display_summary(data)............................................................ NOT DONE    

# without function:-
print("display_summary")
data=[ 34,12,56,78,43,21,90]

len_data=len(data)
min_value=min(data)
max_value=max(data)
sum_value=sum(data)
Average_value=sum_value/len(data)

print("len_data:",len_data)
print("Minimum_value:",min_value)
print("Maximum_value:",max_value)
print("sum of all value:",sum_value)
print("Average_value:",Average_value)

# print("3.calculate factorial")
choice=int(input("enter your choice:"))

num=int(input("Enter a number to calculate its factorial:"))
n=5
factorial=1
i=1
while i<=n:
   factorial*=i
   i+=1
print("Factorial of", n, "is", factorial)

print("4.filter data by threshold...")
choice=int(input("enter your choice:"))
num1=int(input("enter a threshold value to filter out data above this value:"))
data=[12,21,34,43,56,78,90]
Threshold=50
filtered_data=[]
for num in data:
   if num>=50:
      filtered_data.append(num)
      print(filtered_data)

# another example
data=[5,2,8,9,1,7]
threshold=5
filtered_data=[]
for num in data:
   if num>=5:
      filtered_data.append(num)
      print(filtered_data)

print("5.sort data")
choice=int(input("enter your choice:"))

print("Choose sorting option")
print("1. Ascending:") 
print("2. Descending :")

choice=int(input("enter your choice:"))
list=[21,12,34,43,78,56,90]
list.sort()
print(list)

print("6.display data set statistics")
choice=int(input("enter your choice:"))
Data=[12,21,34,43,56,78,90]

min_value=min(Data)
max_value=max(Data)
sum_value=sum(Data)
Average_value=sum_value/len(Data)

print("Minimum_value:",min_value)
print("Maximum_value:",max_value)
print("sum of all value:",sum_value)
print("Average_value:",Average_value)