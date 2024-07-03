# Write a function that asks for an integer and print the square of it.use a while loop with a try and except block to account for incorrect input 
def ask():
    waiting=True
    while waiting:
        try:
            n=int(input())
        except:
            print('pls try again')
        else:
            waiting=False
print('Your number squares is ')
print(n**2)
ask()

