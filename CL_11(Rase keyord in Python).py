# to rase an exception in python we use raise keyword this is more like how we throws a user define exception in java.
a=input("Enter your name \n")
if a.isnumeric():
    raise Exception("Numbers as a name are not allowed") # this will get print in case we give a numaric value to the a insted of a string
print(f'hellow {a}')

# now lets see how this works with the try Exception 
c=input("enter the name:- ")
try:
    print(v)
except Exception as e:
    if c=="Anshul":
        raise Exception(f"{c} is not allowed in this string")
    print("The exception due to v is handeled so don't warry about it ")