tasks = ["Sleeping","Eating","Jogging"]
                      #Add A Task, Remove a Task, Modify a Task, Exit, Invalid option.


while True:
 choice = input("1= Show Task, 2= Add Task, 3= Remove Task, 4= Modify Task, 5= Exit:- ")
 try:
  options = int(choice)
  
 except ValueError:
  print ("Enter Numeric values only.!") 
  continue
  

 if options == 1:
   print(tasks)
   

 elif options == 2:
   add_task = input("Enter the Task you want to Add: ")
   tasks.append(add_task)
   print(tasks)
   

  
 elif options == 3:
   remove_tasks = input("Enter the Task you want to Remove: ")
   if remove_tasks in tasks:
    tasks.remove(remove_tasks)
    print(tasks)
   
   else: 
    print("Task Not Found!")


 elif options == 4:
   modify_tasks_finder = input("Enter the Task, you want to Modify: ")
   if modify_tasks_finder in tasks:
     position = tasks.index(modify_tasks_finder)
     modify_var = input("Enter what to modify: ")
     tasks[position] = modify_var
     print (tasks)
     
   else:
    print("The Task is not found")

 elif options == 5:
   break   

 else:
     print("Choose the right option(1-5)")

    



   
 