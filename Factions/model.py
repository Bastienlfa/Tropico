class Factions:
    def __init__(self):
        self.partisans = 15
        self.approbation = 50

    def AugmentationPartisan(self, np):
        self.partisans = self.partisans + np

    def ReductionPartisans(self, np):
        self.partisans = self.partisans - np

    def AugmentationApprobation(self, a):
        self.partisans = self.partisans + a

    def ReductionApprobation(self, a):
        self.partisans = self.approbation - a

    def Approbation(self):
        return self.approbation

    def Partisans(self):
        return self.partisans


class Capitalistes(Factions):
    def __init__(self):
        super().__init__()
        self.nom = 'Capitalistes'


class Communistes(Factions):
    def __init__(self):
        super().__init__()
        self.nom = 'Communistes'


class Liberaux(Factions):
    def __init__(self):
        super().__init__()
        self.nom = 'Liberaux'


class Religieux(Factions):
    def __init__(self):
        super().__init__()
        self.nom = 'Religieux'


class Militaristes(Factions):
    def __init__(self):
        super().__init__()
        self.nom = 'Militaristes'


class Ecologistes(Factions):
    def __init__(self):
        super().__init__()
        self.nom = 'Ecologistes'


class Loyalistes(Factions):
    def __init__(self):
        super().__init__()
        self.nom = 'Loyalistes'
        self.approbation = 100


class Nationalistes(Factions):
    def __init__(self):
        super().__init__()
        self.nom = 'Nationalistes'




