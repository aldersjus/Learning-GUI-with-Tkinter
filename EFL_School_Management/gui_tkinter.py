from tkinter import *
from english_school_code import *
import pickle

pickled_data = []
school_created = False
students = []
student_data = {}
classes = {}
all_students = []
all_classes = []
temp = [" ", " "]
add = False
info = False

try:
    with open('save.txt','rb') as file:
        pickled_data = pickle.load(file)
        school_created = pickled_data[2]
        
except EOFError:
    print("File empty")
    school_created = False
        
if school_created == False:
    name = input("Please enter the name of your school: ")
    name = name.capitalize()
    pickled_data.insert(0,name)
    name = School(name)
    saved_name = name
    pickled_data.insert(1,saved_name)
    school_created = True
    saved_school = school_created
    pickled_data.insert(2,saved_school)

elif school_created == True:
    name = pickled_data[0]
    saved_name = pickled_data[1]
    saved_school_name = pickled_data[2]
    student_data = pickled_data[3]
    students = pickled_data[4]
    classes = pickled_data[5]
    all_students = pickled_data[6]
    all_classes = pickled_data[7]
    
def gui():
    window = Tk()
    window.title("Cocoon Software")
    window.geometry("860x450")
    #window.wm_iconbitmap("who.ico")
    window.configure(background="powder blue")
    
    photo = PhotoImage(file="me.gif")
    photo_label = Label(window, image=photo, bg="powder blue")
    
    text = Text(window, height=7, width=107)
    text_two = Text(window, height=4, width=50)

    label = Label(window, text=name+" English Language School", font="Verdana 20 bold", bg="powder blue")
    label_two = Label(window, text="Enter details below", font="Verdana 10 bold", bg="powder blue")
    label_three = Label(window, text="Details will be displayed in the box below", font="Verdana 10 bold", bg="powder blue")
    label_four = Label(window, text="Please select your options from the list below", font="Verdana 10 bold", bg="powder blue")
    label_five = Label(window, text="Requested information will be displayed below", font="Verdana 10 bold", bg="powder blue")

    entry_text = StringVar()
    entry = Entry(window, textvariable=entry_text, width=50)
    
    listbox = Listbox(window, height=9, width=50, selectmode=SINGLE)

    def save():
         with open('save.txt','wb') as file:
                pickled_data.insert(3,student_data)
                pickled_data.insert(4,students)
                pickled_data.insert(5,classes)
                pickled_data.insert(6,all_students)
                pickled_data.insert(7,all_classes)
                pickle.dump(pickled_data,file)
                
    def enter_student(argument):
        entry.bind("<Return>", enter_student)
        student = entry.get()
        if student > " ":
            student = student.lower()
            student_name = student.capitalize()
            if student in student_data:  # Is student in student_data.
                    text_two.delete(1.0, END)
                    text_two.insert(END, "Please choose a new name, that student alredy exsists.")
            elif student not in student_data:  # Is not in student_data.
                    text_two.delete(1.0, END)
                    text_two.insert(END, "Student created: " + student_name)
                    all_students.append(student)
                    new_student = Student(student)
                    student_data[student] = new_student
                    save()


    def add_student_data(argument):
        global name_of
        global add
        entry.bind("<Return>",add_student_data)
        name_of = entry.get()
        name_of = name_of.lower()
        if name_of > " " and add == False:
            if name_of in student_data:
                temp.append(name_of)
                add = True
                add_student_data(argument)
                text_two.delete(1.0, END)
                text_two.insert(END, "Enter the information: ")
                entry.delete(0, END)
            elif name_of not in student_data:
                entry.delete(0,END)
                text_two.delete(1.0,END)
                text_two.insert(END,"No such student in this school!")
        elif name_of not in temp and add == True:
            text_two.delete(1.0,END)
            temp.append(name_of)
            student_data[temp[-2]].add_info(temp[-1])
            text_two.insert(END, "Student information updated")
            entry.delete(0,END)
            add = False
            save()

    def see_student_data(argument):
        entry.bind("<Return>",see_student_data)
        name_of_student = entry.get()
        name_of_student = name_of_student.lower()
        if name_of_student > " ":
            if name_of_student in student_data:
                text.delete(1.0, END)
                nam = student_data[name_of_student].student
                namCap = nam.capitalize()
                text.insert(END, namCap + ": ")
                inf = student_data[name_of_student].my_info
                for item in inf:
                    infStu = item.capitalize()
                    text.insert(END, " " + infStu + ",")
            elif name_of_student not in student_data:
                text_two.delete(1.0, END)
                text_two.insert(END,"No such student in this school!")
        
    def add_class(argument):
        entry.bind("<Return>",add_class)
        new_class = entry.get()
        new_class = new_class.lower()
        if new_class > " ":
            append_new_class = new_class
            if new_class in classes:#Is student in student_data.
                text_two.delete(1.0, END)
                text_two.insert(END,"Please choose a new name, that class already exists.")
            elif new_class not in classes:#Is not in student_data.
                all_classes.append(append_new_class)
                class_created = Lesson(new_class)
                classes[new_class] = class_created
                cap = new_class
                classCap = cap.capitalize()
                text_two.delete(1.0, END)
                text_two.insert(END,"Class created: " + classCap)
                save()

    def mark_off_class(argument):
        global name_of
        global add
        entry.bind("<Return>",mark_off_class)
        name_of = entry.get()
        name_of = name_of.lower()
        if name_of > " " and add == False:
            if name_of in classes:
                temp.append(name_of)
                add = True
                mark_off_class(argument)
                text_two.delete(1.0,END)
                text_two.insert(END,"Enter the information: ")
                entry.delete(0,END)
            elif name_of not in classes:
                entry.delete(0,END)
                text_two.delete(1.0,END)
                text_two.insert(END,"No such class in this school!")
        elif name_of not in temp and add == True:
            text_two.delete(1.0,END)
            temp.append(name_of)
            classes[temp[-2]].add_lessons_taken(temp[-1])
            text_two.insert(END, "Class information updated")
            entry.delete(0,END)
            add = False
            save()
    
    def add_student_to_class(argument):
        global name_of
        global add
        entry.bind("<Return>",add_student_to_class)
        name_of = entry.get()
        name_of = name_of.lower()
        if name_of > " " and add == False:
            if name_of in classes:
                temp.append(name_of)
                add = True
                add_student_to_class(argument)
                text_two.delete(1.0,END)
                text_two.insert(END,"Enter the name of student: ")
                entry.delete(0,END)
            elif name_of not in classes:
                entry.delete(0,END)
                text_two.delete(1.0,END)
                text_two.insert(END,"No such class in this school!")
        elif name_of not in temp and add == True:
            text_two.delete(1.0,END)
            temp.append(name_of)
            classes[temp[-2]].add_student(temp[-1])
            text_two.insert(END, "Class information updated, please ensure student \nhas been added to school database.")
            entry.delete(0,END)
            add = False
            save()
       
    def see_class_data(argument):
        entry.bind("<Return>",see_class_data)
        print_off = entry.get()
        print_off = print_off.lower()
        if print_off > " ":
            if print_off not in classes:
                text_two.insert(END,"That class has not been created yet, see choice 8.")
            elif print_off in classes:
                text.insert(END,"Class day/name: ")
                day = classes[print_off].class_name
                capDay = day.capitalize()
                text.insert(END,capDay)
                text.insert(END, "\n")
                text.insert(END,"Students: ")
                stus = classes[print_off].students_in_class
                for item in stus:
                    inStu = item.capitalize()
                    text.insert(END, " " + inStu + ",")
                text.insert(END, "\n")
                text.insert(END,"Lessosns taken: ")
                less = classes[print_off].lessons_taken
                for item in less:
                    capLess = item.capitalize()
                    text.insert(END, " " + capLess + ",")
               
    def see_lesson_data(argument):
        entry.bind("<Return>",see_lesson_data)
        print_lessons = entry.get()
        print_lessons = print_lessons.lower() 
        if print_lessons > " ":     
            if print_lessons not in classes:
                text_two.insert(END,"That class has not been created yet.")
            elif print_lessons in classes:
                text.insert(END,"Lessons taken: ")
                less = classes[print_lessons].lessons_taken
                for item in less:
                    capLess = item.capitalize()
                    text.insert(END, " " + capLess + ",")
                      
         
    def working(argument):
        entry.delete(0, END)
        text.delete(1.0,END)
        text_two.delete(1.0,END)
        choice = listbox.curselection()[0]

        if choice == 0:
            text_two.insert(END,"Please enter student`s name above.")
            enter_student(argument)
                          
        elif choice == 1:
            text_two.insert(END, "Please enter student`s name above.")
            add_student_data(argument)

        elif choice == 2:
            text_two.insert(END,"Enter the name of the student: ")
            see_student_data(argument)
          
        elif choice == 3:
            text_two.insert(END,"Enter the name of the class: ")
            mark_off_class(argument)

        elif choice == 4:
            text_two.insert(END,"Enter the name of the class: ")
            see_class_data(argument)

        elif choice == 5:
            text_two.insert(END,"Enter the name of the class: ")
            see_lesson_data(argument)

        elif choice == 6:
            text_two.insert(END,"Enter the name of the class: ")
            add_student_to_class(argument)

        elif choice == 7:
            text_two.insert(END, "Please enter name of class: ")
            add_class(argument)
       
        elif choice == 8:
            text.delete(1.0, END)
            text.insert(END, "Students: ")
            for student in all_students:
                stu = student.capitalize()
                text.insert(END, " " + stu + ", ")
            text.insert(END, "\n")
            text.insert(END, "Classes: ")
            for classes in all_classes:
                cla = classes.capitalize()
                text.insert(END, " " + cla + ", ")
            

    a = "Please select  to add a new student. "
    b = "Please select  to add student details." 
    c = "Please select  to view student information." 
    d = "Please select  to mark off a class."
    e = "Please select  to print class information."
    f = "Please select  to show lessons taken by a class."
    g = "Please select  to add a student to a class."
    h = "Please select  to create a new class."
    i = "Please select  to print school data base."
    
    for item in [a,b,c,d,e,f,g,h,i]:
        listbox.insert(END, item)
    
    listbox.bind('<<ListboxSelect>>', working)
    label.place(x=50, y=20)
    label_four.place(x=50,y=75)
    listbox.place(x=50,y=100)
    text_two.place(x=450, y=220)
    label_two.place(x=450,y=140)
    entry.place(x=450,y=160)
    label_three.place(x=450,y=190)
    text.place(x=50,y=320)
    label_five.place(x=50, y=290)
    text.insert(END, name)
    photo_label.place(x=675, y=10)
    mainloop()

if __name__ == "__main__":
    gui()
    

