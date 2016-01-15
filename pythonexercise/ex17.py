from sys import argv
from os.path import exists
script,from_file,to_file= argv
print "this is the file we have %s" % from_file
print "we are copying from %s to %s" %(from_file,to_file)
#we are reading from the file
in_file = open (from_file)
in_data = in_file.read()
print "length of the input file %d" % len(in_data)
print "does the output file exists ? %r" % from_file
print "if file exists hit RETURN"
print "if file does not exists hit CTRL-c"
raw_input()
out_file = open (to_file,"w")
out_file.write(in_data)
print "please close the both files"
in_file.close()
out_file.close()



