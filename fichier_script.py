class Personne:
    def __init__(self, nom=None,prenom=None,cin=None):
        self.__nom = nom
        self.__prenom = prenom
        self.__cin = cin
    @property
    def __cin(self):
        return self.__cin
    @__cin.setter
    def __cin(self,c):
        self.__cin = c

    def tostring(self):
        return "Nom: {}\nPrenom: {}\nCin: {}".format(self.__nom,self.__prenom,self.__cin)
    
class Vacciné(Personne):
    def __init__(self,nom =None,prenom=None,cin=None):
        pass

p =Personne("Kaba","Sekou",89)
print(p.c)