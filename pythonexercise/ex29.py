colors =["blue","black","green","white"]
prime =[1,2,3,4]
random =["sanjay",2,"school",3]

for i in colors:
    print "The name  of color is %s" %i
for j in prime:
    print "the prime number is %d" %j
for k in random:
    print "the random number is %r"%k
new_elements=[]
for i in range(0,7):
    print "add %d in the list" %i
    new_elements.append(i)

for j in new_elements:
    print "these are the new elements %s"%j
for i in range(4,5):
    print "this is the new no.:%d adding to the end of the list"%i
    prime.append(i)
for i in prime:
    print "no. in the prime list: %s" %i
