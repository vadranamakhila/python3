m=int(raw_input())
num1=1
num2=1
a=2
if m<= 0:
       print("positive number")
elif m == 1:
         print 1,
else :
         print num1,
         print num2,
         while a<m:
	              num3=num1+num2
	              print num3,
	              num1=num2
	              num2=num3
                      a=a+1
