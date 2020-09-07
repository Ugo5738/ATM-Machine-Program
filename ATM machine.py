print('Welcome to Zenith Bank ATM')
restart = 'Yes'
chances = 3
balance = 40000.64
while chances >= 0:
    pin = int(input('\nPlease Enter Your 4 Digit Pin: \n'))
    if pin == 1234:
        print('You entered your pin correctly')
        while restart not in ('n', 'no', 'N', 'NO'):
            print('\nPlease Press 1 for your balance')
            print('Please Press 2 to make withdrawal')
            print('Please Press 3 to pay in')
            print('Please Press 4 to return card\n')
            option = int(input('What option would you like to choose? \n'))
            if option == 1:
                print(f'Your Account Balance is N{balance}\n')
                restart = input('Would you like to do another transaction? \n')
                if restart in ('n', 'no', 'N', 'NO'):
                    print('Thank you')
                    break
            elif option == 2:
                option_2 = 'y'
                withdrawal = float(input('How much would you like to withdraw? \nN500, N1000, N2000, N5000, N10,000, N20,000: \n'))
                if withdrawal in [500, 1000, 2000, 5000, 10000, 20000]:
                    balance = balance - withdrawal
                    print(f'Your balance is now N{balance}\n')
                    restart = input('Would you like to do another transaction? ')
                    if restart in ('n', 'no', 'N', 'NO'):
                        print('Thank you')
                        break
                elif withdrawal != [500, 1000, 2000, 5000, 10000, 20000]:
                    print('Invalid amount, Please Retry')
                    restart = 'y'
                elif withdrawal == 1:
                    withdrawal = float(input('Please Enter Desired Amount: '))
            elif option == 3:
                pay_in = float(input('How much would you like to pay in? '))
                balance = balance + pay_in
                print(f'Your balance now is N{balance}\n')
                restart = input('Would you like to do another transaction? ')
                if restart in ('n', 'no', 'N', 'NO'):
                    print('Thank you')
                    break
            elif option == 4:
                print('Please wait whilst your card is returned...\n')
                print('Thank you for your service\n')
                break
            else:
                print('Please enter a correct number. \n')
                restart = 'y'
    elif pin != '1234':
        print('Incorrect Password.')
        chances = chances - 1
        if chances == 0:
            print('No more tries')
            break