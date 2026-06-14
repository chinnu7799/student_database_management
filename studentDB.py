import json 

FILENAME = "student.json"

def load_students():
    try:
        with open(FILENAME,"r") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    

def add_student(students):
    sid = input("enter studentID: ")
    name = input("enter student name: ")
    age = input("enter age: ")
    course = input("enter course: ")
    marks = input("enter marks: ")
    students.append({
        "id":sid,
        "name":name,
        "age":age,
        "course":course,
        "marks":marks
    })
    print("student added successfuly")


def save_student(students):
    with open(FILENAME,"w") as f:
        json.dump(students,f,indent=4)




def display_students(students):
    if not students:
        print('no student records found')
        return
    print('\n=== STUDENT RECORDS ===')
    for s in students:
        print(f"ID: {s['id']}, name: {s['name']}, age: {s['age']}, course: {s['course']}, marks: {s['marks']}")

def search_students(students):
    sid = input('enter student id')

    for s in students:
        if s['id'] == sid:
            print(f"found --> {s}")
            return
    print('stdent not found')


def update_students(students):
    sid = input('enter student id: ')

    for s in students:
        if s['id'] == sid:
            s['name'] = input('enter a new name: ')
            s['age']  = input('enter new age: ')
            s['course'] = input('enter course name: ')
            s['marks']= input('enter new marks: ')
            

            print('student updated succesfully')
            return
        print('studentid not found')


def delete_students(students):
    sid = input('enter student id to delete: ')

    for s in students:
        if s['id'] == sid:
            students.remove(s)
            print(f"student deleted successfully")
            return
    print('stdent not found')
    




def main():

    students = load_students()
    while True:
        print("\n======= Student menu =======")
        print("1. Add students")
        print("2. Display students")
        print("3. search students")
        print("4. update students")
        print("5. delete students")
        print("6. save and exit")

        choice = input("enter your choice:  ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            update_students(students)
        elif choice == "5":
            delete_students(students)
        elif choice == "6":
            save_student(students)
            print("data saved. exitting program")
        else:
            print("invalid choice try again!")



main()