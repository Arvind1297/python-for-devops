#wap to take a number from user input and print formatted table
num1 = int(input("enter your number to print table:"))

for i in range (1, 11):
     print(f"{num1}*{i} = {num1*i}")
