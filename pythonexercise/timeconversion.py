
from datetime import datetime


 
def convertToEuTime(us_time):
    return datetime.strptime(us_time, '%I:%M:%S%p').strftime('%H:%M:%S')
t= raw_input().strip()
print convertToEuTime(t)
 
