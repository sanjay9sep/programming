#create the name of the states
states ={
	"uttarpradesh":"up",
	"delhi":"dl",
	"andhrapradesh":"ap",
	"rajasthan":"rj"
}

#create the name of the cities in the states
cities ={
	"up":"agra",
	"dl":"noida",
	"ap":"hyderabad",
	"rj":"kota"
}

print "some cities name :"
print "up has %s" %cities["up"]
print "rj has %s" %cities["rj"]

print "some  states name :"
print "the short name is %s" %states["uttarpradesh"]
print "the short name is %s" %states["andhrapradesh"]

print "some cities name using states:"
print "the name of city is %s" % cities[states["uttarpradesh"]]
print "the name of city is %s" % cities[states["rajasthan"]]
print "the name of city is %s" % cities[states["delhi"]]

#print every state name with abbreviation
print'*'*10
for state,abbrev in states.items():
    print "%s has  this %s abbreviation " %(state,abbrev)
# print every city name with abbreviation
print'-' *10
for city,abbrev in cities.items():
    print "%s has  this %s abbreviation " %(city,abbrev)
	
# print every city in the state
print '+' *10
for state,abbrev in states.items():
    print "%s has  %s abbreviation and has %s city" %(state,abbrev,cities[abbrev])     	




	
