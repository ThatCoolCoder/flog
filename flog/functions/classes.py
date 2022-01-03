from .function import Function
import abc

class o(Function):
    def __init__(self):
        super().__init__('o', 1)
    
    def _run(self, variable):
        print(variable.value)