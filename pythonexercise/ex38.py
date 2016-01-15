colors = "i like blue color"
stuff = colors.split (' ')
print "this is the split version of colors :",stuff
animals = ["dog","cat","rat","tiger"]
#while len(stuff)<8:
    # next = animals.pop()
     #print"this is the animal that is poped :%s" % next

     #print "add %s in the color:" % next
     #stuff.append(next)
    # print"the lenght of stuff is %s" %len(stuff)
 
print "now elements in the colors list are:",stuff

for i in range(1,9):
    next = animals.pop()
    print"this is the animal that is poped :%s" % next

    print "add %s in the color:" % next
    stuff.append(next)
    print"the lenght of stuff is %s" %len(stuff)
 
	

 


