from sys import argv
script,file_name= argv
def contents(f):
    print f.read()
def rewind(f):
    f.seek(0)
def print_a_line(l,f):
    print l, f.readline()
print"open all the contents of a file"
file= open(file_name)
contents(file)
print"rewind the file :"
rewind(file)
print "contents of file  line by line: "
line=1
print_a_line(line,file)
line=line + 1
print_a_line(line,file)
line=line+1
print_a_line(line,file)

