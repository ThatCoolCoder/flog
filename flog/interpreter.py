from typing import *

from flog import Variable, VariableType, reset_variables, functions

class Interpreter:
    def __init__(self):

        self.VARIABLE_DELIMITER = '%'
    
    def run(self, program: str, input_values: List[Tuple[VariableType, Any]] = []):
        # Run string as Flog program

        self.__setup_variables(input_values)
        
        program_idx = 0
        while True:
            function = self.__get_function_with_name(program[program_idx])
            variable = self.__get_variable_with_name(program[program_idx])
            # If there is a function with that name, try calling it
            if function != None:
                args = []
                for arg_idx in range(function.num_args):
                    program_idx += 1
                    args.append(self.__get_variable_with_name(program[program_idx]))
                function.run(args)
                # Advance program onto start of next command
                program_idx += 1
            # Otherwise try setting the variable with that name
            elif variable is not None:
                # Find how long the value of the variable is by seeing how far away the delimiter is
                value_end = program.find(self.VARIABLE_DELIMITER, program_idx)
                if value_end == -1:
                    value_end = len(program)
                string_value = program[program_idx + 1:value_end]

                variable.parse(string_value)
                # Move it past the variable value, the variable delimiter and onto the start of the next command
                program_idx += len(string_value) + 1 + len(self.VARIABLE_DELIMITER)
            else:
                raise ValueError(f'Unknown command or variable {program[program_idx]}')

            if program_idx >= len(program):
                break

    def __setup_variables(self, input_values: List[Tuple[VariableType, Any]] = []):
        self.variables = reset_variables.reset_variables()

        used_variables = []
        for variable_type, value in input_values:
            usable_variables = [v for v in self.variables if (v not in used_variables and v.type == variable_type)]
            
            if len(usable_variables) == 0:
                raise ValueError('Ran out of variables to put input into. Oops!')
            variable = usable_variables[0]
            used_variables.append(variable)
            variable.value = value

    def __get_variable_with_name(self, name: str):
        for v in self.variables:
            if v.name == name:
                return v
        return None

    def __get_function_with_name(self, name: str):
        for f in functions.data:
            if f.name == name:
                return f
        return None