from .function import Function

# Instantiate one of each function class to use
data = []

def o(variable):
    print(variable.value, end='')
data.append(Function('o', 1, o))

def O(variable):
    print(variable.value, end='')
    quit()
data.append(Function('O', 1, O))

def p(variable):
    print(variable.value)
data.append(Function('p', 1, p))

def P(variable):
    print(variable.value)
    quit()
data.append(Function('P', 1, P))

def q():
    quit()
data.append(Function('q', 0, q))

def Q(variable):
    if variable.value > 0:
        quit()
data.append(Function('Q', 1, Q))

def equals(var1, var2, var3):
    var3.value = (var1.value == var2.value)
data.append(Function('equals', 3, equals))

def e(variable):
    variable.value = 1 - variable.value % 2
data.append(Function('e', 1, e))

def E(var1, var2):
    var2.value = 1 - var1.value % 2
data.append(Function('E', 2, E))

def a(var1, var2):
    var2.value += var1.value
data.append(Function('a', 2, a))

def A(var1, var2, var3):
    var3.value = var1.value + var2.value
data.append(Function('A', 3, A))

def s(var1, var2):
    var2.value = var1.value - var2.value
data.append(Function('s', 2, s))

def S(var1, var2, var3):
    var3.value = var1.value - var2.value
data.append(Function('S', 3, S))

def m(var1, var2):
    var2.value *= var1.value
data.append(Function('m', 1, m))

def M(var1, var2, var3):
    var3.value = var1.value * var2.value
data.append(Function('M', 1, M))

def plus(variable):
    variable.value += 1
data.append(Function('plus', 1, plus))

def minus(variable):
    variable.value -= 1
data.append(Function('minus', 1, minus))

def f(var1, var2):
    var2.value = []
    for i in range(1, var1.value + 1):
        if var1.value % i == 0:
            var2.value.append(i)
data.append(Function('f', 2, f))

def F(var1, var2):
    print('Sorry, haven\'t implemented F yet')
data.append(Function('F', 2, F))

def c(var1, var2, var3):
    var3.value = (var1.value in var2.value)
data.append(Function('c', 3, c))

def C(var1, var2, var3):
    var3.value = (var1.value not in var2.value)
data.append(Function('C', 3, C))

def semicolon(var1, var2, var3):
    var3.value = var1.value[var2.value]
data.append(Function('semicolon', 3, semicolon))

def colon(var1, var2, var3):
    var1.value = [*var1.value, *[''] * (len(var1.value) - var3.value + 1)]
    var1.value[var3.value] = var2.value
data.append(Function('colon', 3, colon))

def l(var1, var2):
    var2.value = len(var1)
data.append(Function('l', 2, l))

def L(var1, var2):
    var2.value = len(var1) - 1
data.append(Function('L', 2, L))

def slash(var1, var2):
    var1.value.append(var2.value)
data.append(Function('slash', 2, slash))

def h():
    print('Hello, World!')
data.append(Function('h', 0, h))

def H(variable):
    variable.value = 'Hello, World!'
data.append(Function('H', 1, H))