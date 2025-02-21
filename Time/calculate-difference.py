#البرنامج يحسب اختلاف تاريخ شيئين بالسنوات والاشهر والايام
import datetime

#اخذ المعلومات من المستخدم
year_user=int(input("enetr an old year"))
month_user=int(input("enter an old month"))
day_user=int(input("enter an old day"))

year_user2=int(input("enetr a new year"))
month_user2=int(input("enter a new month"))
day_user2=int(input("enter a new day"))


#حساب الفارق بالايام
old_date=datetime.date(year_user,month_user,day_user)
new_date=datetime.date(year_user2,month_user2,day_user2)
age_days=(new_date-old_date).days

#تحويل الايام الى تاريخ
years=age_days//365
remaining_days=age_days%365
months=remaining_days//30
days=remaining_days%30 

#طباعة النتيجة
print("the difference is:")
print("\n")
print(f"years is: {years}")
print(f"months is: {months}") 
print(f"days is: {days}")
