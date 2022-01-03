import enum

@enum.unique
class VariableType(enum.Enum):
    NUMBER = 0
    STRING = 1
    NUMBER_LIST = 2
    STRING_LIST = 3

class Variable:
    def __init__(self, name: str, var_type: VariableType, is_input: bool = False):
        self.name = name
        self.type = var_type
        self.is_input = is_input

        if self.type == VariableType.NUMBER:
            self.value = 0
        elif self.type == VariableType.STRING:
            self.value = ''
        else:
            self.value = []
    
    def parse(self, value: str):
        # Parse the value and set this variable to the value
        self.value = value