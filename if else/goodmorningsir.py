import time
time_stamp = int(time.strftime('%H'))

if time_stamp >=6 and time_stamp  <12:
    print("Good Morning sir ")
elif time_stamp >=12 and time_stamp < 17:
    print("Good Afternoon sir ")
elif time_stamp >= 17 and time_stamp <  19:
    print("Good Evening sir ")
elif time_stamp >= 19 and time_stamp < 24: 
    print("Good Night sir ")
else:
    print("it is midnight sir ")    