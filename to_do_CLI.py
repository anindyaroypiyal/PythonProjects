import dbh
import os

def showTasks():
    print ( "\nID\t\tTasks\n" )
    for rows in dbh.showdb () :
        print ( rows[0], '\t\t', rows[1] )

print("HOW MAY I BE USEFUL TODAY ?")
while True:
    ch = int ( input ( "(Choose an option)\n\t 1. View Tasks\n\t 2. Add task\n\t 3. Delete Task\n\t 4. QUIT\n" ) )

    if ch == 1:
        # os.system("clear")
        showTasks()
        print()
        continue
    elif ch == 2:
        os.system("cls")
        task = input("Enter a task:  ")
        if len(task) != 0:
            dbh.insertTask(task)
        showTasks()
        print()
        continue
    elif ch == 3:
        try:
            dlt = int(input("Enter the ID of the task you wish to delete:  "))
        except:
            print("enter valid id")
            continue
        dbh.deletyById(dlt)
        showTasks()
        continue
    elif ch == 4:
        print("OK, Thank you <3")
        break
    else:
        print("Choose a valid option")
        continue
