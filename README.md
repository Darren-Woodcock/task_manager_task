# task_manager_task
Task Manager in Python. Capstone project
Modify the previous task to use functions for the register user, add task, view 
all and view my tasks sections.

The register user function should be able to check for existing users and not allow
a duplicate to be registered. If attempted an appropriate error message should be 
displayed.

If view my tasks is selected, the display should have a corresponding task number,
which the user can select or use '-1' to return to the menu. The user can then 
choose to edit the task or mark as complete. editing allows only the assigned
user and the due date to be changed. This can only be done if task has not been
marked complete.

Add a new menu input called generate reports, which outputs 2 txt files: 
task_overview.txt and user_overview.txt. 

Modify display statistics option to generate statistics from task_overview.txt
and user_overview.txt files. If the files do not exist, first run generate 
reports option.
