# try except finally example
try:
    f=open('testfile.txt','r')
    f.write('write a test line')
except:
    print('all other exceptions')
finally:
    print('i always run')