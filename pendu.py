
class MotADeviner:

    def __init__(self, mot = ""):
        self.symbole = "*"
        self.mot = mot.upper()
        if self.mot == "":
            self.demander_mot()
        self.mot_split = list(self.mot)
        self.mot_cache = ""
        self.lettre = ""
        self.lettres_deja_rentrees = [" ", "'", ".", ",", "-", "$", "€"]
        self.cacher_mot()
        
        
    def cacher_mot(self):
        mot_cache_split = [self.symbole if not l in self.lettres_deja_rentrees else l for l in self.mot_split]
        self.mot_cache = "".join(mot_cache_split)
        print(self.mot_cache)
        return not self.symbole in self.mot_cache
    

    def demander_mot(self):
        print()
        self.mot = input("Veuillez entrer un mot ? : ").upper()


    def demander_lettre(self):
        self.lettre = input("Essayer une lettre : ")
        self.lettres_deja_rentrees.append(self.lettre.upper())


    def si_lettre_correcte(self):
        return (self.lettre.upper()) in self.mot




class Jeu:

    def __init__(self, mot_a_deviner):
        self.mot_a_deviner = mot_a_deviner
        self.vie = int(len(self.mot_a_deviner.mot) * 0.6)
        if self.vie <= 1:
            self.vie = 3

    def lancer(self):
        pluriel = "s" if self.vie > 1 else ""
        for i in range(50):
            print()
        print(self.mot_a_deviner.mot_cache)
        print("Vous avez", self.vie, "vie" + pluriel + " pour trouver ce mot !")
        print()
        while self.vie > 0:
            self.mot_a_deviner.demander_lettre()
            if self.mot_a_deviner.cacher_mot():
                break
            if not self.mot_a_deviner.si_lettre_correcte():
                self.vie -= 1
            pluriel = "s" if self.vie > 1 else ""
            print("Vie" + pluriel + " restante" + pluriel + " :", self.vie)
            print()
        print()
        if self.vie > 0:
            print("Bravo vous avez gagné(e) la partie")
        else:
            print("Vous avez perdu !")

        print("Le mot à retrouver était :", self.mot_a_deviner.mot)
        print()    




Jeu(MotADeviner()).lancer()

