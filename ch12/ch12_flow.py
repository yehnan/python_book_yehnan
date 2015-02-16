

def foo():
    try :
        raise ValueError
    except IndexError:
        print('IndexError')
    finally:
        print('foo finally')
    print('foo end')
def bar():
    try:
        foo()
    except ValueError:
        print('ValueError')
    finally:
        print('bar finally')
    print('bar end')
bar()
print('program end')

