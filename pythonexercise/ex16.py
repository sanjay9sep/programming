from sys import argv
script,filename = argv
print "this is the  name of the file % r" %filename
print "if u want this file hit RETURN"
print "if u dont want that file  then hit CTRL-D"
raw_input("?")
print "i m oopening this file..."
txt = open (filename,"w")
#print txt.read()
print "now this file is in writing mode"
print "now i m truncating this file"
txt.truncate()
print "enter the line 1:"
line1 =raw_input()
print "enter the line 2:"
line2 =raw_input()
print "now i m writing in files"
txt.write(line1)
txt.write(line2)
print "now i m closing this file "
txt.close()
