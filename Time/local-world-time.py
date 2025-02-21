import datetime

#حساب الوقت المحلي
local_time=datetime.datetime.now()
print("local time:")
print("\n")
print(f"the year is:{local_time.year}")
print(f"the month is: {local_time.month}")
print(f"the day is: {local_time.day}")
print(f"the hour is: {local_time.hour}")
print(f"the minute is: {local_time.minute}")
print(f"the second is: {local_time.second}")

#حساب الوقت العالمي
UTC=datetime.datetime.utcnow()
print("UTC:")
print("\n")
print(f"the year is:{UTC.year}")
print(f"the month is: {UTC.month}")
print(f"the day is: {UTC.day}")
print(f"the hour is: {UTC.hour}")
print(f"the minute is: {UTC.minute}")
print(f"the second is: {UTC.second}")
