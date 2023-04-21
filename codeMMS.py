import random

listePokemon = ["Ouisticram","Tortipousse","Tiplouf"]
listePokemon1 = ["Galopa","Bouldeneu","Tentacruel"]
listePokemon2 = ["Maganon","Tropius","Leviator"]


class Pokémon:
    
    #constructeur
    def __init__(self,nom,typePokemon,pv,vitesse,attaque,esquive,defense,attaque1,attaque2,attaque3,capacite,type_cap):
        """str,str,int,int,int,int,int,str,str,str,str,str,int -> void
        Précondition: aucune
        Rôle: Initialise un pokémon selon ses attributs."""
        
        self.nom = nom
        self.type = typePokemon
        self.pv = pv
        self.pvBase = pv
        self.vitesse = vitesse
        self.attaqueBase = attaque
        self.attaque = attaque
        self.esquive = esquive
        self.attaque1 = attaque1
        self.attaque2 = attaque2
        self.attaque3 = attaque3
        self.capacite = capacite
        self.type_cap = type_cap
        self.defense = defense
        self.statut = 0
                                #statut = 0 -> pas de probleme
                                #statut = 1 -> paralisé
                                #statut = 2 -> brulure
                                #statut = 3 -> confusion

#------------------------------------------Début attaques phisique-----------------------------------------------#

    #attaque phisique
    def charge(self,adversaire):
        """self, Pokemon -> int
        Précondition: aucune
        Rôle: Le pokémon objet utilise l'attaque charge sur le pokémon cible (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive:
            return self.nom+" attaque charge !", adversaire.nom+" esquive l'attaque !"
        else:
            adversaire.pv = adversaire.pv - (self.attaque- adversaire.defense)
            return self.nom+" attaque charge !", ""   
        
    def vive_attaque(self,adversaire):
        """self, Pokemon -> int
        Précondition: aucune
        Rôle: Le pokémon objet utilise l'attaque vive-attaque sur le pokémon cible (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive and adversaire.vitesse > self.vitesse:
            return self.nom+" attaque charge !",adversaire.nom+" esquive l'attaque !"
        else:
            if self.vitesse > adversaire.vitesse:
                adversaire.pv = adversaire.pv - ((self.attaque +1) - adversaire.defense)
                return self.nom+" attaque vive-attaque !", ""
            else:
                adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
                return self.nom+" attaque vive-attaque !", ""
            
    def ecrasement(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque écrasement sur un pokémon (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive:
            return self.nom+" attaque ecrasement !",adversaire.nom+" esquive l'attaque !"
        else :
            adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
            return self.nom+" attaque ecrasement !",""
        
    def feinte(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque feinte sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
        return self.nom+" attaque feinte !", ""
    
    def etreinte(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque étreinte sur un pokémon (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive:
            return self.nom+" attaque etreinte !",adversaire.nom+" esquive l'attaque !"
        else :
            adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
            return self.nom+" attaque etreinte !",""
        
    def ligotage(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque ligotage sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
        return self.nom+" attaque ligotage !", ""

#------------------------------------------Fin attaques phisique-----------------------------------------------#
    
#------------------------------------------Debut attaques Feu-----------------------------------------------#
    
    #attaques type       
    def flammeche(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune 
        Rôle: Utilise l'attaque flammèche sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        if adversaire.type == "Plante":
            adversaire.pv = adversaire.pv - round(((self.attaque + (0.7*self.attaque)) - adversaire.defense))
            return self.nom+" attaque flammeche !","C'est super efficace !"
        if adversaire.type == "Eau" or adversaire.type =="Feu":
            adversaire.pv = adversaire.pv - round(((self.attaque - (0.6*self.attaque)) - adversaire.defense))
            return self.nom+" attaque flammeche !","Ce n'est pas tres efficace..."
        else:
            adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
            return self.nom+" attaque flammeche !", ""
        
    def roue_de_feu(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque roue de feu sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        if adversaire.type == "Plante":
            adversaire.pv = adversaire.pv - round(((self.attaque + (0.5*self.attaque))- adversaire.defense))
            return self.nom+" attaque roue-de-feu !", "C'est super efficace !"
        if adversaire.type == "Eau" or adversaire.type =="Feu":
            adversaire.pv = adversaire.pv - round(((self.attaque - (0.5*self.attaque)) - adversaire.defense))
            return self.nom+" attaque roue-de-feu !", "Ce n'est pas tres efficace..."
        else:
            adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
            return self.nom+" attaque roue-de-feu !",""
        
    def nitrocharge(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque nitrocharge sur un pokémon (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive and adversaire.vitesse >= 14:
            return self.nom+" attaque nitrocharge !", adversaire.nom+" esquive l'attaque !"
        else:
            if adversaire.type == "Plante" :
                adversaire.pv = adversaire.pv - round(((self.attaque + (0.7*self.attaque)) - adversaire.defense))
                self.vitesse = self.vitesse + 1
                return self.nom+" attaque nitrocharge !","C'est super efficace !"
            if adversaire.type == "Eau" or adversaire.type =="Feu":
                adversaire.pv = adversaire.pv - round(((self.attaque - (0.7*self.attaque)) - adversaire.defense))
                self.vitesse = self.vitesse + 1
                return self.nom+" attaque nitrocharge !","Ce n'est pas tres efficace..."
            else:
                adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
                self.vitesse = self.vitesse + 1
                return self.nom+" attaque nitrocharge !",""
            
    def lance_flammes(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque lance-flammes sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        if adversaire.type == "Plante":
            adversaire.pv = adversaire.pv - round(((self.attaque + (0.7*self.attaque))- adversaire.defense))
            return self.nom+" attaque lance-flammes !", "C'est super efficace !"
        if adversaire.type == "Eau" or adversaire.type =="Feu":
            adversaire.pv = adversaire.pv - round(((self.attaque - (0.6*self.attaque)) - adversaire.defense))
            return self.nom+" attaque lance-flammes !", "Ce n'est pas tres efficace..."
        else:
            adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
            return self.nom+" attaque lance-flammes !",""
    
    def poing_de_feu(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque Poing de feu sur un pokémon (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive or adversaire.vitesse >= 3* self.vitesse :
            return self.nom+" attaque Poing de feu !", adversaire.nom+" esquive l'attaque !"
        else:
            if adversaire.type == "Plante" :
                adversaire.pv = adversaire.pv - round(((self.attaque + (0.7*self.attaque)) - adversaire.defense))
                self.vitesse = self.vitesse + 1
                return self.nom+" attaque Poing de feu !","C'est super efficace !"
            if adversaire.type == "Eau" or adversaire.type =="Feu":
                adversaire.pv = adversaire.pv - round(((self.attaque - (0.5*self.attaque)) - adversaire.defense))
                self.vitesse = self.vitesse + 1
                return self.nom+" attaque Poing de feu !","Ce n'est pas tres efficace..."
            else:
                adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
                self.vitesse = self.vitesse + 1
                return self.nom+" attaque Poing de feu !",""
            
#------------------------------------------Fin attaques Feu-----------------------------------------------#

#------------------------------------------Debut attaques Plante-----------------------------------------------#
            
    def vol_vie(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque vol-vie sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        if adversaire.type == "Eau":
            adversaire.pv = adversaire.pv - round(((self.attaque + (0.5*self.attaque))- adversaire.defense))
            self.pv = self.pv + self.attaque
            if self.pv > self.pvBase:
                self.pv = self.pvBase
            return self.nom+" attaque vol-vie !","C'est super efficace !"
        if adversaire.type == "Feu" or adversaire.type == "Plante":
            adversaire.pv = adversaire.pv - round(((0.6*self.attaque) - adversaire.defense))
            self.pv = self.pv + round((0.5*self.attaque))
            if self.pv > self.pvBase:
                self.pv = self.pvBase
            return self.nom+" attaque vol-vie !","Ce n'est pas tres efficace..."
        else:
            adversaire.pv = adversaire.pv - round(((0.5*self.attaque)) - adversaire.defense)
            self.pv = self.pv + round((0.5*self.attaque))
            if self.pv > self.pvBase:
                self.pv = self.pvBase
            return self.nom+" attaque vol-vie !",""
        
    def feuille_magik(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque feuille magik sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        if adversaire.type == "Eau":
            adversaire.pv = adversaire.pv - round(((self.attaque + (0.5*self.attaque))- adversaire.defense))
            return self.nom+" attaque feuille magik !","C'est super efficace !"
        if adversaire.type == "Plante" or adversaire.type == "Feu":
            adversaire.pv = adversaire.pv - round(((self.attaque - (0.4*self.attaque)) - adversaire.defense))
            return self.nom+" attaque feuille magik !","Ce n'est pas tres efficace..."
        else:
            adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
            return self.nom+" attaque feuille magik !",""
    
        
    def fouet_lianes(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque fouet-lianes sur un pokémon (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive:
            return self.nom+" attaque fouet-lianes !", adversaire.nom+" esquive l'attaque !"
        else:
            if adversaire.type == "Eau":
                adversaire.pv = adversaire.pv - round(((self.attaque + (0.4*self.attaque))- adversaire.defense))
                return self.nom+" attaque fouet-lianes !","C'est super efficace !"
            if adversaire.type == "Plante" or adversaire.type =="Feu":
                adversaire.pv = adversaire.pv - round(((self.attaque - (0.4*self.attaque)) - adversaire.defense))
                return self.nom+" attaque fouet-lianes !","Ce n'est pas tres efficace..."
            else:
                adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
                return self.nom+" attaque fouet-lianes !",""
    
    def lance_soleil(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque lance soleil sur un pokémon (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralyse !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive or adversaire.vitesse >= 3* self.vitesse :
            return self.nom+" attaque lance-soleil !", adversaire.nom+" esquive l'attaque !"
        else:
            if adversaire.type == "Plante" or adversaire.type =="Feu":
                adversaire.pv = adversaire.pv - round(((self.attaque - (0.4*self.attaque))- adversaire.defense))
                return self.nom+" attaque lance-soleil !", "Ce n'est pas tres efficace..."
            if adversaire.type == "Eau":
                adversaire.pv = adversaire.pv - round(((self.attaque + (0.6*self.attaque)) - adversaire.defense))
                a = random.randint(0,2)
                if a == 0:
                    adversaire.statut = 1
                    return self.nom+" attaque lance-soleil et paralyse "+adversaire.nom+" !", "C'est super efficace !"
                return self.nom+" attaque lance-soleil !", "C'est super efficace !"
            else:
                adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
                return self.nom+" attaque lance-soleil !", ""

#------------------------------------------Fin Capacités Plante-----------------------------------------------#
            
#------------------------------------------Debut Capacités Eau-----------------------------------------------#

    def ecume(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque écume sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut pas attaquer..."
        if adversaire.type == "Feu":
            adversaire.pv = adversaire.pv - round(((self.attaque + (0.5*self.attaque)) - adversaire.defense))
            return self.nom+" attaque ecume !","C'est super efficace !"
        if adversaire.type == "Plante" or adversaire.type == "Eau":
            adversaire.pv = adversaire.pv - round(((self.attaque - (0.4*self.attaque))- adversaire.defense))
            return self.nom+" attaque ecume !","Ce n'est pas tres efficace..."
        else :
            adversaire.pv = adversaire.pv - (self.attaque- adversaire.defense)
            return self.nom+" attaque ecume !",""
        
    def vibraqua(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque vibraqua sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut pas attaquer..."
        if adversaire.type == "Feu":
            adversaire.pv = adversaire.pv - round(((self.attaque + (0.5*self.attaque))- adversaire.defense))
            return self.nom+" attaque vibraqua !","C'est super efficace !"
        if adversaire.type == "Plante" or adversaire.type == "Eau":
            adversaire.pv = adversaire.pv - round(((self.attaque - (0.4*self.attaque)) - adversaire.defense))
            return self.nom+" attaque vibraqua !","Ce n'est pas tres efficace..."
        else:
            adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
            return self.nom+" attaque vibraqua !",""
    
    def bulle_dO(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque bulle d'O sur un pokémon (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive:
            return self.nom+" attaque bulle d'O !", adversaire.nom+" esquive l'attaque !"
        else:
            if adversaire.type == "Feu":
                adversaire.pv = adversaire.pv - round(((self.attaque + (0.5*self.attaque))- adversaire.defense))
                return self.nom+" attaque bulle d'O !", "C'est super efficace !"
            if adversaire.type == "Plante" or adversaire.type == "Eau":
                adversaire.pv = adversaire.pv - round(((self.attaque - (0.5*self.attaque)) - adversaire.defense))
                return self.nom+" attaque bulle d'O !", "Ce n'est pas tres efficace..."
            else:
                adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
                return self.nom+" attaque bulle d'O !",""
    
    def surf(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque surf sur un pokémon (non-esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut pas attaquer..."
        if adversaire.type == "Feu":
            adversaire.pv = adversaire.pv - round(((self.attaque + (0.5*self.attaque))- adversaire.defense))
            return self.nom+" attaque surf !","C'est super efficace !"
        if adversaire.type == "Plante" or adversaire.type == "Eau":
            adversaire.pv = adversaire.pv - round(((self.attaque - (0.6*self.attaque)) - adversaire.defense))
            return self.nom+" attaque surf !","Ce n'est pas tres efficace..."
        else:
            adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
            return self.nom+" attaque surf !",""
    
    def hydro_queue(self,adversaire):
        """self,Pokemon -> void
        Précondition: aucune
        Rôle: Utilise l'attaque bulle d'O sur un pokémon (esquivable)"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut pas attaquer..."
        a = random.randint(0,100)
        if a <= adversaire.esquive or adversaire.vitesse >= 3* self.vitesse :
            return self.nom+" attaque hydro-queue !", adversaire.nom+" esquive l'attaque !"
        else:
            if adversaire.type == "Feu":
                adversaire.pv = adversaire.pv - round(((self.attaque + (0.6*self.attaque))- adversaire.defense))
                return self.nom+" attaque hydro-queue !", "C'est super efficace !"
            if adversaire.type == "Plante" or adversaire.type == "Eau":
                adversaire.pv = adversaire.pv - round(((self.attaque - (0.4*self.attaque)) - adversaire.defense))
                return self.nom+" attaque hydro-queue !", "Ce n'est pas tres efficace..."
            else:
                adversaire.pv = adversaire.pv - (self.attaque - adversaire.defense)
                return self.nom+" attaque hydro-queue !",""
        
#------------------------------------------Fin attaques Eau-----------------------------------------------#

#------------------------------------------Debut Capacités-----------------------------------------------#

    #capacité baisse defense
    def groz_yeux(self,adversaire):
        """self -> void
        Précondition: aucune
        Rôle: Baisse la défense de l'adversaire"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut plus attaquer..."
        adversaire.defense = adversaire.defense -1
        return self.nom+" utilise Gros Yeux !", "La defense de "+adversaire.nom+ " baisse !"
    
    def grincement(self,adversaire):
        """self -> void
        Précondition: aucune
        Rôle: Baisse la défense de l'adversaire"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut plus attaquer..."
        adversaire.defense = adversaire.defense -1
        return self.nom+" utilise grincement !", "La defense de "+adversaire.nom+ " baisse !"
    
    #capacité baisse attaque
    def rugissement(self,adversaire):
        """self -> void
        Précondition: aucune
        Rôle: Baisse l'attaque de l'adversaire"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut plus attaquer..."
        adversaire.attaque = adversaire.attaque -2
        return self.nom+" utilise rugissement !", "L'attaque de "+adversaire.nom+ " baisse !"
    
    #capacité augmente vitesse
    def hate(self):
        """self -> void
        Précondition: aucune
        Rôle: Augmente la vitesse du lanceur"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut plus attaquer..."
        self.vitesse = self.vitesse + 2
        return self.nom+" utilise hate !", "La vitesse de "+self.nom+ " augmente beaucoup !"
    
    #capacité augmente attaque
    def croissance(self):
        """self -> void
        Précondition: aucune
        Rôle: Augmente l'attaque du lanceur"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut plus attaquer..."
        self.attaque = self.attaque + 2
        return self.nom+" utilise croissance !", "L'attaque de "+self.nom+ " augmente !"
    
    #capacité baisse vitesse
    def grimace(self,adversaire):
        """self -> void
        Précondition: aucune
        Rôle: Baisse la vitesse de l'adversaire """
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut plus attaquer..."
        adversaire.vitesse = adversaire.vitesse - 2
        return self.nom+" utilise grimace !", "La vitesse de "+self.nom+ " baisse !"
    
#------------------------------------------Fin Capacités-----------------------------------------------#       

#------------------------------------------Debut Statut-----------------------------------------------#
    
    def test_statut(self):
        """liste(Pokémon) -> Pokémon
        Précondition: equipe != ["vide","vide","vide"]
        Rôle: Permet de tester si le pokémon peut attaquer ou non"""
        if self.statut == 1:
            return self.nom+" est paralise !", "Il ne peut plus attaquer..."
        return False

#------------------------------------------Fin Statut-----------------------------------------------#

#------------------------------------------Début BOT-----------------------------------------------# 

    def queFaire(self,adversaire,equipeEnnemie,sacEnnemie):
        """Pokémon,pokémon,liste[pokémon],liste[str] -> void
        Précondition: none
        Rôle: Définie l'action que doit faire le bot"""
        if self.pv <= 0:
            if self.nom == equipeEnnemie[0].nom:
                equipeEnnemie[0] = "vide"
                if equipeEnnemie[1] != "vide":
                    equipeEnnemie[0],equipeEnnemie[1] = equipeEnnemie[1],equipeEnnemie[0]
                    return self.nom+" est K.O !", equipeEnnemie[0].nom+" est envoye par l'adversaire !"
                if equipeEnnemie[1] == "vide" and equipeEnnemie[2] != "vide":
                    equipeEnnemie[0],equipeEnnemie[2] = equipeEnnemie[2],equipeEnnemie[0]
                    return self.nom+" est K.O !", equipeEnnemie[0].nom+" est envoye par l'adversaire !"
                if equipeEnnemie == ["vide","vide","vide"]:
                    return "Vous avez gagne !", ""
        if self.statut == 1 and sacEnnemie[3] == "anti-para":
            return self.anti_para(sacEnnemie)
        
        if self.pv < (self.pvBase / 4) and sacEnnemie != ["vide","vide","vide"]:
            if self.pvBase < 40 and sacEnnemie[0] == "potion":
                return self.potion(sacEnnemie)
            if self.pvBase > 40 and self.pvBase <80 and sacEnnemie[1] == "super-potion":
                return self.super_potion(sacEnnemie)
            if self.pvBase > 80 and sacEnnemie[2] == "hyper-potion":
                return self.hyper_potion(sacEnnemie)
            else:
                return self.attaqueBot(adversaire)
        else:
            return self.attaqueBot(adversaire)
        
    def attaqueBot(self,adversaire):
        """self,self -> void
        Précondition: none
        Rôle: Définie l'action que doit faire le bot"""
        if self.pv == self.pvBase and adversaire.vitesse > self.vitesse and self.type_cap == "vitesse_up":
            if self.capacite == "Hâte":
                return self.hate()
        if self.pv == self.pvBase and adversaire.pv > 3*self.attaque and self.type_cap == "attaque_up":
            if self.capacite == "Croissance":
                return self.croissance()
        if self.pv == self.pvBase and adversaire.pv > 3*self.attaque and self.type_cap == "defense_down":
            if self.capacite == "Groz'Yeux":
                return self.groz_yeux(adversaire)
            if self.capacite == "Grincement":
                return self.grincement(adversaire)
        if self.pv == self.pvBase and adversaire.attaque > self.pv//3 and self.type_cap == "attaque_down":
            if self.capacite == "Rugissement":
                return self.rugissement(adversaire)
        if self.pv == self.pvBase and adversaire.vitesse > self.vitesse and self.type_cap == "vitesse_down":
            if self.capacite == "Grimace":
                return self.grimace(adversaire)
        else:
            if ((adversaire.type == "Feu" or adversaire.type == "Eau") and self.type == "Feu") or ((adversaire.type == "Eau" or adversaire.type == "Plante") and self.type == "Eau") or \
               ((adversaire.type == "Plante" or adversaire.type == "Feu") and self.type == "Plante"):
                if self.vitesse > adversaire.vitesse and self.attaque3 == "Vive-attaque":
                    return self.vive_attaque(adversaire)
                else:
                    if self.attaque1 == "Charge":
                        return self.charge(adversaire)
                    if self.attaque1 == "Ecrasement":
                        return self.ecrasement(adversaire)
                    if self.attaque1 == "Feinte":
                        return self.feinte(adversaire)
                    if self.attaque1 == "Ligotage":
                        return self.ligotage(adversaire)
                    if self.attaque1 == "Etreinte":
                        return self.etreinte(adversaire)
            
            if adversaire.esquive >= 10 or adversaire.vitesse >= (self.vitesse*2):
                if self.attaque2 == "Flammèche":
                    return self.flammeche(adversaire)
                if self.attaque2 == "Vol-vie":
                    return self.vol_vie(adversaire)
                if self.attaque2 == "Ecume":
                    return self.ecume(adversaire)
                if self.attaque2 == "Roue de Feu":
                    return self.roue_de_feu(adversaire)
                if self.attaque2 == "Vibraqua":
                    return self.vibraqua(adversaire)
                if self.attaque2 == "Lance-flammes":
                    return self.lance_flammes(adversaire)
                if self.attaque2 == "Feuille Magik":
                    return self.feuille_magik(adversaire)
                if self.attaque2 == "Surf":
                    return self.surf(adversaire)
            else:
                if self.attaque3 == "Nitrocharge":
                    return self.nitrocharge(adversaire)
                if self.attaque3 == "Fouet-Lianes":
                    return self.fouet_lianes(adversaire)
                if self.attaque3 == "Bulle d'O":
                    return self.bulle_dO(adversaire)
                if self.attaque3 == "Hydro-queue":
                    return self.hydro_queue(adversaire)
                if self.attaque3 == "Poing de feu":
                    return self.poing_de_feu(adversaire)
                if self.attaque3 == "Lance-Soleil":
                    return self.lance_soleil(adversaire)
                if self.attaque3 == "Vive-attaque":
                    if self.attaque2 == "Flammèche":
                        return self.flammeche(adversaire)
                    if self.attaque2 == "Vol-vie":
                        return self.vol_vie(adversaire)
                    if self.attaque2 == "Ecume":
                        return self.ecume(adversaire)
                

#------------------------------------------Fin BOT-----------------------------------------------#
        
#------------------------------------------Debut soins-----------------------------------------------#       
        
    #soins
    def potion(pokemon,sac):
        """Pokemon -> void
        Précondition: aucune
        Rôle: Soigne le pokémon cible"""
        pokemon.pv = pokemon.pv + 20
        sac[0] = "vide"
        if pokemon.pv > pokemon.pvBase:
            pokemon.pv = pokemon.pvBase
        return pokemon.nom+" utilise une potion !", ""
    
    def super_potion(pokemon,sac):
        """Pokemon -> void
        Précondition: aucune
        Rôle: Soigne le pokémon cible"""
        pokemon.pv = pokemon.pv + 50
        sac[1] = "vide"
        if pokemon.pv > pokemon.pvBase:
            pokemon.pv = pokemon.pvBase
        return pokemon.nom+" utilise une super potion !", ""
    
    def hyper_potion(pokemon,sac):
        """Pokemon -> void
        Précondition: aucune
        Rôle: Soigne le pokémon cible"""
        pokemon.pv = pokemon.pv + 100
        sac[2] = "vide"
        if pokemon.pv > pokemon.pvBase:
            pokemon.pv = pokemon.pvBase
        return pokemon.nom+" utilise une hyper potion !",""
    
    def anti_para(pokemon,sac):
        """Pokemon -> void
        Précondition: aucune
        Rôle: Soigne le pokémon cible"""
        if pokemon.statut == 0:
            sac[3] = "vide"
            return "Vous utilisez un anti-para !", "Mais c'est inefficace !"
        if pokemon.statut == 1:
            pokemon.statut = 0
            sac[3] = "vide"
            return pokemon.nom+" utilise une potion anti-para", "Il n'est plus paralise !"
            
#------------------------------------------Fin soins-----------------------------------------------#

#--------------------------------------------Partie------------------------------------------------#

def changer(equipe,n):
    """liste(Pokémon) -> Pokémon
    Précondition: equipe != ["vide","vide","vide"]
    Rôle: Permet de changer le pokémon actif du joueur"""
    if equipe[n].pv <= 0:
        return "Le Pokemon est K.O","Choisissez un autre Pokemon !"
    r = equipe[0].nom
    if n == 0:
        return equipe[0].nom+" est deja sur le terrain !",""
    else:
        equipe[0],equipe[n] = equipe[n],equipe[0]
        return r+" reviens !", equipe[0].nom+" GO !"
    
#--------------------------------------------Partie------------------------------------------------#
    
#------------------------------------------Lancement de partie-----------------------------------------------#

def Equipe(equipe):
    """list(str) -> list(self)
    Précondition: none
    Rôle: compose notre équipe selon nos choix."""
    #self,nom,typePokemon,pv,vitesse,attaque,esquive,defense,attaque1,attaque2,attaque3,capacite,type_cap
    if equipe[0] == "Ouisticram":
        equipe[0] = Pokémon("Ouisticram","Feu",20,11,9,10,1,"Charge","Flammèche","Vive-attaque","Hâte","vitesse_up") #augmente la vitesse 
    if equipe[0] == "Tortipousse":
        equipe[0] = Pokémon("Tortipousse","Plante",30,8,7,4,3,"Charge","Vol-vie","Vive-attaque","Rugissement","attaque_down") #baisse attaque
    if equipe[0] == "Tiplouf":
        equipe[0] = Pokémon("Tiplouf","Eau",25,10,8,8,2,"Charge","Ecume","Vive-attaque","Rugissement","attaque_down") #baisse attaque
    if equipe[1] == "Galopa":
        equipe[1] = Pokémon("Galopa","Feu",55,18,18,10,2,"Ecrasement","Roue de Feu","Nitrocharge","Hâte","vitesse_up") #augmente la vitesse
    if equipe[1] == "Bouldeneu":
        equipe[1] = Pokémon("Bouldeneu","Plante",75,14,12,8,4,"Feinte","Vol-vie","Fouet-Lianes","Croissance","attaque_up") #augmente attaque
    if equipe[1] == "Tentacruel":
        equipe[1] = Pokémon("Tentacruel","Eau",60,16,15,5,3,"Ligotage","Vibraqua","Bulle d'O","Grincement","defense_down") #baisse defense
    if equipe[2] == "Maganon":
        equipe[2] = Pokémon("Maganon","Feu",110,15,35,6,3,"Feinte","Lance-flammes","Poing de feu","Groz'Yeux","defense_down") #baisse defense
    if equipe[2] == "Tropius":
        equipe[2] = Pokémon("Tropius","Plante",120,10,30,2,5,"Ecrasement","Feuille Magik","Lance-Soleil","Croissance","attaque_up")#augmente attaque
    if equipe[2] == "Leviator":
        equipe[2] = Pokémon("Leviator","Eau",90,22,40,10,4,"Etreinte","Surf","Hydro-queue","Grimace","vitesse_down") #baisse vitesse
        
    for i in range(len(listePokemon)):
        if equipe[0].nom == listePokemon[i]:
            listePokemon.pop(i)
            break
    for i in range(len(listePokemon1)):
        if equipe[1].nom == listePokemon1[i]:
            listePokemon1.pop(i)
            break
    for i in range(len(listePokemon2)):
        if equipe[2].nom == listePokemon2[i]:
            listePokemon2.pop(i)
            break

    #definir l'équipe ennemie
    pok1 = random.choice(listePokemon)
    pok2 = random.choice(listePokemon1)
    pok3 = random.choice(listePokemon2)
    if pok1 == "Ouisticram":
        pok1 = Pokémon("Ouisticram","Feu",20,11,9,10,1,"Charge","Flammèche","Vive-attaque","Hâte","vitesse_up")
    if pok1 == "Tortipousse":
        pok1 = Pokémon("Tortipousse","Plante",30,8,7,4,3,"Charge","Vol-vie","Vive-attaque","Rugissement","attaque_down")
    if pok1 == "Tiplouf":
        pok1 = Pokémon("Tiplouf","Eau",25,10,8,8,2,"Charge","Ecume","Vive-attaque","Rugissement","attaque_down")
    if pok2 == "Galopa":
        pok2 = Pokémon("Galopa","Feu",55,18,18,10,2,"Ecrasement","Roue de Feu","Nitrocharge","Hâte","vitesse_up")
    if pok2 == "Bouldeneu":
        pok2 = Pokémon("Bouldeneu","Plante",75,14,12,8,4,"Feinte","Vol-vie","Fouet-Lianes","Croissance","attaque_up")
    if pok2 == "Tentacruel":
        pok2 = Pokémon("Tentacruel","Eau",60,16,15,5,3,"Ligotage","Vibraqua","Bulle d'O","Grincement","defense_down")
    if pok3 == "Maganon":
        pok3 = Pokémon("Maganon","Feu",110,15,35,6,3,"Feinte","Lance-flammes","Poing de feu","Groz'Yeux","defense_down")
    if pok3 == "Tropius":
        pok3 = Pokémon("Tropius","Plante",120,10,30,2,5,"Ecrasement","Feuille Magik","Lance-Soleil","Croissance","attaque_up")
    if pok3 == "Leviator":
        pok3 = Pokémon("Leviator","Eau",90,22,40,10,4,"Etreinte","Surf","Hydro-queue","Grimace","vitesse_down")
    
    equipeEnnemie = [pok1,pok2,pok3]
    return equipe,equipeEnnemie

def Sac():
    """void -> void
    Précondition: aucune
    Rôle: Initialise les sacs"""
    sacEnnemie = ["potion","super-potion","hyper-potion","anti-para"]
    sac = ["Potion","Super-potion","Hyper-potion","Anti-para"]
    return sac,sacEnnemie

#------------------------------------------Lancement de partie-----------------------------------------------#

# equipe = ["Tiplouf","Galopa","Maganon"]
# equipe,equipeEnnemie = Equipe(equipe)
# sac,sacEnnemie = Sac() 
#print(equipe[0].charge(equipeEnnemie[0]))



##SYSTEME DE MOYENNE POUR PATCH LES POKEMONS OU NON
# list_pok = [Pokémon("Ouisticram","Feu",18,12,9,10,1,"Charge","Flammèche","Vive-attaque","Hâte","vitesse_up"),Pokémon("Tortipousse","Plante",30,8,7,4,3,"Charge","Vol-Vie","Vive-attaque","Rugissement","attaque_down"),
#             Pokémon("Tiplouf","Eau",25,10,8,8,2,"Charge","Ecume","Vive-attaque","Rugissement","attaque_down"),Pokémon("Galopa","Feu",55,18,18,10,2,"Ecrasement","Roue de Feu","Nitrocharge","Hâte","vitesse_up"),
#             Pokémon("Bouldeneu","Plante",75,14,12,8,4,"Feinte","Vol-Vie","Fouet-Lianes","Croissance","attaque_up"),Pokémon("Tentacruel","Eau",60,16,15,5,3,"Ligotage","Vibraqua","Bulle d'O","Grincement","defense_down"),
#             Pokémon("Maganon","Feu",110,15,35,6,3,"Feinte","Lance-flammes","Poing de feu","Groz'Yeux","defense_down"),Pokémon("Tropius","Plante",120,10,30,2,5,"Ecrasement","Feuille Magik","Lance-Soleil","Croissance","attaque_up"),
#             Pokémon("Leviator","Eau",90,22,40,10,4,"Etreinte","Surf","Hydro-queue","Grimace","vitesse_down")]
# i=0
# while i != len(list_pok):
#     print(list_pok[i].nom,(list_pok[i].pv+list_pok[i].vitesse+list_pok[i].attaque+list_pok[i].esquive+ list_pok[i].defense)/5)
#     i=i+1



