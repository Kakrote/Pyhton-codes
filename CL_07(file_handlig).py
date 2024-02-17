# f=open("test.txt")
# # content=f.read() # this read function will read the content of the file where the f is pointing.
# # print(content)
# # content=f.readlines() # this will give as an list of the content of every line
# content=f.readline() # this will read the content line by line one line at a one time.
# print(content)
# f.close()

# f=open("test.txt","w")
# f.write("all privious content is vanished hehehe") # this will replace the old content of the file with this new content.
# f=open("test.txt","a")
# # this a append mode 
# f.write("\nthis will not vanish the privious content but will add this in our existing content as well")
f=open("test.txt","r+")
# this a read and write mode for the file.
print(f.read())
f.write("\nThis will also get added to the existing content")
print(f.read()) 