print('''
Welcome to saint john's Northwestern Millitary academy!
This is your Academic Planner program that will help you keep
your assignments in line!

''')

homework_to_do = []
homework_due_dates = []


quiz/test = []
quiz/test_due_dates = []


while True:
    #code goes here

choice = int(input('''please enter a choice
1) Add homework
2) Add quiz/test
3) Display homework, quizzes and tests
'''))

if choice == 1:
    print("what homework do you need to add?: ")
elif choice == 2:
    print("what quiz/test do you need to add?: ")
elif choice == 3:
    print("The following is you homework")
    print(homework_to_do)
    print(homework_due_dates)

    print("The following is your quizzes/tests")
    print(quiz/test)
    print(quiz/test_due_dates)


