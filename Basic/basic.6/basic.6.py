import requests

def title_extractor(user_id,limit=None):
 try:   
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    response.raise_for_status()
    data = response.json()

    user_titles = [post["title"] for post in data]
  
    if limit:
     user_titles = user_titles[:limit]

    return user_titles 
    
 except requests.exceptions.RequestException as e:
   print("The error is: ", e)

print(type(title_extractor(1,1)))
while True:
 try:
  ask = int(input("\nEnter the ID you want to search: "))
  titles = title_extractor(ask,5)

  if titles:
    print("\nThe Titles are: ")
    for i,title in enumerate(titles,1):
      print(f"{i}. {title}")
      
    break
  else: 
    print("Please enter a number starting from 1. ")    

 except ValueError:
  print("Please enter a numeric Value! ")




     
    