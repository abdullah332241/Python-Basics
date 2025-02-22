#البرنامج يعطيك اي يوم من ايام الاسبوع بناء على التاريخ المدخل
import datetime

#اخذ المعلومات من المستخدم
year=int(input("enetr year "))
month=int(input("enter month "))
day=int(input("enter day "))

#حفظ البيانات في متغير
date_user=datetime.date(year,month,day)

#تحويل التاريخ الى يوم
day_of_week=date_user.strftime("%A")
#لاخراج ترقيم اليوم (%w)لاخراج اختصار اليوم و (%a)ملاحظ يمكم استخدام 

print(f"the date entered is {day_of_week}") 
