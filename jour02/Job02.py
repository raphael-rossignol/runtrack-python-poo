class Livre:
    def __init__(self):
        self.__titre = "Somehow I manage"
        self.__auteur = "Michael Scott"
        self.__nbpages = 400

    def __gettitre(self):
        return self.__titre

    def __getauteur(self):
        return self.__auteur

    def __getnbpages(self):
        return self.__nbpages

    def modifyvalues(self):
        self.__gettitre()
        self.__getauteur()
        self.__getnbpages()

        self.__titre = "Creed's Thoughts"
        self.__auteur = "Creed Bratton"
        self.__nbpages = 50

        if self.__nbpages % 2 != 0:
            print("Nombre de pages incorrect")
        else:
            print("Le titre est", self.__titre, ",l'auteur est", self.__auteur, "et le nombre de pages est", self.__nbpages)


livre = Livre()
livre.modifyvalues()
