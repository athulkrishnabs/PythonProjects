def divider(d):
  return 100/d                                
   #1.)Ask the user for a number, divide 100 by it, handle division by zero or invalid input.              
while True:
  try:  
    number= int(input("Please enter The Number:-  "))
    print(f"This is the answer: {divider(number)}")
    break
  except ZeroDivisionError:
    print("Hey, Please enter a number other Than zero")
  except ValueError:
    print("Hey, Please enter a numeric value") 


