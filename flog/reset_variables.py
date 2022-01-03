from flog import Variable, VariableType

def reset_variables():
    return [
        Variable('1', VariableType.NUMBER, True),
        Variable('2', VariableType.NUMBER, True),
        Variable('3', VariableType.NUMBER, True),
        Variable('4', VariableType.STRING, True),
        Variable('5', VariableType.STRING, True),
        Variable('6', VariableType.NUMBER_LIST, True),
        Variable('7', VariableType.NUMBER_LIST, True),
        Variable('8', VariableType.STRING_LIST, True),
        Variable('9', VariableType.STRING_LIST, True),
        Variable('0', VariableType.NUMBER),
        Variable('_', VariableType.STRING),
        Variable('|', VariableType.NUMBER_LIST)
    ]