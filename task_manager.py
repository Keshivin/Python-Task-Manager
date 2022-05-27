# Here I set boolean values
user_correct = False
password_correct = False
password_confirm = False
user_exit = False
admin = False
main_menu = False

# Here I set variable options for menu
option = ""
register_user = "r  - Register User"
add_task = "a  - Add Task"
all_tasks = "va - View All Tasks"
my_tasks = "vm - View My Tasks"
end = "e  - Exit"
statistics = "s  - Statistics"
task_count = 0
user_count = 0

# Here I set a variable for admin options
admin_options = f"""\nPlease select one of the following options: \n
                {register_user}
                {add_task}
                {all_tasks}
                {my_tasks}
                {statistics}
                {end}"""

# Here I set a variable for user options
user_options = f"""\nPlease select one of the following options: \n
                {all_tasks}
                {my_tasks}
                {end}"""

# Here I open user file
with open(r"user.txt", "r+") as user:
    # Here I assign contents to a variable
    user_contents = user.read()

    # Display Login
    print("\tLogin\n")

    # Here I request username
    username = input("Username: ")

    # if username is found boolean value set to true
    if username in user_contents:
        user_correct = True

    else:
        # Here I create a loop for incorrect username
        while not user_correct:

            # Here I request that user enters username
            username = input("\tIncorrect Username!\nUsername: ")

            # if username is found change the boolean value
            if username in user_contents:
                user_correct = True

    # if user is admin change boolean value
    if username == "admin":
        admin = True

    # if username is correct request password
    if user_correct == True:
        password = input("Password: ")

        # if password is found change boolean value
        if password in user_contents:
            password_correct = True

        # Here I create a loop so that I request user to enter a password if password is false
        while not password_correct:
            password = input("\tIncorrect Password!\nPassword: ")

            # if the password is found change boolean
            if password in user_contents:
                password_correct = True

        # if username and password and username are correct proceed with if loop below
        if user_correct == True and password_correct == True:

            # Here I create a loop to circulate options
            while option != "e":

                # if user is admin display appropriate option
                if admin == True:

                    # Here I display options for admin user
                    print(admin_options)

                # else display appropriate option
                else:
                    print(user_options)

                # Here I assign option a value
                option = input("Selection: ").lower()

                # if option to register task and user is admin
                if option == "r" and admin == True:

                    # open files for instant change
                    with open(r"user.txt", "a") as add_user:

                        # request username and password
                        new_username = input("Username: ")
                        new_password = input("Password: ")
                        new_password_confirm = input("Confirm Password: ")

                        # while confirmation is not valid ask user for confirmation again and type "e" to return to menu
                        while new_password_confirm != new_password:
                            new_password_confirm = input(
                                "\tPasswords do not match!(Type 'e' to return to menu)\nConfirm Password: ")

                            # if new_password_confirm is equal to 'e' or 'E' break loop
                            if new_password_confirm == 'e' or new_password_confirm == 'E':
                                break

                            # elif passwords match change boolean
                            elif password == new_password:
                                confirm_password == True

                            # if password confirmation is change boolean
                        if new_password_confirm == new_password:
                            confirm_password = True

                            # if boolean value is true
                            if confirm_password:
                                # set variable
                                new_user = f"\n{new_username}, {new_password}"

                                # add task to txt
                                add_user.write(new_user)

                # elif option == a
                elif option == "a" and admin == True:

                    # Here I open file user.txt
                    with open(r"user.txt", "r") as check_user:

                        # Here I add contents to variable
                        check_user_contents = check_user.read()

                        # Here I open file tasks.txt
                        with open(r"tasks.txt", "a") as tasks:

                            # Here I request user input for for which user the task is for
                            new_task_user = input("\nEnter user the task is for: ")

                            # if user in user.txt change boolean value to proceed
                            if new_task_user in check_user_contents:
                                user_exists = True

                            # Here I set a loop if user doesn't exist
                            while user_exists == False:

                                # I request for user to input the user the new task is for
                                new_task_user = input("\n\tUser Does Not Exist!\n"
                                                      "(Type 'e' to return to menu)"
                                                      "\nEnter user the task is for: ")

                                # if user enters e or E break loop
                                if new_task_user == "e" or new_task_user == "E":
                                    break

                                # elif user is found change the boolean value to proceed
                                elif new_task_user in check_user_contents:
                                    user_exists = True

                            # if user is found request appropriate information and store in variables
                            if user_exists == True:
                                task_title = input("Enter the title of the task: ")
                                new_task = input(f"Enter {new_task_user}'s new task: ")
                                date_assigned = input("Date task was assigned: ")
                                due_date = input("Due Date: ")
                                full_task = f"\n{new_task_user}, {task_title}, {new_task}, {date_assigned}, {due_date}," \
                                            f"No"

                                # Here I write a new task to txt file
                                tasks.write(full_task)

                # elif user chooses va
                elif option == "va":

                    # Here I open file tasks.txt
                    with open(r"tasks.txt", "r") as view_tasks:

                        # Here I set variable for contents in view_tasks
                        view_tasks_contents = view_tasks.readlines()

                        # Here I set for loop to display tasks in a readable format
                        for line in view_tasks_contents:
                            # Here I set a delimiter
                            line = line.split(",")

                            # Here I display the va information
                            print(f"\n"
                                  f"Name - {line[0]}\nTasks Title - {line[1]}\nTask - {line[2]}"
                                  f"\nDate Assigned - {line[-3]}\nDue Date - {line[-2]}"
                                  f"\nCompleted - {line[-1]}")

                # if user selects "vm"
                elif option == "vm":

                    # open file tasks.txt
                    with open(r"tasks.txt", "r") as view_my_tasks:

                        # Here I set variable for contents in view_my_tasks
                        view_my_tasks = view_my_tasks.readlines()

                        # display which user tasks belong to
                        print(f"\n\t{username}'s Tasks:")

                        # Here I set a for loop to display every task for user
                        for line in view_my_tasks:

                            # Here I set a delimiter
                            line = line.split(",")

                            # if username in line print tasks
                            if username in line:
                                print(f"\nTask Title - {line[1]}\nTask - {line[2]} \nDate Assigned - {line[-3]}"
                                      f"\nDue Date - {line[-2]}")

                # if user selects "s"
                elif option == "s" and admin == True:

                    # Here I set a while loop for continuous referral to stats options
                    while main_menu == False:

                        # Here I request user to input selection
                        stats_input = input("\n\t\tStatistics:\nau - All Users\nat - All Tasks\n"
                                            "m  - Main Menu\n\nSelection: ").lower()

                        # if user selection is "au"
                        if stats_input == "au":

                            # Here I open file user.txt
                            with open(r"user.txt", "r") as stats_users:

                                # Here I set contents in variable stat_users
                                stats_users_contents = stats_users.readlines()

                                # Here I set a for loop to count lines
                                for line in stats_users_contents:
                                    user_count += 1

                            # Here I display total number of users
                            print(f"\n\tTotal number of users is: {user_count}")

                        # if user selection is 'at'
                        elif stats_input == 'at':

                            # Here I open file tasks.txt
                            with open(r"tasks.txt", "r") as stats_tasks:

                                # Here I set contents in variable stats_tasks
                                stats_tasks_contents = stats_tasks.readlines()

                                # Here I set a loop to count lines
                                for lines in stats_tasks_contents:
                                    task_count += 1

                            # Here I display the total number of tasks
                            print(f"\n\tTotal number of tasks is: {task_count}")

                        # elif user selection is "m" break loop
                        elif stats_input == "m":
                            break
