# Importing the datetime module 
import datetime
from datetime import *

# Function 1: reg_user is called when the user selects 'r' to register a user.

def reg_user(menu):

    if menu == "r":  # Setting if statement for menu_choice.

        new_user = input("Please enter a new username: \n")

        # Checking if the username already exists in the usernames_list.
        while new_user in usernames_list:

            print("The username you entered is already listed.")

            new_user = input("Please enter a new username: \n")

        # If the new username is not already listed, it is added to usernames_list.
        if new_user not in usernames_list:

            usernames_list.append(new_user)

            # The updated list is then updated in the dictionary user_details.
            user_details["Usernames"] = usernames_list

        # The user will then be prompted to enter a password.
        new_password = input("Please enter a new password: \n")

        # The user is asked to confirm their new password.
        pass_confirm = input("Please confirm your new password: \n")

        # If the new and confirmed password values do not match, an appropriate error message is displayed.
        while new_password != pass_confirm:

            print("Your confimed password does not match the original password.")
            new_password = input("Please enter your new password: \n")
            pass_confirm = input("Please confirm your new password: \n")

        # If the new and confirmed password values match, a successful message is displayed.
        if new_password == pass_confirm:

            print("Your password is valid.")

            # The new password is added to the passwords_list.
            passwords_list.append(new_password)

            # The updated list is updated in the dictionary user_details.
            user_details["Passwords"] = passwords_list

            # user.txt file opened to write to.
            with open('user.txt', 'r+') as f:

                # Using for statement to print username and passwords on separate lines.
                # The number of lines is equal to the number of items in usernames_list.
                for i in range(len(usernames_list)):

                        # Writing from the apppropriate dictionary keys, in the correct format.
                       f.write(user_details["Usernames"][i] +
                               ";" + user_details["Passwords"][i] + '\n')

        # Message returned at the end of function.
        return("Your new username and password have been successfully added.")


# Function 2: add_task is called when a user selects 'a' to add a new task.
def add_task(menu):

    if menu == "a":

        import datetime
        from datetime import date

        # Getting user input on the username of the person the task is assigned to.
        name = input(
            "Please enter the username of the person you wish to assign the task to: \n")

        # Getting user input on the title of the task being added.
        title = input("Please enter the title of the task: \n")

        # Getting information regarding the description of the added task.
        descrip = input("Please enter a description of the task: \n")

        # Using the previously imported datetime module today() function to calculate the current date.
        current_date = datetime.date.today()

        # Changing the date object to a string in the correct date format.
        assigned_date = current_date.strftime('%d %m %Y')

        # Getting input on the due date of the task being added.
        date_format = input(
            "Please enter the due date of the task (e.g. dd-mm-yyyy): \n")

        date_list = date_format.split("-")

        numbers_date = [int(x) for x in date_list]

        due_date = date(numbers_date[2], numbers_date[1],
                        numbers_date[0]).strftime('%d %m %Y')

        # task_completed is automatically set to "No" when adding a new task.
        task_completed = "No"

        # Casting all the user input info into a list, to add to the tasks_dict.
        task_list = [name, title, descrip,
            assigned_date, due_date, task_completed]

        tasks_dict[f"Task {count} details:"] = task_list

        # Opening the tasks.txt file to enter the new task information.
        with open('tasks.txt', 'r+') as f2:

            # Printing the list values for each key in tasks_dict to a new line.
            for key in tasks_dict:

                # Casting to a string enabling the info to be written to the file.
                line_string = str(tasks_dict[key])

                bad_chars = ["[", "]", "\'", ]

                # Taking out characters pertaining to previous list/dictionary format.
                for i in bad_chars:

                    line_string = line_string.replace(i, "")

                # Writing the correct format of each string line to the file.
                f2.write(line_string + '\n')

        # Message returned at the end of the function.
        return("Your new task has been added successfully.")

# Function 3: view_all is called when a user selects 'va' to view all tasks listed in tasks.txt.
# These tasks are already stored in the dictionary 'tasks_dict'.
# Therefore, the dictionary will be used to view all the tasks.


def view_all(menu):

    if menu == "va":

        task_count = 0

        for key in tasks_dict:

            task_count += 1

            print(f"""____________________________________________
Task {str(task_count)}:     {str(tasks_dict[key][1])}
Assigned to:            {str(tasks_dict[key][0])}
Date assigned:          {str(tasks_dict[key][3])}
Due Date:               {str(tasks_dict[key][4])}
Task Complete?          {str(tasks_dict[key][5])}
Task Description:
 {str(tasks_dict[key][2])}
________________________________________________""")

    return("End of Tasks.")

# Function 4: view_mine is called when a user selects 'vm' to view all tasks assigned to them.


def view_mine(menu, username):

    if menu == "vm":

        task_count = 0  # Setting a count for number of tasks.

        for key in tasks_dict:

            # calculating the total number of tasks by increasing the count through tasks_dict.
            task_count += 1

            # If the task is assigned to the user, it is displayed.
            if username == (tasks_dict[key][0]):

                print(f"""____________________________________________
Task {str(task_count)}:      \t{str(tasks_dict[key][1])}
Assigned to:        {str(tasks_dict[key][0])}
Date assigned:      {str(tasks_dict[key][3])}
Due Date:           {str(tasks_dict[key][4])}
Task Complete?      {str(tasks_dict[key][5])}
Task Description:
 {str(tasks_dict[key][2])}
________________________________________________""")  # This is a user friendly format with numbered tasks.

    # The user can now choose to either edit a task by number or return to the main menu.
    task_selection = input(
        "\nPlease select a a task by number to edit (e.g. 1, 2,3) or type -1 to return to the main menu. \n")

    # If they select '-1', they return to the outer while loop main menu.
    if task_selection == "-1":

        return(menu)

    else:  # If they enter a task number, they can choose to mark as complete or edit.

       option = input(
           "Would you like to mark the task as complete or edit the task? (e.g. mark OR edit) \n")

       if option == "mark":

           # If they choose to mark, the item linked to that task for completion is changed to 'Yes' in tasks_dict.
           tasks_dict[f"Task {task_selection} details:"][5] = "Yes"

           return("Your task has been successfully marked as complete.")

       # If they choose to edit, the task must be incomplete, i.e. appropriate item in dictionary list equal to 'No'.
       elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "No"):

           #They are given the option to edit username or due date.
           edit_choice = input(
               "Would you like to edit the task username or due date? (Type 'U' or 'D') \n").lower()

           # If they choose to edit the username, they are prompted to enter a new username for the task.
           if edit_choice == "u":

               name_edit = input(
                   "Please enter a new username for the task: \n")

               # The new name is assigned in the dictionary.
               tasks_dict[f"Task {task_selection} details:"][0] = name_edit

               # Successful return message.
               return("The task username has been updated successfully.")

           # If they choose to edit the due date, they are prompted to enter a new date.
           elif edit_choice == "d":

               due_date_change = input(
                   "Please enter a new due date (e.g. 12 May 2020) \n")

               # New date is updated in the tasks_dict.
               tasks_dict[f"Task {task_selection} details:"][4] = due_date_change

               # Sucessful return message.
               return("The due date has been updated successfully.")

       elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "Yes"):

           return("You can only edit tasks that are not already complete. \nChoose 'vm' from menu below to select another task to edit.")


# Function 6: Generating text files 'task_overview.txt' and 'user_overview.txt'.

def generate_reports():

    # Setting blank strings to store info in to be written to the generated text files.
    task_overview = ""
    user_overview = ""

    # Total number of tasks is equal to the key count of tasks_dict.
    tasks_total = len(tasks_dict)

    # Adding a string with the total tasks number to the tas_overview string.
    task_overview = task_overview + \
        f"The total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."

    # Setting variables for integers concerning complete and incomplete tasks 
    x = 0
    y = 0

    for key in tasks_dict:

        # Checking for which tasks are complete by finding the 'Yes' string in each key of tasks_dict.
        if tasks_dict[key][5] == "Yes":

            # If the task is complete, i.e. 'Yes' string item is present, variable x is increased by 1.
            x += 1

        # Checking for which tasks are complete by finding the 'No' string in each key of tasks_dict.
        elif tasks_dict[key][5] == "No":

           # If the task is complete, i.e. 'No' string item is present, variable y is increased by 1.
           y += 1


    # All of the numbers calculated above are now built into sentences in the task_overview string.
    # Percentages are also calculated within the f-strings added, with the results being rounded to 2 decimal places and cast into strings into sentences.
    task_overview = task_overview + \
        f"\nThe total number of completed tasks is {str(x)}." + \
                                                        f"\nThe total number of incomplete tasks is {str(y)}."
    task_overview = task_overview + \
        f"\nThe percentage of incomplete tasks is {str(round((y / len(tasks_dict)) * 100, 2))}%."

    # Now generating a 'task_overview' file.
    # The task_overview string is then written to the file in an easy to read format.
    with open('task_overview.txt', 'w') as f3:

        f3.write(task_overview)

    # Setting variables to store information regarding total users and complete tasks for a user
    a = 0
    b = 0
    c = 0

    for key in tasks_dict:

        # Counting the number of tasks assigned to the user by identifying the first list item.
        if tasks_dict[key][0] == username:

            # Integer 'a' is increased by 1 if the task is for the user.
            a += 1

        # Checking if the task for the user is complete.
        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "Yes":

           b += 1  # Integer 'b' is increased by 1 if the task is complete.

        # Checking if the task for the user is incomplete.
        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "No":

            c += 1  # Integer 'c' is increased by 1 if the task is incomplete.


    # Writing all the info calculated above into sentence strings which are built into the user_overview string variable.
    user_overview = user_overview + \
        f"The total number of users registered with task_manager.py is {str(len(user_details))}."
    user_overview = user_overview + \
        f"\nThe total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."
    user_overview = user_overview + \
        f"\nThe total number of tasks assigned to {username} is {str(a)}."
    user_overview = user_overview + \
        f"\nThe percentage of the total number of tasks assigned to {username} is {str(round((a / len(tasks_dict)) * 100, 2))}%."
    user_overview = user_overview + \
        f"\nThe percentage of tasks assigned to {username} that have been completed is {str(round((b / a) * 100, 2))}%."
    user_overview = user_overview + \
        f"\nThe percentage of tasks still to be completed by {username} is {str(round((c / a) * 100, 2))}%."

    # Now generating a 'user_overview' file.
    # The user_overview string is then written to the file in an easy to read format.
    with open('user_overview.txt', 'w') as f4:

        f4.write(user_overview)

    # The user then views a message stating that their reports have been successfully generated.
    return("Your reports have been generated successfully.")


# Writing the program.
# Firstly, I will build the current info from tasks.txt and user.txt into appropriate lists and dictionaries.

user_details = {}

# The user details dictionary will be built with lists from 'usernames_list' and 'passwords_list' as values.
usernames_list = []
passwords_list = []

tasks_dict = {}

# Opening the tasks.txt file to read and write information from it.
# Adding the info in the user.txt file into the set list.
with open('user.txt', 'r+') as f:

    for line in f:

        # Stripping newline characters from the line.
        newline = line.rstrip('\n')

        split_line = newline.split(";")  # Splitting the line into a list.

        # Assigning items from the list into corresponding list.
        usernames_list.append(split_line[0])
        passwords_list.append(split_line[1])

        # Lists are now stored as values assigned to keys in user_details dictionary.
        user_details["Usernames"] = usernames_list
        user_details["Passwords"] = passwords_list


# Setting a count to keep track of the number of lines in the tasks.txt file.
count = 1

# Opening the tasks.txt file to read and write information to it.
with open('tasks.txt', 'r+') as f2:

    for line in f2:

        newline = line.rstrip('\n')  # Stripping newline characters.

        # Splitting line into a list of items.
        split_line = newline.split(", ")

        # Assigning each list of items to a key in tasks_dict.
        tasks_dict[f"Task {count} details:"] = split_line

        count += 1  # Count used to change key value for each list of info.


# Getting input from the user on their login details.
username = input("Please enter your username: \n")
password = input("Please enter your password: \n")

# Creating a while loop to run indefinitely whilst login details are incorrect.
# Appropriate error messages are displayed.
# Use of the words 'in' and 'not in' used to test whether the username and password appear in the appropriate lists.
while (username not in usernames_list) or (password not in passwords_list):

       # If username is correct and password is correct, the following message is displayed.
       if (username not in usernames_list) and (password in passwords_list):

            print("Your username is not listed.")

            # User is prompted to re-enter details.
            username = input("Please re-enter your username: \n")
            password = input("Please re-enter your password: \n")

        # If password is incorrect and username is correct, the following message is displayed.
       elif (password not in passwords_list) and (username in usernames_list):

            print("Your password is incorrect.")

            username = input("Please re-enter your username: \n")
            password = input("Please re-enter your password: \n")

        # If both the username and password are incorrect, the following message is displayed.
       elif (username not in usernames_list) and (password not in passwords_list):

            print("Your username and password are incorrect.")

            username = input("Please re-enter your username: \n")
            password = input("Please re-enter your password: \n")

# If both username and password are correct, the successful login message is displayed.
if (username in usernames_list) and (password in passwords_list):

    print("You are successfully logged in.")


# Indefinite loop created to display the menu once the user is logged in.
# This allows the user to return to the menu after each option.
# If they wish to exit the program, they can choose the 'exit' option from the menu.
while 1:

    # The admin user views a specific menu with extra options (gr and ds).
    if username == "admin":

        menu = input("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
""").lower()

    else:  # All other users can only view the basic menu.

       menu = input("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
e - exit
""").lower()

    if menu == "r":  # Choosing 'r' from the menu causes the reg_user function to be called.

        print(reg_user(menu))

    elif menu == "a":

        print(add_task(menu))

    elif menu == "va":  # Choosing 'va' from the menu causes the view_all function to be called.

        print(view_all(menu))

    # Choosing 'vm' from the menu causes the view_mine function to be called.
    elif menu == "vm":

       print(view_mine(menu, username))

    # Choosing 'gr' from the menu causes text files user_overview and task_overview to be generated.
    elif menu == "gr":

        print(generate_reports())  # Calling function to generate report files.

    elif menu == 'ds':

        # Calling function generate files in case they do no exist yet.
        print(generate_reports())

        print("""\n____________________________________________________
The task overview report is as follows:
____________________________________________________\n""")  # Heading printed for user-friendly display.

        # Opening the task_overview file to get info from it.
        with open('task_overview.txt', 'r+') as f3:

            for line in f3:

                print(line)  # Printing/displaying each line in the file.

        print("""\n_____________________________________________________
The user overview report is as follows:
_____________________________________________________\n""")  # Heading printed for user_friendly display.

        # Opening user_overview file.
        with open('user_overview.txt', 'r+') as f4:

            for line in f4:

                print(line)  # Displaying each line of the file.

        print("""\n______________________________________________________
End of Statistics Reports
______________________________________________________\n""")  # End of reports display.

    elif menu == "e":  # If the user selects 'e' they can log out of the program.

        print("You are successfully logged out.")

        break  # break statement ends the infinte while loop to exit the program.
