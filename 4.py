num = int(input("Enter a number:"))
factorial = 1
if num < 0:
        print('negative no,no factorial')
elif num == 0:
        print('The factorial of 0 is 1')
else:
    for i in range(1,num + 1):
        factorial = factorial *1
print("The factorial of",num,"is",factorial)
