usernames=['Ibhav','Harsh','Komal','Jetha','Manoj','Pashuram','Admin']
entered='Ibhav'
if usernames==[]:
        for username in usernames:
                print("All ok")

        else:
                print("We need to find users")

if entered.lower()=='admin':
        print("Hello admin, Would you like to see status report")
else:
        print(f"Welcome, {entered}!")

        # Check if the entered username is in the list of usernames
        if entered.lower() in usernames:
                print(f"Welcome, {entered}!")
        else:
                print("Invalid username!")

        # Check if the entered username is 'admin'
        if entered.lower() == 'admin':
                print("Hello admin, Would you like to see status report")