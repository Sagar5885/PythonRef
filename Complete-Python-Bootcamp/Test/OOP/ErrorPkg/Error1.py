def ask_int_while():
    while True:
        try:
            val = int(input('please enter integer: '))
        except:
            print('Input is not integer!')
            continue
        else:
            print('Input is integer, very good!')
            break
        finally:
            print('Finally Execute Always!')

        print(val)

ask_int_while()


x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')


def ask():
    while True:
        try:
            n = input('Input an integer: ')
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break

    print('Thank you, you number squared is: ', n ** 2)

ask()