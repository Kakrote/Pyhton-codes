import os
# listdir(we can give it the directory as an argument to find the list of files in it )
# print(os.listdir()) # Gives the list of the all files and folder in the present directory.
# print(os.listdir("c://Program Files")) # we can go into any directory through this function.


# os.mkdir("name of the folder") this creates a folder for in the present directory. 
# os.makedirs("name of the folders ") this can make multiple folders a single time 

# os.mkdir("new") the new folder will be created by the name of new.
# os.makedirs("this/that")

# os.rename("old filename","new filename") this will rename the file with the new name.
# os.rename("test.txt","he.txt") 

# os.environ.get('name of the enviroment variable e.g path') # this will give the info of the enviroment variable.
# print(os.environ.get('path'))

# os.path.exists(name of the directory) this will retun the bollen for if the path for the given directory exist or not.
print(os.path.exists("c://")) # will retun true.
# for all finction go through the documentation.

