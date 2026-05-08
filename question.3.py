#wap to take a number from user input
#and print formatted table
num1 = int(input("enter your number to print table reverse :"))

for i in range (10 , 0,-1):
    print(f"{num1}*{i}: {num1*i}")
