current_users=['Ibhav','cat','dog','monkey']
new_users=['monkey','cat','lion','fish']
for new_user in new_users:
    if new_user in current_users:
        print("Unavalable")

    else:
        print("Available")

        # Check if the new user is already in the list of current users
        if new_user in current_users:
            print("Unavailable")  # If the new user is already taken, print "Unavailable"
        else:
            print("Available")  # If the new user is available, print "Available"