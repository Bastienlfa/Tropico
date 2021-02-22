import json


def ListParty():
    with open('./bd.json') as conf:
        conf = json.load(conf)
        nom = []
        for elt in conf:
            nom.append(elt['nom'])
        return nom


def CreateParty(nvl):
    with open('./bd.json') as conf:
        conf = json.load(conf)
        resul = conf
        Party = nvl
        resul.append(Party)

        with open('./bd.json', 'w') as mb:
            json.dump(resul, mb, indent=1)


class Partie:
    def __init__(self):
        self.nom = 'benjamin'
        self.mode = 'facile'
        self.bd = './bd.json'
        self.saison = 0
        self.agriculture = 15
        self.industries = 15
        self.tresorerie = 200

    def DownloadParty(self, nom):
        with open(self.bd) as conf:
            conf = json.load(conf)
            for elt in conf:
                if elt['nom'] == nom:
                    self.nom = elt['nom']
                    self.mode = elt['mode']
                    self.faction = elt['faction']
                    return print('Bienvenu', self.nom)

    def nextsaison(self):
        if self.saison < 3:
            self.saison = self.saison + 1
        else:
            self.saison = 0

        return self.saison

    def getsaison(self):
        return self.saison

