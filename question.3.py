#wap to take a number from user input
#and print formatted table
num1 = int(input("enter your number :"))

for i in range (10 , 0,-1):
    num2 = num1*i
    print(f"{num1}x{i}: {num2}")
