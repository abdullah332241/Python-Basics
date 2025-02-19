#حساب القاسم المشترك الاكبر والمضاعف المشترك الاصغر

import math
import functools

#ناخذ مجموعة ارقام من المستخدم لحسابها
nums=list(map(int,input("enter a numbers").split()))
#ملاحظة نفصل بين الارقام المدخلة باستخدام مسافة

 # math حساب الناتج مبشارة باستخدام مكتبة
Lcm=functools.reduce(math.lcm,nums)
Gcd=functools.reduce(math.gcd,nums)
#هو لتوحيد النواتج الى ناتج واحد functools بمكتبة  reduce سبب استخدام عنصر  

print(f"Lcm is: {Lcm}")
print(f"Gcd is: {Gcd}")
