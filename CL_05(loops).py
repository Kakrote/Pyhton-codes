li=[["Anshul",13],["rohit",58],["neha",45]]
for i in li:
    print(i) # this will give me a list of list.
for i,j in li:
    print(i,"roll no:",j)# to know what happen in it look for the notes. 
for i,j in li:
    if j<=13:
        print("no one")
    else:
        print(i,"roll no",j)
# while looop
k=2
while(k<10):
    print(k)
    k+=1