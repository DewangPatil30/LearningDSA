def a():
    b()
    print('a')
def b():
    c()
    print('b')
def c():
    d()
    print('c')
def d():
    print('d')
    
    
a()