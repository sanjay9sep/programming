# problem in output
def func(*a,**keyword):
    
    for key in keyword:
        print keyword[key]

func(1,2,3,4,5,6,b=1,a=0,c=2,d=9)

