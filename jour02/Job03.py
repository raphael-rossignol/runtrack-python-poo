class Livre:
    def __init__(self):
        self.__titre = "Somehow I manage"
        self.__auteur = "Michael Scott"
        self.__nbpages = 400
        self.__disponible = True

     def verification(self):
        verification = False

        if self.__disponible:
            verification = True
        return verification

    def emprunter(self):
        emprunter = False
        self.verification()
        if self.verification():
            self.__disponible = False
            emprunter = True

        return emprunter

    def rendre(self):
        self.emprunter()
        if self.emprunter():
            self.__disponible = True



livre = Livre()
livre.verification()
livre.emprunter()
livre.rendre()
