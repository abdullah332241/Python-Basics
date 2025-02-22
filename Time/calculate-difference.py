#البرنامج يحسب اختلاف تاريخين بالسنوات والاشهر والايام
import datetime

#اخذ المعلومات من المستخدم
year_user=int(input("enetr year a"))
month_user=int(input("enter month a"))
day_user=int(input("enter day a"))

year_user2=int(input("enetr year b"))
month_user2=int(input("enter month b"))
day_user2=int(input("enter day b"))


#حساب الفارق بالايام
date_a =datetime.date(year_user,month_user,day_user)
date_b =datetime.date(year_user2,month_user2,day_user2)
age_days=(abs(date_a-date_b).days)

#تحويل الايام الى تاريخ
years=age_days//365
remaining_days=age_days%365
months=remaining_days//30
days=remaining_days%30 

#طباعة النتيجة
if date_a>date_b:
    print(f"date a is greater by {years} years , {months} months , {days} days!")
else:
    print(f"date b is greater by {years} years , {months} months , {days} days!")
