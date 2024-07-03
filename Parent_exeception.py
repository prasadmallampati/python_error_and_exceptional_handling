# parent Exception
a=eval(input())
b=eval(input())
try:
    print(a/b)
except Exception as e:
    print(e)
finally:
    print('end of try/except')
    