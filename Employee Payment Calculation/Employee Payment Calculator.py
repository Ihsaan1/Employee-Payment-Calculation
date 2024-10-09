def startup():

    print("Services: Payment Calculation")
    
    service = input("enter the service you require: ")

    if service == str.casefold("payment calculation"):
        payment()
    else:
        print("This is not a valid service we offer")
        startup()

def payment():
    employee_name = input("enter your name: ")
    employee_position = input("enter your position: ")
    hours_worked = float(input("enter your hours worked this week: "))
    
    normal_pay = hours_worked * 21
    senior_manager_pay = 21 * 5
    manager_pay = 21 * 3
    associate_pay = 21 * 2

    senior_manager = str.casefold("senior manager")
    manager = str.casefold("manager")
    associate = str.casefold("associate")
    
    if employee_position == senior_manager:
        payment = hours_worked * senior_manager_pay
    elif employee_position == manager:
        payment = hours_worked * manager_pay
    elif employee_position == associate:
        payment = hours_worked * associate_pay
    else:
        payment = normal_pay

        
    print("Employee Name: ", employee_name)
    print("Employee Position: ", employee_position)
    print("Employee Wages:", payment)


startup()