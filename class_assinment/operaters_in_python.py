#   Program using IN operator
details=['Neha bisht','MCA','B','45']
frinds=["Raj","Heansj","Mandeep","Mohit"]
print(frinds)
frn=input("Enter the name of the frind-  ")
if frn in frinds:
    print("he is my frind")
else:
    print("he not a frind")

print(f'\nname={details[0]}\nclass={details[1]}\nsec={details[2]},roll_no={details[3]}')