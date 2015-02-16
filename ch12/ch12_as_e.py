


def f():
    try:
        [0, 1, 2][999]
    except IndexError as e:
        print(e)
    finally:
        print(e)
    print(e)
f()

def f():
    exc = None 
    try:
        [0, 1, 2][999]
    except IndexError as e:
        exc = e
        print(exc)
    finally:
        print(exc)
    print(exc)
f()

