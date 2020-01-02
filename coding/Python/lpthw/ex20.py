# this is tutorial related to functions and files

from sys import argv

script,input_file=argv

# simple print all
def print_all(f):
    print(f.read())

# move a location in a file
def rewind(f):
    f.seek(10)

def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file=open(input_file)

print("let's print whole file first")
print(current_file.read())

# lets go first of file
print("let rewind file")
rewind(current_file)

print("let's print 3 line")

current_line=0
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)
