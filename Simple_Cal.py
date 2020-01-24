import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('===============================[Simple_Cal]===============================')
    InputString = str(input('Run a simple calculation (Yes or No)?  :   '))
    if InputString == str('Yes'):
        NumberOne = int(input('Enter first number                     :   '))
        Operator = str(input('Enter operator (+, -, *, /)            :   '))
        if Operator == (str('+')) or Operator == (str("-")) or Operator == (str("*")) or Operator == (str("/")):
            NumberTwo = int(input('Enter second number                    :   '))
            print('Equation                               :   ', NumberOne, Operator, NumberTwo)
            if Operator == (str('+')):
                print('Answer                                 :  ',NumberOne + NumberTwo)
            elif Operator == (str('-')):
                print('Answer                                 :  ',NumberOne - NumberTwo)
            elif Operator == (str('*')):
                print('Answer                                 :  ',NumberOne * NumberTwo)
            elif Operator == (str('/')):
                print('Answer                                 :  ',NumberOne / NumberTwo)
        else:
            print('Invalid operator!')
    elif InputString != str("Yes"):
        print('User did\'nt input \"Yes!\"')
    print('==========================================================================')
    LoopBreak = input("Run another calculation (Yes or No)?   :  ")
    if LoopBreak != str("Yes"):
        break
    else:
        continue
os.system('cls' if os.name == 'nt' else 'clear')
