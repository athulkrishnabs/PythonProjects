def divider(d):
  return 100/d                                
   #1.)Ask the user for a number, divide 100 by it, handle division by zero or invalid input.              
while True:
  try:  
    number= int(input("Please enter The Number to divide 100 with:-  "))
    print(f"This is the answer: {divider(number)}")
    break
  except ZeroDivisionError:
    print("Hey, Please enter a number other Than zero")
  except ValueError:
    print("Hey, Please enter a numeric value") 

#2.)Ask user for a key in a dictionary, handle invalid keys.

fav_movie_ratings = {"Spiderman":"8.5","Batman":"9","Ironman":"10","Superman":"8"}

def fav(f):
  return fav_movie_ratings[f]

while True:
  search = input("Enter The Name Of The Movie You Want To Search:- ")
  if not search.isalpha():
     print("Hey, Please enter the film name in alphabets")
     continue
  try:
    print(f"The Rating For The Film {search} is {fav(search)}")
    break

  except KeyError:
    print("The Film you searched cannot be found in our database.")

#3.)Try opening a file that might not exist, handle the error gracefully.

search = input("Enter the file name you want to search:- ")

try:
  with open(search,"r") as h:
    content = h.read() 
    print(content)
except FileNotFoundError:
  print("Sorry Dude,Your File Ran away!! :(")    


    
    


 
  

