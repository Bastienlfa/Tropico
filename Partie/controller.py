from Partie.model import Partie, ListParty, CreateParty
import json

LP = ListParty()


def controleNvl(nom):
    if nom in LP:
        print('Ce nom existe déja')
        return False
    else:
        return True


def saisiRa(ra):
    if ra == 'c':
        nom = input('Nom de la nouvelle partie: ')
        a = controleNvl(nom)
        if a:
            mode = input('Mode partie: facile/difficile')
            nvl = {'nom': nom, 'mode': mode}
            CreateParty(nvl)
    elif ra == 'r':
        print(LP)
        nom = input('Nom de la partie à charger')
        if nom not in LP:
            print('Partie inexistante verifier le nom')
            saisiRa(ra)
        else:
            a = Partie()
            a.DownloadParty(nom)
    else:
        return print('Mauvaise entrée')
