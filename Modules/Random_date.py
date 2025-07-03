import random
import time 
def getRandomDate(startdate,enddate):
    print("Generating random dates between",startdate,"and",enddate)
    Random_Generator = random.random()
    dateformat ='%m/%d/%Y'
    starttime = time.mktime(time.strptime(startdate,dateformat))
    endtime = time.mktime(time.strptime(enddate,dateformat))
    random_time = starttime + Random_Generator*(endtime-starttime)
    random_date = time.strftime(dateformat,time.localtime(random_time))
    return random_date

print(getRandomDate("12/24/1999","3/4/2009"))
