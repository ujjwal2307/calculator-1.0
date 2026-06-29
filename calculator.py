def ans(value):
    return f"Your answer is: {value}\nNext question:"

while True:
    #Variables
    a=int(input("Enter 1st number: ").strip())
    b=int(input("Enter 2nd number: ").strip())
    print("To add enter \'+\'      |  To subtract enter \'-\'\nTo multipy enter \'*\'  |  To divide enter \'/\'\nTo get the reminder after division enter \'%\'\nTo get exponent, enter '**'\nTo exit, enter 'exit' |  To return to 1st number, enter 'return' ")
    c=input("Enter ARITHMETIC OPERATOR: ".strip().lower())
    if c=='+':
        print(ans(a+b))
    elif c=='-':
        print(ans(a-b))
    elif c=='*':
        print(ans(a*b))
    elif c=='**':
        print(ans(a**b))
    elif c=='/':
        if b==0:
            print('Cannot divide by 0')
        else:
            print(ans(a/b))
    elif c=='%':
        if b==0:
            print("Cannot divide by 0")
        else:
            print(ans(a%b))
    elif c=='exit':
        break
    elif c=="return":
        continue
    else:
        print("Choose valid arithmetic operator")
