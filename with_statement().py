# with open()
with open('demo1.txt','r') as f:
    text=f.read()
    print(text)
    f.close()