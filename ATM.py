message =" please choose your option 1-->check balance , 2--->deposite amount 3-->withdral"
print(message)
task=int(input('select your option Sir/Mam:'))
available_balance = 5059

if (task >=1) and (task<=3):
    # 1 balnce
    # 2 deposite
    # 3 withdrwal
    if task == 1:
    # 1 balnce
     check_message = f"Your availabe balance is:-{available_balance}"
     print(check_message)
    elif task == 2:

    # deposite  
        deposite_amount = int(input('please enter the amount:'))
        if  deposite_amount > 0:
            available_balance += deposite_amount
            print('ypur amount success fully deposite')
            check_message = f"your balance is :-{available_balance}"
            print(check_message)
        else:
            print('please give your valuable amont') 
    else:
        withdrwal_amount = int(input('please enter your withdrawl:-'))
        if withdrwal_amount <= available_balance:
            available_balance -= withdrwal_amount
            print('you have succesfully withdrawl your amount')
            check_message = f"your available balance is :-{available_balance}"
            print(check_message)
else:
    print('please choose corect option')       
         