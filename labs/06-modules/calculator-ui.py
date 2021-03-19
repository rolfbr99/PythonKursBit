from calculator import *

operators={"+":add,"-":sub,"/":div,"x":mul,"*":mul}

calc=input("Rechnung eingeben: ")

x,op,y=calc.split(" ")
func=operators.get(op)

print(x,op,y)
if func == None:
    print("Unkown operator")
elif (func == div and y=="0"):
    print("Division by zero not allowed")
else:        
    print ( func(float(x), float(y)) )