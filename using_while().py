# using while
def ask_for_int():
    while True:

        try:
            result=int(input('please provide number='))
        except:
            print('that is not a number')
        finally:
            print('end of try/except/finally')
ask_for_int() # calling