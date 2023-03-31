import math

print('''Choose 'Investment' or 'Bond' from the menu below to proceed:
Investment - to calculate the amount of interest you'll earn in interest
Bond - to calculate the amount you'll have to pay on a home loan''')

question = input(f"\nEnter either 'investment' or 'bond' from the menu above to proceed:").lower()

#Calculating simple and compound investment.
if question == 'investment':
    while True:
        try:
            P = int(input("Enter the amount of money you are depositing: "))
            r = float(input("Enter interest rate (only a number): "))
            r = r / 100
            t = int(input("Enter the number of years you plan on investing: "))
            it = input("Do you want a simple/compound interest: ").lower()

            if it == 'simple':
                answer = P*(1 + r * t)
                total = answer
                print(f"""\nAmount: £{P}
Rate of Interest (per annum): {r}
Time (in years): {t}
Final Amount: £{total.__round__()}""")
                y_n = input("Would you like to run another calculation y/n:")
                if y_n == 'n':
                    break
            elif it:
                answer = P* math.pow((1+r),t )
                total = answer
                print(f"""\nAmount: £{P}
Rate of Interest (per annum): {r}
Time (in years): {t}
Final Amount: £{total.__round__()}""")
                y_n = input("Would you like to run another calculation y/n:")
                if y_n == 'n':
                    break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue


#Calculating bond option.
elif question == 'bond':
    while True:
        try:
            P = int(input("What is the current house value: "))
            i = float(input("Enter interest rate: "))
            i = i / 100
            rp = int(input("In how many months you plan to repay: "))
            monthly = (i * P) / (1 - (1 + i) ** (-rp))
            print(f"""\nCurrent house value: £{P}
Interest rate: {i}
Number of installments: {rp}
Monthly Repayments: £{monthly.__round__()}""")
            y_n = input("Would you like to run another calculation y/n:")
            if y_n == 'n':
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue