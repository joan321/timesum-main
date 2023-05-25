import datetime
timelist = ['10:30','8:50','5:20']
timesum = datetime.timedelta()
for i in timelist:
    (m,s)= i.split(':')
    d = datetime.timedelta(minutes= int(m), seconds=int(s))
    timesum +=d
    print(str(timesum))