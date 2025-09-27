contacts = {"alex":"789654123","sudev":"5665522","antony":"85122222"}

def add_contacts():
    name = input("Enter Name: ")
    number = input("Enter Number: ")
    contacts[name]=number
    print(f"{name} Phone number is {number}")

def show_contacts():
    for k,y in sorted(contacts.items()):
        print(f"{k}'s number is {y}")

def de_contacts():
    name = input("Enter Name: ")
    if name in contacts:
        contacts.pop(name)
        print(f"{name} is deleted from the contact book")
    else:
        print(f"Sorry, {name} not in contacts")    
   
    print(f"\nPlease Verify the list: {contacts}")

while True:
    Welcome = input("Welcome, Type 1-ADD/UPDATE, 2-DELETE, 3-SHOW, 4-EXIT:- ")
    if Welcome == "1":
        add_contacts()
    elif Welcome == "2":
        de_contacts()
    elif Welcome == "3":
        show_contacts()
    elif Welcome == "4":
        break
    else:
        print("Sorry Sir, Request Invalid")



        

