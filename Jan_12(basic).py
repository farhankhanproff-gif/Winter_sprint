class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number= roll_number
        self.marks = marks

    def display_info(self):
            print(f"Name: {self.name}")
            print(f"Roll : {self.roll_number}")
            print(f"Marks : {self.marks}")

    def check_result(self):
            status = ''
            if self.marks>40:
                status = "PASS"
            else:
                status = "FAIL"

            print(f"Result : {status}")

try:
     name = input("Enter student name: ")
     roll_number = int(input("Enter student roll number: "))
     marks = int(input("Enter student marks: "))
except ValueError:
     print("Your data type is invalid.")


student1 = Student(name, roll_number, marks)

print("-"*30 + "STUDENT PROFILE" + "-" *30)
student1.display_info()
student1.check_result()
     
     



                

                
            