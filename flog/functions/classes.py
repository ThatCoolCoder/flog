from .function import Function

# File containing all of the builtin functions for flog

# Basic IO

class o(Function):
    def __init__(self):
        super().__init__('o', 1)
    
    def _run(self, variable):
        print(variable.value, end='')

class O(Function):
    def __init__(self):
        super().__init__('O', 1)
    
    def _run(self, variable):
        print(variable.value, end='')
        quit()

class p(Function):
    def __init__(self):
        super().__init__('p', 1)
    
    def _run(self, variable):
        print(variable.value)

class P(Function):
    def __init__(self):
        super().__init__('P', 1)
    
    def _run(self, variable):
        print(variable.value)
        quit()

class q(Function):
    def __init__(self):
        super().__init__('q', 0)
    
    def _run(self):
        quit()

class Q(Function):
    def __init__(self):
        super().__init__('Q', 1)
    
    def _run(self, variable):
        if variable.value > 0:
            quit()

# Program flow:

class equals(Function):
    def __init__(self):
        super().__init__('=', 3)
    
    def _run(self, var1, var2, var3):
        var3.value = (var1.value == var2.value)

# Math

class a(Function):
    def __init__(self):
        super().__init__('a', 2)
    
    def _run(self, var1, var2):
        var2.value += var1.value

class A(Function):
    def __init__(self):
        super().__init__('a', 3)
    
    def _run(self, var1, var2, var3):
        var3.value = var1.value + var2.value

class plus(Function):
    def __init__(self):
        super().__init__('+', 1)
    
    def _run(self, variable):
        variable.value += 1

class minus(Function):
    def __init__(self):
        super().__init__('-', 1)
    
    def _run(self, variable):
        variable.value -= 1

# Other

class h(Function):
    def __init__(self):
        super().__init__('h', 0)
    
    def _run(self):
        print('Hello, World!')

class H(Function):
    def __init__(self):
        super().__init__('H', 1)
    
    def _run(self, variable):
        variable.value = 'Hello, World!'
