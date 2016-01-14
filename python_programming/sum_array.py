array=[]
print "Enter 10 numbers :"
for i in range(10):
    a=raw_input(">")
    array.append(a)
for i in array:
    print "numbers in the array list are : %s" %i
sum= 0
for i in array:
    sum+=int(i)
print "the sum of elements is %s" %sum
