from sys import argv
script,user_name = argv
pr = ">>>>>>>>>>" #it is just a string variable
print "my script name is %s,my user name is %s" %(script,user_name)
print "what do you lke %s" %(user_name)
like =raw_input(pr)
print "where do you live %s" %(user_name)
live = raw_input(pr)
print "whats ur favourite food %s" %(user_name)
food = raw_input(pr)
print '''
i like %r i live in %r.
my favourite good is %r.
''' %(like,live,food)


