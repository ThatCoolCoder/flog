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

# Comparing

class equals(Function):
    def __init__(self):
        super().__init__('=', 3)
    
    def _run(self, var1, var2, var3):
        var3.value = (var1.value == var2.value)

class e(Function):
    def __init__(self):
        super().__init__('e', 1)
    
    def _run(self, variable):
        variable.value = 1 - variable.value % 2

class E(Function):
    def __init__(self):
        super().__init__('E', 2)
    
    def _run(self, var1, var2):
        var2.value = 1 - var1.value % 2

# Basic math

class a(Function):
    def __init__(self):
        super().__init__('a', 2)
    
    def _run(self, var1, var2):
        var2.value += var1.value

class A(Function):
    def __init__(self):
        super().__init__('A', 3)
    
    def _run(self, var1, var2, var3):
        var3.value = var1.value + var2.value

class s(Function):
    def __init__(self):
        super().__init__('s', 2)
    
    def _run(self, var1, var2):
        var2.value = var1.value - var2.value

class S(Function):
    def __init__(self):
        super().__init__('S', 3)
    
    def _run(self, var1, var2, var3):
        var3.value = var1.value - var2.value

class m(Function):
    def __init__(self):
        super().__init__('m', 1)
    
    def _run(self, var1, var2):
        var2.value *= var1.value

class M(Function):
    def __init__(self):
        super().__init__('M', 1)
    
    def _run(self, var1, var2, var3):
        var3.value = var1.value * var2.value

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

# Not basic math

class f(Function):
    def __init__(self):
        super().__init__('f', 2)
    
    def _run(self, var1, var2):
        var2.value = []
        for i in range(1, var1.value + 1):
            if var1.value % i == 0:
                var2.value.append(i)

class F(Function):
    def __init__(self):
        super().__init__('F', 2)
    
    def _run(self, var1, var2):
        print('Sorry, haven\'t implemented F yet')

# Lists

class c(Function):
    def __init__(self):
        super().__init__('c', 3)
    
    def _run(self, var1, var2, var3):
        var3.value = (var1.value in var2.value)

class C(Function):
    def __init__(self):
        super().__init__('C', 3)
    
    def _run(self, var1, var2, var3):
        var3.value = (var1.value not in var2.value)

class semicolon(Function):
    def __init__(self):
        super().__init__(';', 3)
    
    def _run(self, var1, var2, var3):
        var3.value = var1.value[var2.value]

class colon(Function):
    def __init__(self):
        super().__init__(':', 3)
    
    def _run(self, var1, var2, var3):
        var1.value = [*var1.value, *[''] * (len(var1.value) - var3.value + 1)]
        var1.value[var3.value] = var2.value

class l(Function):
    def __init__(self):
        super().__init__('l', 2)
    
    def _run(self, var1, var2):
        var2.value = len(var1)

class L(Function):
    def __init__(self):
        super().__init__('L', 2)
    
    def _run(self, var1, var2):
        var2.value = len(var1) - 1

class slash(Function):
    def __init__(self):
        super().__init__('/', 2)
    
    def _run(self, var1, var2):
        var1.value.append(var2.value)

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
