from sys import argv
script, filename = argv
txt = open (filename)
print "the name of file is %s" % filename
print txt.read()
filename_again =raw_input("new name of file is")
txt_again = open(filename_again)
print txt_again.read()

