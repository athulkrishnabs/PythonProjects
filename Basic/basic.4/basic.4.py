#Project STUDENT Report System.
#Functions needed: Show Student, Search Student, Add Student, Remove Student, Modify Student, Exit.

Students = {"Alex":{"Age":"24","Course":"Python","Place":"Kerala"},
            "Arun":{"Age":"24","Course":"C++","Place":"Kerala"},
            "Jacob":{"Age":"24","Course":"SQL","Place":"Kerala"}}

while True:
 try:
  choice = int(input("Type: 1-Show, 2-Search, 3-Add, 4-Remove, 5-Modify, 6-Exit:- "))
  
  if choice == 1:                  #Show Students
   for k,v in Students.items():
    print(k,v)


  elif choice == 2:                       #Search Student

   search = input("Enter The Name You Want To Search:- ")
   if search in Students:
    print(f"{search} : {Students[search]}")

   else:
    print("Sorry, This User is not in our database.")

  elif choice == 3:             #Add Student
 
   add_name = input("Enter the Name of the Student:- ")
   if not add_name.isalpha():
    print("Please Enter Only Alphabets !")
   else:
    add_age = input("Enter the Age Of the Student:- ")
    if not add_age.isdigit():
      print("Please Enter Only Numeric Values !")
    else:
      add_course = input("Enter the Course of the Student:- ")
      if not add_course.isalpha():
       print("Please Enter Only Alphabets !")
      else:
       add_place =  input("Enter the Place of the Student:- ") 
       Students[add_name]= {"Age":add_age,"Course":add_course,"Place":add_place}
       print(f"{add_name}:{Students[add_name]}")

   
  elif choice == 4:                     #Remove Student
   remove_student = input("Enter the Name of Student to remove:- ") 
   if remove_student in Students:
    del Students[remove_student]
    print(Students)
   

  elif choice == 5:
   
   search_name = input("Enter the Student Name to Modify:- ")
   if search_name in Students:

    try:
     choice_1 = int(input("Type: 1-Name, 2-Age, 3-Course, 4-Place:- "))

     if choice_1 == 1:
      modify_name = input("Enter New Name:- ")
      if not modify_name.isalpha():
       print("Enter only Alphabets.")
      else:
       Students[modify_name] = Students.pop(search_name)
       print(modify_name,Students[modify_name])
      
     elif choice_1 == 2:
      modify_age = input("Enter New Age:- ")
      if not modify_age.isdigit():
       print("Enter Only Numeral Value!")
      else:
       Students[search_name]["Age"] = modify_age

     elif choice_1 == 3:
      modify_course = input("Enter New Course: ")
      if not modify_course.isalpha():
       print("Enter Only Alphabets !")
      else:
       Students[search_name]["Course"] = modify_course

     elif choice_1 == 4:
      modify_place = input("Enter New Place: ")
      if not modify_place.isalpha():
        print("Enter Only Alphabets!")
      else:
        Students[search_name]["Place"] = modify_place 
       
    
     else:
      print("The Student you want to modify is not in our Database.")   

    except ValueError:
     print("Enter Only Numerical Value") 
   
  elif choice == 6:
    break 


  else:
   print("Choose a Value Between 1-6")

 except ValueError: 
   print("Please Enter Only Numerical Value")
    



    


    





