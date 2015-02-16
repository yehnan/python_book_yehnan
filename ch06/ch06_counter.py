

# not work
# def counter(n):
    # def bar(x):
        # n += x
        # return n
    # return bar

def counter(n):
    def bar(x):
        nonlocal n 
        n += x
        return n
    return bar

c0 = counter(0)
c100 = counter(100)
print(c0(1)) 
print(c100(10)) 
print(c0(1)) 
print(c0(3)) 
print(c100(20)) 





