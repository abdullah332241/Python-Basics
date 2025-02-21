#البرنامج يحسب عمر شيء معين بالسنوات والاشهر والايام

import datetime

#اخذ المعلومات من المستخدم
year_user=int(input("enetr a year"))
month_user=int(input("enter a month"))
day_user=int(input("enter a day"))

#حساب العمر بالايام
birth_date=datetime.date(year_user,month_user,day_user)
today=datetime.date.today()
age_days=(today-birth_date).days

#تحويل الايام الى تاريخ
years=age_days//365
remaining_days=age_days%365
months=remaining_days//30
days=remaining_days%30 

#طباعة النتيجة
print(f"years is: {years}")
print(f"months is: {months}") 
print(f"days is: {days}")
