# entry point to the app


def main():
    # students = 
    while True:
       print('======MENU======')
       print('1. Add Student')
       print('2. Add Scholarship Student')
       print('3. View all Students')
       print('4. Exit ')

       user_choice = (input('Enter your choice: '))

       if (user_choice == '1'):
           ## method to add student
           print('student added sucessfully')
       elif (user_choice == '2'):
           ##method to add scholarship students
           print('scholarship student added sucessfully')
       elif (user_choice == '3'):
            ## Display entries in "students"
            print("******************************")
       elif (user_choice == '4'): 
            status = False
            break # To stop/to exit from the loop,and if proper exit condition is not specified
       else:
            print("Please select a valid choice")
# initialize python project 
if __name__ == "__main__":
    main()