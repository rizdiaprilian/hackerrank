
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