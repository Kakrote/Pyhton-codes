num=["1","2","20","10"]
num=list(map(int,num))
num[2]=num[2]+20
print(num[2])
# note the map function also take an function
num=list(map(lambda x:x*x,num))
print(num)
def squre(a):
    return a**2
def cube(a):
    return a**3
fun=[squre,cube]
for i in range(10):
    val=list(map(lambda c:c(i),fun))
    print(val)
print("\n using a filter function\n")
nu=[1,2,3,4,5,6,7,8]
value=list(filter(lambda x:x>5,nu))
print(value)
print("\n reduce function\n")
from functools import reduce as r
v=r(lambda x,y:x+y,value)
print(v) 