print('''
Welcome to saint john's Northwestern Millitary academy!
This is your Academic Planner program that will help you keep
your assignments in line!

''')

homework_to_do = []
homework_due_dates = []


quiz_test = []
quiz_test_due_dates = []


while True:
    #code goes here

    choice = int(input('''please enter a choice
    1) Add homework
    2) Add quiz/test
    3) Display homework, quizzes and tests
    '''))

    if choice == 1:
        homework = input("what homework do you need to add?: ")
        homework_to_do.append(homework)
        date = input("when is this due by?")
        homework_due_dates.append(date)
    elif choice == 2:
        quiz_test_added = input("what quiz/test do you need to add?: ")
        quiz_test.append(quiz_test_added)
        quiz_test_due = input("When is your quiz/test due by?")
        quiz_test_due_dates.append(quiz_test_due)
    elif choice == 3:
        
        
        
        
        print("The following is you homework")
        print(homework_to_do)
        print(homework_due_dates)

        print("The following is your quizzes/tests")
        print(quiz_test)
        print(quiz_test_due_dates)


