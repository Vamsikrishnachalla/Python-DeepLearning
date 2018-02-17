contacts = [{"name":'Vamsi', "number":9640423536, "email":"vamsi@gmail.com"},{"name":"Lohit", "number":9908393310, "email":"lohith@gmail.com"},{"name":"haravind","number":7979876756,"email":"haravind@gmail.com"}]

# Letting the user choose from the below options to access the list of contacts
print("Choose from the options below:")
print(" 1. Display the contact by name")
print(" 2. Display the contact by number")
print(" 3. Edit the contact by name")
print(" 4. Exit from the program")
var = int(input("Please enter the function that you ought to choose:"))

if(var==1):
    # Prompting the user to enter the name of the contact to displayed
    name = input("Enter the name to display the contact: ")
    # Moving over all the contacts to match with the entered name
    for q in contacts:
        # To check for the username, whether present in the contacts or not?
        if name in q.values():
            # Printing the name, if present in the list
            print("The contact details associated with the entered name are:","Name of the user:",q["name"], "\n", "Phone number of the user:",q["number"],"\n", "Email of the user:",q["email"])
        else:
            # Username not found in the list
            print("The entered user not found in contacts")

# If user chooses to display the contact by the contact number
elif(var==2):
    # Prompting the user to enter the mobile-number of the user
    pnumb = int(input("Please enter the phone number: "))
    # Checking over the contacts for the matching phone number in the list
    for r in contacts:
        # Checking if the phone number exists in the list:
        if pnumb in r.values():
            # Prnting the contact if condition is true
            print("The contact details associated with the entered number are:","\n","Name of the user:",r["name"], "\n", "Phone number of the user:",r["number"],"\n", "Email of the user:",r["email"])
# If user chooses to edit the contact by name:
elif(var==3):
    # Prompting the user to enter the name of the contact he intends to edit
    user = input("Please enter the name of the user: ")
    # Iterating over the contact_list
    for s in contacts:
        # checking if the user entered value of name whether exists in the contact or not
        if user in s.values():
            # Printing the contact before updating the list
            print(s)
            # Prompting the user to enter the number that he want to update to
            newphone = int(input("Please enter the new phone number:"))
            # Editing the nimber for the particular user
            s["number"] = newphone
            # Printing the contact
            print("The updated contact details:","\n","Name of the user:",s["name"], "\n", "Phone number of the user:",s["number"], "\n", "Email id:",s["email"])

elif(var==4):
    # Exiting the program
    exit()

