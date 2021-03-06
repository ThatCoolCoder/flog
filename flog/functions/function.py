from typing import *
import abc

from flog import Variable, VariableType

class Function:
    def __init__(self, name: str, num_args: str, func: callable):
        self.name = name
        self.num_args = num_args
        self.func = func
    
    def run(self, args: List[Variable]):
        if len(args) != self.num_args:
            raise ValueError(f'Invalid number of arguments for function {self.name}')
        self.func(*args)