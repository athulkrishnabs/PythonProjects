#Function that classifies a score into grades

def classifier(n):
    if n >= 90:
      return (f"Hey You Have Scored {n}marks and Your Grade is: A")
    elif n >= 70:
      return (f"Hey You Have Scored {n}marks and Your Grade is: B") 
    elif n >= 50:
      return (f"Hey You Have Scored {n}marks and Your Grade is: C")
    else:
      return (f"Hey You Have Scored {n}marks and Your Grade is: F") 


while True:       
   try:
      marks = int(input("Please Enter Your Grades Here: "))
      print(classifier(marks))
      break 
   except ValueError:
      print("Invalid input Please enter only numbers")