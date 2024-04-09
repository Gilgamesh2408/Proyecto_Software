import time 

print ("¿Que desea que te recuerden?")
text = str(input())
print("¿En cuanto tiempo quiere que se le recuerde?")

local_time = float(input())
local_time = local_time *60

time.sleep(local_time)

print(text)
