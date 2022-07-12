a=100
print (a)
def someFunction():
    global a
    print(a)
    a='changing variable'
someFunction()
print(a)

tup1 = ('Manish','Chynika','Sidhish','Dinesh');
print(tup1[0])