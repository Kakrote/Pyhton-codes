class dadaji:
    _var=10 # this is for protected
    @classmethod
    def will(cls):
        return f"My property goes to my son whoes name is raju rasthogi"
class beta(dadaji):
    _var2=20
    @classmethod
    def will(cls):
        return f"My property given by my dad to me goes to  my son viru shasthra bhudhe"
class potha(beta):
    __var3=30 #  this is for private 
    @classmethod
    def will(cls):
        return f"MY properte which I have inherited from my dadaji and my father is mine"

p=potha()
print(p._var) # we can acces the protected variable of a dadaji class
print(p._potha__var3) # this is how you print the private variable 
print(p._var2)
print(p.will())
  