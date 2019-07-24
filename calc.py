num1,op,num2=input("enter calculation").split()
num1=int(num1)
num2=int(num2)
if op=="+":
    print("{} + {} = {}".format(num1,num2,num1+num2))
elif op=="-":
    print("{} - {} = {}".format(num1,num2,num1-num2))
elif op=="*":
    print("{} * {} = {}".format(num1,num2,num1*num2))
elif op=="/":
    print("{} / {} = {}".format(num1,num2,num1/num2))
elif op=="%":
    print("{} % {} = {}".format(num1,num2,num1%num2))
else:
    print("invalid calculation")
