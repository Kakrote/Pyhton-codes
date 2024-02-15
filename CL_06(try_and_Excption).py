num1=input("Enter the value ")
num2=input("Enter the value ")
try:
    print(int(num1)+int(num2))
except Exception as e:
    print("this is a exeption ",e)
print("This is our rest of the code which will be exicuted in any case even if the above code showes some error")