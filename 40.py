a=int(raw_input())
num1=1
num2=1
i=2
if a<= 0:
       print("positive number")
elif a == 1:
         print 1,
else :
         print num1,
         print num2,
         while i<a:
	              num3=num1+num2
	              print num3,
	              num1=num2
	              num2=num3
                      i=i+1
