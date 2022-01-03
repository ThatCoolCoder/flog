# Flog

An ascii-only golfing language because why not.

## Running interpreter

To run the interpreter, run `python3 -m flog <your program as a string> <input variables>` from this directory. To provide input variables, you must provide flags as to how a variable should be interpreted. A flag goes before each variable. Flag values:
- `-n`: number
- `-s`: string
- `-ln`: list of numbers
- `-ls`: list of strings

Example:

`python3 -m flog a12o02 -n 14 -n 16 -s "Hello world" -ln "4,5,3,5" -ls "he,ll,o`

## Variables

This language is variable-based (unlike some other golfing languages). Variables are represented by the characters 0-9 plus some others. Variables can be of type `number`, `string`, or `list`. Lists can contain numbers or strings. See `Table of variables` for specifics on what each variable does.

#### Input and input variables

Many of the variables are used as inputs. If an input of their type is passed to the interpreter, then they are set to that value. Otherwise they're set to default values, which allows using the spare input vars as temporary processing vars. In other words, you can use the unused input vars as normal vars. For detail on the actual variables used for input, see `Table of variables`.

#### Table of variables

- 1: number input 1 (defaults to 0)
- 2: number input 2 (defaults to 0)
- 3: number input 3 (defaults to 1)
- 4: string input 1 (defaults to '')
- 5: string input 2 (defaults to '')
- 6: list of numbers input 1 (defaults to [])
- 7: list of numbers input 2 (defaults to [])
- 8: list of strings input 1 (defaults to [])
- 9: list of strings input 2 (defaults to [])
- 0: temporary number 1. Resets to 0 at the start of every loop cycle
- _: temporary string 1. Resets to '' at the start of every loop cycle
- |: temporary number list 1. Resets to [] at the start of every loop cycle

## Variables are cool, but how do I actually code something?

Code in this language is made up of a sequence of commands. A command either sets a variable or calls an in-built function. No separator is required after a command calling a function - the length of the command can be determined by the function's name (which is a single character) and the number of arguments. However, after setting a variable, the following character must be a precent sign. (this is known as the variable delimiter)

#### Setting variables

To set a variable, type the variable's name followed by the value you want to insert into it. The type of the variable (see `Table of variables`) determines how the value will be parsed.

I haven't thought out parsing fully, but here's the basics:
- value containing only digits and decimal point (eg `58.95`) -> number var: parse that as a floating point
- value containing characters other than digits and decimal point (eg `hello`) -> number var: sum of all ascii codes in that number
- any value -> string var: use that value as-is
- any value -> list var: split string into characters and put each character into the list

Examples:
- `057` sets variable `0` to the number value `57`
- `4hello` puts string value `hello` into variable `4`
- `2asdf` sets variable `2` to the number value `414` (95 + 115 + 100 + 102).
- `|hello world` sets variable `|` to `['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']`

#### Calling functions

All functions have single-character names. They're called by writing the name followed by the variables on which to act upon. You must always call a function with the correct amount of arguments or it will lead to misparsing the following code, as the length of a block is determined by the amount of arguments a function demands. Functions can't return anything, but they can write results into arguments if they wish. Arguments must be references to variables, the parser doesn't allow for calling functions with primitives.

Examples:
- `a0|` calls function `a` (which accepts 2 arguments) with arguments variable `0` and variable `|`

## List of functions

None of these have been implemented yet, this is just planning.

#### Basic IO and program flow:

- `o` (1 arg). Output the supplied value.
- `O` (1 arg). Output the supplied value and quit the program.
- `p` (1 arg). Output the supplied value followed by a newline.
- `P` (1 arg). Output the supplied value followed by a newline and quit the program.
- `q` (0 args). Quit the program.

#### Math:

- `a` (2 args). Add arg 1 and arg 2 together, and write the result into arg 2.
- `A` (3 args). Add arg 1 and arg 2 together, and write the result into arg 3.
- `+` (1 arg). Increment arg 1.

## Whitespace

Whitespace is completely ignored in this language. It can be added for legibility but the interpreter will pay absolutely no attention to it.