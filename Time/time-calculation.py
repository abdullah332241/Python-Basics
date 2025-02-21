import time

time_now=time.time()  #يعطينا الوقت بالثواني من 1970

coorect_time=time.ctime(time_now)         #يحول الثواني لوقت مفهوم 

print(f"the time is {coorect_time}") 
