a=0
b=1
n=int(input("enter number of fibonacci to be generated:"))
if n<=0:
   printf("not possible ")
else if n==1:
   print(a)
elif n>=2:
   print("{},{}",format(a,b),end='')
   for i in range(2,n)
   c=a+b
   print(",{}".format(c),end='')
   a=b
   b=c
