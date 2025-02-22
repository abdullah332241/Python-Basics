#هدف البرنامج للعد التنازلي تدخل التاريخ المراد ويحسبه ويحدث النتيجة كل ثانية

import datetime
import time

print("HI what date do you want?")
year_user=int(input("enter year"))
month_user=int(input("enter month"))
day_user=int(input("enter day"))
minute_user=int(input("enter hour"))
hour_user=int(input("enter minute"))
second_user=int(input("enter second"))

time_user=datetime.datetime(year_user,month_user,day_user,hour_user,minute_user,second_user)

while True:
    now=datetime.datetime.now()
    remaining_time=time_user-now

    if remaining_time.total_seconds()<=0:
        print("the time is up!")
        break

    
    total_seconds=int(remaining_time.total_seconds())
     
    years=total_seconds//(365*24*60*60)
    total_seconds%=(365*24*60*60)

    months=total_seconds//(30*24*60*60)
    total_seconds%=(30*24*60*60)

    days=total_seconds//(24*60*60)
    total_seconds%=(24*60*60)

    hours=total_seconds//(60*60)
    total_seconds%=(60*60)

    minutes=total_seconds//(60)
    seconds=total_seconds%(60)

    print(f"Time left {years}:years , {months}:months , {days}:dys , {hours}:hours , {minutes}:minutes , {seconds}:seconds")
    time.sleep(1)
    
