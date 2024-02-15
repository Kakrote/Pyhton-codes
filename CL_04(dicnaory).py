dic1={"Anshul":"lalpani","Anirudh":"Khasirampur"}
print(dic1)
print(dic1["Anirudh"])
# Puting a dicitonry under a dici.
dic2={"Aman":{"morning":"Kumbichour","afternoon":"dehradun","evnuing":"Uttranchal univirsity"}}
print(dic2["Aman"])
print(dic2["Aman"]["morning"])# Accesing a amans moring value.
#Adding a new elements in the dicitory
dic1["Anurag"]="hourse" # it will add the value of anurag to the dic1.
print(dic1)
del dic1["Anirudh"] # to delete the elements from the dicitionry.
print(dic1)
print(dic1.keys())
print(dic1.items())
