# Module 3
#   Programming Assignment 4
#     Prob-2.py

# <YOUR NAME>

'''
Input(s): workers information-> name, hourly wage, hours.
Process: checking overtime pay, calculating taxes and insurance.  
Output: regular wages, overtime wages taxes, insurance, and take home pay. 
'''


def main():
    # customers inputs
    name = input("Enter your name: ")
    print(name)

    hourly_wage = float(input("Enter your hourly wage: $"))
    print("$", hourly_wage)

    weekly_hours = float(input("How many hours did you work this week?:"))
    print(weekly_hours)

    # find the overtime. weekly hours - 40= overtime
    # total wage is 40 * wage + (overtime * 1.5) * wage

    # calculations for over 40 hours a week
    if weekly_hours > 40:
        reg_pay = 40 * hourly_wage
        print("Regular wage: $", reg_pay)
        overtime_wage = (weekly_hours-40) * hourly_wage * 1.5
        print("Overtime wage: $", overtime_wage)
        total_wages = reg_pay + overtime_wage
        print("Total: $", total_wages)
    # calculations for under 40 hours a week
    elif weekly_hours <= 40:
        regular_pay = hourly_wage * weekly_hours
        total_wages = regular_pay
        print("Regular wage: $", regular_pay)
        print("Overtime wage: $0.00")
        print("Total: $", regular_pay)

    # calculations for tax withholding
    tax = total_wages * 0.2
    print("Tax withholding: $", tax)

    # calculations for insurance withholding
    insurance = total_wages * 0.1
    print("Insurance withholding: $", insurance)

    # Final take home pay
    take_home = total_wages - insurance - tax
    print("Take home pay:$", take_home)


main()
