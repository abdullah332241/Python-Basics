import time

#يقيس مدة تنفيذ كود معين

start=time.perf_counter()  

num=1
while num<=10000000:
    num+=1

end=time.perf_counter()

#ملاحظة يمكنك وضع اي كود بالداخل لحساب مدة تنفيذه

print(f"the time is {end-start:.6f} second")
