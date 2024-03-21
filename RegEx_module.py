import re
str="Hello Hwww... sir I am Anshul Pundir and I want to work with the fang compani \n as of yours"
Rex=re.search(r'H[^e]',str) # besically this '^' helps us to avoid those H which are followed by 'e' as in this case we have Hello.
print(Rex)