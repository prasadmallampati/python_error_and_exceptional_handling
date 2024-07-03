a=int(input())
b=int(input())

try:
    a/b
except Exception as e:
    print(e)
print(dir(locals()['__builtin__']))