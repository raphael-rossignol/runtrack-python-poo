class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis ", self.nom, self.prenom)


personne1 = Personne("Rossignol", "Raphael")
personne1.SePresenter()
personne2 = Personne("Saindoun", "Abraham")
personne2.SePresenter()
