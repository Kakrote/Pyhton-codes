# 0,1,1,2,3,5,8.........
def febo(n):
   a=0
   b=1
   series=[a,b]
   while len(series)<=n:
      a,b=b,a+b
      series.append(b)
   print(series)
n=int(input("Enter the number: "))
febo(n)
   