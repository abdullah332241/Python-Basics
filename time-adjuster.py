#برنامج يسمح لك بالتعديل على الزمن
import datetime
import dateutil

#عرض الخيارات على المستخدم
print("1. years , months , days")
print("2. hours , minutes , seconds")
print("3. all: years , months , days hours , minutes , seconds")

choice_user=input("enter any type operations?")
operations_type=input("enetr any operations (+ or -)?")

#في حال اختار النوع العام بالاعوام والشهور والايام
if choice_user=="1":
    
    #اخذ معلومات من المستخدم وحفظها في متغير
    year1=int(input("enter year"))
    month1=int(input("enter month"))
    day1=int(input("enter day"))
    date1=datetime.date(year1,month1,day1)

    # في حال اراد اضافة وقت
    if operations_type=="+":
     year_change__=int(input("how much increase do you want in years?"))
     month_change__=int(input("how much increase do you want in months?"))
     day_change__=int(input("how much increase do you want in days?"))
     result=date1+dateutil.relativedelta.relativedelta(years=year_change__,months=month_change__,days=day_change__)
     print(f"the date after modification is: {result}")

    #في حال اراد ازالة وقت
    elif operations_type=="-":
     year_change_=int(input("how much do you want to decrease in years?"))
     month_change_=int(input("how much do you want to decrease in months?"))
     day_change_=int(input("how much do you want to decrease in days?"))
     result=date1-dateutil.relativedelta.relativedelta(years=year_change_,months=month_change_,days=day_change_)
     print(f"the date after modification is: {result}")

#في حال اختار النوع الدقيق بالساعات والدقائق والثواني
elif choice_user=="2":

    hour1=int(input("enter hour"))
    minute1=int(input("enter minute"))
    second1=int(input("enter second"))
    date2=datetime.datetime(hour1,minute1,second1)

    if operations_type=="+":
     hour_change__=int(input("how much increase do you want in hours?"))
     minute_change__=int(input("how much increase do you want in minutes?"))
     second_change__=int(input("how much increase do you want in seconds?"))
     result=date2+dateutil.relativedelta.relativedelta(hours=hour_change__,minutes=minute_change__,seconds=second_change__)
     print(f"the date after modification is: {result}")

    elif operations_type=="-":
     hour_change_=int(input("how much do you want to decrease in hours?"))
     minute_change_=int(input("how much do you want to decrease in minutes?"))
     second_change_=int(input("how much do you want to decrease in seconds?"))
     result=date2-dateutil.relativedelta.relativedelta(hours=hour_change_,minutes=minute_change_,seconds=second_change_)
     print(f"the date after modification is: {result}")

#في حال اختار كل النوعين والتحكم بالزمن بشكل كامل
elif choice_user=="3":

    year2=int(input("enter year"))
    month2=int(input("enter month"))
    day2=int(input("enter day"))
    hour2=int(input("enter hour"))
    minute2=int(input("enter minute"))
    second2=int(input("enter second"))
    date3=datetime.datetime(year2,month2,day2,hour2,minute2,second2)

    if operations_type=="+":
     year_change__2=int(input("how much increase do you want in years?"))
     month_change__2=int(input("how much increase do you want in months?"))
     day_change__2=int(input("how much increase do you want in days?"))
     hour_change__2=int(input("how much increase do you want in hours?"))
     minute_change__2=int(input("how much increase do you want in minutes?"))
     second_change__2=int(input("how much increase do you want in seconds?"))
     result=date3+dateutil.relativedelta.relativedelta(years=year_change__2,months=month_change__2,days=day_change__2,hours=hour_change__2,minutes=minute_change__2,seconds=second_change__2)
     print(f"the date after modification is: {result}")

    elif operations_type=="-":
     year_change_2=int(input("how much do you want to decrease in years?"))
     month_change_2=int(input("how much do you want to decrease in months?"))
     day_change_2=int(input("how much do you want to decrease in days?"))
     hour_change_2=int(input("how much do you want to decrease in hours?"))
     minute_change_2=int(input("how much do you want to decrease in minutes?"))
     second_change_2=int(input("how much do you want to decrease in seconds?"))
     result=date3-dateutil.relativedelta.relativedelta(years=year_change_2,months=month_change_2,days=day_change_2,hours=hour_change_2,minutes=minute_change_2,seconds=second_change_2)
     print(f"the date after modification is: {result}")
