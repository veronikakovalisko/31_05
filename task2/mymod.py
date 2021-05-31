''' Create a Python module called `mymod.py`, which has three functions:
count_lines(name) function that reads an input file and counts
the number of lines in it (hint: file.readlines() does most of the work for you, and `len` does the rest)
count_chars(name) function that reads an input file
and counts the number of characters in it (hint: file.read() returns a single string)
test(name) function that calls both counting functions with a given input file­name.
Such a filename generally might be passed-in, hard-coded, input with raw_input,
or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.'''
def count_lines(name: str):
    with open(name) as fp:
        n = len(fp.readlines())
    return n

def count_chars(name: str):
    with open(name) as fp:
       line = fp.read()
       n = len(line)
    return n

def test(name):
    return count_chars(name), count_lines(name)

print(count_chars('filename'))