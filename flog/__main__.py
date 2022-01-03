import sys

from flog import VariableType, Interpreter

# Small thing to pass command line args to a flog program

FLAG_TO_VARIABLE_TYPE = {
    '-n' : VariableType.NUMBER,
    '-s' : VariableType.STRING,
    '-ln' : VariableType.NUMBER_LIST,
    '-ls' : VariableType.STRING_LIST
}

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise ValueError('Expected program as argument 1')
    elif len(sys.argv) == 2:
        raw_args = []
    else:
        raw_args = sys.argv[2:]

    program = sys.argv[1]

    input_values = []
    next_value_type = None
    for arg in raw_args:
        # If we don't have a type defined, try and define one
        if next_value_type == None:
            next_value_type = FLAG_TO_VARIABLE_TYPE[arg]
        # Otherwise use that type to parse the next variable
        else:
            value = None
            if next_value_type == VariableType.NUMBER:
                value = int(arg)
            elif next_value_type == VariableType.STRING:
                value = arg
            elif next_value_type == VariableType.NUMBER_LIST:
                value = [str(x) for x in arg.split(',')]
            elif next_value_type == VariableType.STRING_LIST:
                value = arg.split(',')

            input_values.append((next_value_type, value))

            next_value_type = None
    interpreter = Interpreter()
    interpreter.run(program, input_values)