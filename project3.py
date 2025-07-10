print("welcome to the student data organizer ")

print("select an option:")
print("1.Add student")
print("2.display all student")
print("3.update student information")
print("4.Delete students")
print("5.Display subject offered")
print("6.Exit")

choice=(input("enter your choice:"))
def add_student():
 print("enter student details:")
StudentID=int(input(" Student id:"))
StudentName=input("Name:")
StudentAge=int(input("Age:"))
StudentGrade=(input("Grade"))
StudentDOB=(input("Date of birth (YYYY-MM-DD):"))
StudentSubject=input(" Subjects:")
 
print("\nStudent added successfully!")

print("Select an option:")
print("1.Add student")
print("2.Display all students")
print("...")



 
print("\n....Display all students....")
student=[]
print("\n....Display all students....") 

student = [
    {"ID": 101, "Name": "Alice", "Age": 20, "Grade": "B+", "DOB": "2002-05-14", "Subject": "Math,science,english"},
]

for s in student:
    print(f"StudentID: {s['ID']}, | StudentName: {s['Name']} | StudentAge: {s['Age']} | StudentGrade: {s['Grade']} | StudentsDOB: {s['DOB']} | StudentSubject: {s['Subject']}")

print("....")

print("Select an option:")
choice=int(input("enter your choice"))
print("Exiting the programe Goodbye!!")