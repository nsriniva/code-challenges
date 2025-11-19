
class Print:
    def __init__(self, arg):
        self.func = None
        self.arg = None
        if callable(arg):   
            print(f'Initializing class decorator with function {arg.__name__}!')
            self.func = arg
        else:
            print(f'Initializing class decorator with argument {arg}!')
            self.arg = arg
        
    def __call__(self, *args, **kw_args):
        if self.func is None and callable(args[0]):
            func = args[0]
            def wrapper(*args, **kw_args):
                func(*args, *kw_args)
                print(f'Class decorator arg {self.arg}!')
            return wrapper            

        print(f'Function name is {self.func.__name__} with args {args} and kw_args{kw_args}')
        self.func(*args, **kw_args)

@Print(109)
def test_func(arg1):
    print(f'Executing test_func with argument {arg1}!')

@Print
def test2_func(arg1):
    print(f'Executing test2_func with argument {arg1}!')


test_func(10)
test2_func(20)
