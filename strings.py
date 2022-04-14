
### Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[(position+1):]
    return string

### Swap Case
def swap_case(s):
    return s.swapcase()

### String split and join
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

### Find a string
def count_substring(string, sub_string):
    result = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            result += 1
    return result

### Text wrapping
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)