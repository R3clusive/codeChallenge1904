value = 9998

vel = [int(i) for i in str(value)]

sorted(vel)
j = ""
import datetime
a = datetime.datetime.now()
for i in sorted(vel):
 j = str(i) + j
 final = -1
for i in range(int(value)+1,int(j)):
 num = [int(l) for l in str(i)]
 if sorted(num) == sorted(vel):
    final = i
    break
print(final)
b = datetime.datetime.now()
c = b - a

print("time it took" str(c))
