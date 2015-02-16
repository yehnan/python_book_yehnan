


class FooException(Exception):
    def __init__(self, msg, status):
        Exception.__init__(self, msg, status)
        self.msg = msg
        self.status = status

try:
    raise FooException('hello', 'sta')
except FooException as e:
    print(e)