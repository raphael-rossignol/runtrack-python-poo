class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTVA = self.prixHT * self.TVA
        return prixTVA

    def afficher(self):
        print("Le nom du produit est", self.nom)
        print("Le prixHT est", self.prixHT)
        print("Le prix avec TVA est", self.CalculerPrixTTC())


baguette = Produit("Baguette", 0.80, 1.20)
baguette.CalculerPrixTTC()
baguette.afficher()

ordinateur = Produit("Ordinateur", 400, 1.20)
ordinateur.CalculerPrixTTC()
ordinateur.afficher()