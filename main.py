from colorama import *


class Voiture:
    marque = ''
    couleur = ''
    compteurVoitureCree = 0

    def __init__(self, marque, couleur):
        Voiture.compteurVoitureCree += 1
        self.marque = marque
        self.couleur = couleur
        listeTout.append(self)
        print(
            Fore.LIGHTWHITE_EX + f"Une voiture a été ajouté, la marque de la voiture est ci-dessous : ")


listeTout = []
listeToyota = []
listeRenault = []


class Renault(Voiture):
    finition = ''

    def __init__(self, marque, couleur, finition):
        super().__init__(marque, couleur)
        self.finition = finition
        print(Fore.LIGHTBLUE_EX + f"Renault" + Fore.LIGHTWHITE_EX)
        print('------------------------------')


def ajoutListeRenault():
    for i in range(2):
        couleur = input(Fore.LIGHTWHITE_EX + f"Quel est la couleur de votre Renault ?")
        finition = input("Quel est la finition de votre Renault ?")
        renault = Renault('Renault', couleur, finition)
        listeRenault.append(renault)


def afficherListeRenault():
    print(Fore.MAGENTA + "La liste RENAULT :")
    for i in listeRenault:
        print(
            Fore.MAGENTA + f"La marque de la voiture est " + Fore.LIGHTBLUE_EX + i.marque + Fore.MAGENTA + ", la couleur est " + Fore.LIGHTBLUE_EX + i.couleur + Fore.MAGENTA + " et la finition est '" + Fore.LIGHTBLUE_EX + i.finition + Fore.MAGENTA + "'" + Fore.WHITE)


ajoutListeRenault()


class Toyota(Voiture):
    ch = 0

    def __init__(self, marque, couleur, ch):
        super().__init__(marque, couleur)
        self.ch = ch
        print(Fore.MAGENTA + f"Toyota" + Fore.LIGHTWHITE_EX)
        print('------------------------------')


def ajoutListeToyota():
    for i in range(2):
        couleur = input(Fore.LIGHTWHITE_EX + f"Quel est la couleur de votre Toyota ?")
        ch = input("Votre toyota a combien de CH ?")
        toyota4 = Toyota('Toyota', couleur, ch)
        listeToyota.append(toyota4)


def afficherListeToyota():
    print(Fore.MAGENTA + "La liste TOYOTA :")
    for i in listeToyota:
        print(
            Fore.MAGENTA + f"La marque de la voiture est " + Fore.LIGHTBLUE_EX + i.marque + Fore.MAGENTA + ", la couleur est " + Fore.LIGHTBLUE_EX + i.couleur + Fore.MAGENTA + " et le nombre de ch est de '" + Fore.LIGHTBLUE_EX + str(
                i.ch) + Fore.MAGENTA + "'" + Fore.WHITE)


def afficherlisteTout():
    print(Fore.MAGENTA + "La liste compléte :")
    for i in listeRenault:
        print(
            Fore.MAGENTA + f"La marque de la voiture est " + Fore.LIGHTBLUE_EX + i.marque + Fore.MAGENTA + ", la couleur est " + Fore.LIGHTBLUE_EX + i.couleur + Fore.MAGENTA + " et la finition est '" + Fore.LIGHTBLUE_EX + i.finition + Fore.MAGENTA + "'" + Fore.WHITE)
    for i in listeToyota:
        print(
            Fore.MAGENTA + f"La marque de la voiture est " + Fore.LIGHTBLUE_EX + i.marque + Fore.MAGENTA + ", la couleur est " + Fore.LIGHTBLUE_EX + i.couleur + Fore.MAGENTA + " et le nombre de ch est de '" + Fore.LIGHTBLUE_EX + str(
                i.ch) + Fore.MAGENTA + "'" + Fore.WHITE)


ajoutListeToyota()

afficherListeRenault()
print('')
afficherListeToyota()
print('')
print('')
afficherlisteTout()
