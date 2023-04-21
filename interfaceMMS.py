"""
Structure pygame
"""

#--------- importations -----------#

import pygame       # importation de pygame dans un espace propre
from pygame.locals import *
import colorsys
import math  
import codeMMS
import animation

#--------- fonctions utilisées-----------#


def Aff_centre(text,taille,couleur):
    """str,int,(int,int,int) -> void
        Précondition: aucune
        Rôle: affiche au centre de la fenetre un texte."""
    police = pygame.font.Font("police/Pixellari.ttf",taille) 
    texte = police.render(text,True,couleur)
    rectTexte = texte.get_rect()
    rectTexte.center = rectFenetre.center
    fenetre.blit(texte,rectTexte)
    
def Suivant():
    """void -> void
        Précondition: aucune
        Rôle: affiche le "bouton" Suivant."""
    police = pygame.font.Font("police/Pixellari.ttf",50)
    texte = police.render("Suivant",True,blanc)
    fenetre.blit(texte,(965,700))
    
def Retour():
    """void -> void
        Précondition: aucune
        Rôle: affiche le "bouton" Retour."""
    police = pygame.font.Font("police/Pixellari.ttf",50)
    texte = police.render("Retour",True,blanc)
    fenetre.blit(texte,(30,700))
    
    
def contour_pe(x_s1,x_s2,y_s1,y_s2):
    """int,int,int,int -> void
        Précondition: les x et y doivent être compris entre 0 et la longueur/largeur
        Rôle: affiche le contour pour Préparé son équipe."""
    x_s, y_s = pygame.mouse.get_pos()
    if x_s1<=x_s<=x_s2 and y_s1<=y_s<=y_s2:
        pygame.draw.rect(fenetre,blanc,(largeur//2-(x_s2-x_s1)//2,hauteur//2-(y_s2-y_s1)//2-34,x_s2-x_s1,y_s2-y_s1+60))
        pygame.draw.rect(fenetre,gris,(largeur//2-(x_s2-x_s1)//2,hauteur//2-(y_s2-y_s1)//2-21,x_s2-x_s1,y_s2-y_s1+34))
    else:
        fenetre.fill(gris)
            
def contour_q(x_s1,x_s2,y_s1,y_s2):
    """int,int,int,int -> void
        Précondition: les x et y doivent être compris entre 0 et la longueur/largeur
        Rôle: affiche le contour pour Quitter."""
    x_s, y_s = pygame.mouse.get_pos()
    if x_s1<=x_s<=x_s2 and y_s1<=y_s<=y_s2:
        pygame.draw.rect(fenetre,blanc,(30,687,x_s2-x_s1,y_s2-y_s1+30))
        pygame.draw.rect(fenetre,gris,(30,694,x_s2-x_s1,y_s2-y_s1+15))
        
def contour_r(x_s1,x_s2,y_s1,y_s2):
    """int,int,int,int -> void
        Précondition: les x et y doivent être compris entre 0 et la longueur/largeur
        Rôle: affiche le contour pour Retour."""
    x_s, y_s = pygame.mouse.get_pos()
    if x_s1<=x_s<=x_s2 and y_s1<=y_s<=y_s2:
        pygame.draw.rect(fenetre,blanc,(30,687,x_s2-x_s1-10,y_s2-y_s1+30))
        pygame.draw.rect(fenetre,gris,(30,694,x_s2-x_s1-10,y_s2-y_s1+15))
    else:
        pygame.draw.rect(fenetre,gris,(30,687,x_s2-x_s1-10,y_s2-y_s1+30))

def contour_s(x_s1,x_s2,y_s1,y_s2):
    """int,int,int,int -> void
        Précondition: les x et y doivent être compris entre 0 et la longueur/largeur
        Rôle: affiche le contour pour Suivant."""
    x_s, y_s = pygame.mouse.get_pos()
    if x_s1<=x_s<=x_s2 and y_s1<=y_s<=y_s2:
        pygame.draw.rect(fenetre,blanc,(965,687,x_s2-x_s1,y_s2-y_s1+30))
        pygame.draw.rect(fenetre,gris,(965,694,x_s2-x_s1,y_s2-y_s1+15))
    else:
        pygame.draw.rect(fenetre,gris,(965,687,x_s2-x_s1,y_s2-y_s1+30))
        
def resumequipe():
    """void -> void
        Précondition: Aucune
        Rôle: affiche le résumer de l'équipe lors de sa création ."""
    center = (largeur//4)+(largeur//8)*3, hauteur//2+hauteur//2.6
    rect = carre.get_rect()
    rect.center = center
    fenetre.blit(carre,(rect))
            
    center = (largeur//4)*2, hauteur//2+hauteur//2.6
    rect = carre.get_rect()
    rect.center = center
    fenetre.blit(carre,(rect))
            
    center = (largeur//8)*3, hauteur//2+hauteur//2.6
    rect = carre.get_rect()
    rect.center = center
    fenetre.blit(carre,(rect))
    if equipe[0]=="Ouisticram":
        center = (largeur//8)*3, hauteur//2+hauteur//2.6
        rect = image1.get_rect()
        rect.center = center
        fenetre.blit(image1,(rect))
    if equipe[0]=="Tiplouf":
        center = (largeur//8)*3, hauteur//2+hauteur//2.6
        rect = image2.get_rect()
        rect.center = center
        fenetre.blit(image2,(rect))
    if equipe[0]=="Tortipousse":
        center = (largeur//8)*3, hauteur//2+hauteur//2.6
        rect = image3.get_rect()
        rect.center = center
        fenetre.blit(image3,(rect))
        
    if equipe[1]=="Galopa":
        center = (largeur//4)*2, hauteur//2+hauteur//2.6-5
        rect = image4.get_rect()
        rect.center = center
        fenetre.blit(image4,(rect))
    if equipe[1]=="Bouldeneu":
        center = (largeur//4)*2, hauteur//2+hauteur//2.6-5
        rect = image5.get_rect()
        rect.center = center
        fenetre.blit(image5,(rect))
    if equipe[1]=="Tentacruel":
        center = (largeur//4)*2, hauteur//2+hauteur//2.6-5
        rect = image6.get_rect()
        rect.center = center
        fenetre.blit(image6,(rect))
    
    if equipe[2]=="Leviator":
        center = (largeur//4)+(largeur//8)*3, hauteur//2+hauteur//2.6-10
        rect = image7.get_rect()
        rect.center = center
        fenetre.blit(image7,(rect))
    if equipe[2]=="Tropius":
        center = (largeur//4)+(largeur//8)*3, hauteur//2+hauteur//2.6-10
        rect = image8.get_rect()
        rect.center = center
        fenetre.blit(image8,(rect))
    if equipe[2]=="Maganon":
        center = (largeur//4)+(largeur//8)*3, hauteur//2+hauteur//2.6-10
        rect = image9.get_rect()
        rect.center = center
        fenetre.blit(image9,(rect))
    
def text_animation(texte,couleur,pos,taille):
    """str,(int,int,int),(int,int),int -> void
        Précondition: aucun
        Rôle: affiche un texte de manière animé."""
    text=''
    for i in range(len(texte)):
        text+=texte[i]
        police=pygame.font.Font("police/pokemon.ttf",taille)
        text_surface=police.render(text,True,couleur)
        fenetre.blit(text_surface,pos)
        pygame.display.update()
        pygame.time.wait(35)

def nb_pv():
    """void -> void
        Précondition: aucun
        Rôle: affiche les points de vie allié au combat."""
    if equipe[0].pv//100>=1:
        texte = police.render(str(equipe[0].pv),True,(60,60,60))
        fenetre.blit(texte,(900,496))
        texte = police.render(str(equipe[0].pv),True,blanc)
        fenetre.blit(texte,(896,492))
    else:
        texte = police.render(str(equipe[0].pv),True,(60,60,60))
        fenetre.blit(texte,(920,496))
        texte = police.render(str(equipe[0].pv),True,blanc)
        fenetre.blit(texte,(916,492))
        
    
def nb_pvm():
    """void -> void
        Précondition: aucun
        Rôle: affiche les points de vie ennemie au combat."""
    texte = police.render(str(pvm),True,(60,60,60))
    fenetre.blit(texte,(1020,496))
    texte = police.render(str(pvm),True,blanc)
    fenetre.blit(texte,(1016,492))
   
   
#initialisation de variable utiliser dans le code

equipe= [0,0,0]        
victoire=False
pok=0
anim_combat=True
nfenetre=0

b=0
o=0
D=0
k=0
d=0
F=0
u=0
h=1
h1=0

#compétance
vive_attaque=False
charge=False
flammeche=False
vol_vie=False
ecume=False
ecrasement=False
nitrocharge=False
roue_de_feu=False
feinte=False
fouet_lianes=False
vibraqua=False
bulle_dO=False
lance_soleil=False
lance_flammes=False
ligotage=False
poing_de_feu=False
hydro_queue=False
surf=False
etreinte=False
feuille_magik=False
gros_yeux=False
grincement=False
rugissement=False
hate=False
croissance=False
grimace=False

#changement de pokémon
choix=False
changement1=False
changement2=False
changement3=False
Action_bot=False
impossible_pok=False
test=False

#utilisation du sac
action_sac=None
soigne1=False
soigne2=False
soigne3=False
nb_pot=1
nb_spot=1
nb_hpot=1
nb_para=1

#action possible
Attaque=False
Sac=False
Pokemon=False
base_inter=True

#couleurs utilisées
bleu=(0,0,250)
rouge=(250,0,0)
vert=(0,250,0)
blanc=(250,250,250)
noir=(0,0,0)
gris=(112,112,112)

#--------- partie principale -----------#

pygame.init()  # lancement de pygame

pygame.display.set_caption("Pokémon MMS")
# dimensions de la fenetre :
largeur = 1152 # largeur en pixels
hauteur = 768 # hauteur en pixels

try:
    fenetre = pygame.display.set_mode((largeur,hauteur))
    rectFenetre = fenetre.get_rect()
    Aff_centre("Chargement du jeu",60,blanc)
    pygame.display.flip()
    
    #importation d'un partie des images utilisées
    carre=pygame.image.load("Img/carré.png")
    carre=pygame.transform.scale(carre, (100, 100))
    image1=pygame.image.load("Img/Base/Ouisticram.png")
    image2=pygame.image.load("Img/Base/tiplouf.png")
    image3=pygame.image.load("Img/Base/tortipousse.png")
    image4=pygame.image.load("Img/1 evol/Galopa.png")
    image5=pygame.image.load("Img/1 evol/Bouldeneu.png")
    image6=pygame.image.load("Img/1 evol/Tentacruel.png")
    image7=pygame.image.load("Img/2 evol/Leviator.png")
    image8=pygame.image.load("Img/2 evol/Tropius.png")
    image9=pygame.image.load("Img/2 evol/Maganon.png")
    
    image10=pygame.image.load("Img/Combat/battle1.png")
    image11=pygame.image.load("Img/Combat/battle2.png")
    image12=pygame.image.load("Img/Combat/jungle.png")
    image13=pygame.image.load("Img/Combat/trainer2.png")
    image15=pygame.image.load("Img/Combat/flèche.png")
    image16=pygame.image.load("Img/Combat/battle1_.png")
    image17=pygame.image.load("Img/Combat/battle3.png")
    image18=pygame.image.load("Img/Combat/Sac.png")
    image19=pygame.image.load("Img/Combat/Pokemon.png")
    image20=pygame.image.load("Img/Combat/battle2_.png")
    image21=pygame.image.load("Img/Combat/Pokemon_choix.png")
    
    image1b=pygame.image.load("Img/Base/Ouisticramb.png")
    image2b=pygame.image.load("Img/Base/tiploufb.png")
    image3b=pygame.image.load("Img/Base/tortipousseb.png")
    image4b=pygame.image.load("Img/1 evol/Galopab.png")
    image5b=pygame.image.load("Img/1 evol/Bouldeneub.png")
    image6b=pygame.image.load("Img/1 evol/Tentacruelb.png")
    image7b=pygame.image.load("Img/2 evol/Leviatorb.png")
    image8b=pygame.image.load("Img/2 evol/Tropiusb.png")
    image9b=pygame.image.load("Img/2 evol/Maganonb.png")
    
    #importation des sons/musiques
    clc1= pygame.mixer.Sound('Son/clc_1.mp3')
    clc2= pygame.mixer.Sound('Son/clc_2.mp3')
    clc3= pygame.mixer.Sound('Son/clc_3.mp3')
    cb_pok= pygame.mixer.Sound('Son/pokemon_combat.mp3')
    #reglage du volume
    clc1.set_volume(0.2)
    clc2.set_volume(0.2)
    clc3.set_volume(0.2)
    cb_pok.set_volume(0.04)
    
    
#-----------------------------------------------------------------------------
    
    continuer = True
    pygame.display.flip()
    while continuer:
        #print(pygame.mouse.get_pos()) #utiliser seulement pour obtenir des coordonnées facilement
        pygame.display.flip()

            
            
        
#--------- Fenetre de base -----------#
        

        if nfenetre==0:
            fenetre.fill(gris)
            contour_pe(265,890,352,402)
            contour_q(30,185,700,738)
            Aff_centre("Prépare ton équipe !",70,blanc)
            police = pygame.font.Font("police/Pixellari.ttf",50)
            texte = police.render("Quitter",True,blanc)               
            fenetre.blit(texte,(30,700))
            for event in pygame.event.get(): # on prend le premier événement de la pile
                if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                    continuer = False
                if event.type==MOUSEBUTTONDOWN:
                    x,y=event.pos
                    if 30<=x<=185 and 700<=y<=738: # clic sur "Quitter" ferme la fenêtre
                        continuer=False
                    elif 265<=x<=890 and 352<=y<=402: # clic sur "Suivant" ferme la fenêtre
                        nfenetre=1
                        clc3.play()
                        fenetre.fill(gris)
                        c=0  
                    else:
                        Action=None
                        
                        
#--------- Fenetre numéro 1 -----------#
                                     
        elif nfenetre==1:
            #redimension des images
            img1 = pygame.transform.scale(image1, (300, 300))
            img2 = pygame.transform.scale(image2, (300, 300))
            img3 = pygame.transform.scale(image3, (300, 300))
            img1b = pygame.transform.scale(image1b, (312, 312))
            img2b = pygame.transform.scale(image2b, (312, 312))
            img3b = pygame.transform.scale(image3b, (312, 312))
            
            x_s, y_s = pygame.mouse.get_pos()
            if 198<=x_s<=377 and 72<=y_s<=341: #Ouisitcram contour
                center = largeur//4, hauteur//4
                rect = img1b.get_rect()
                rect.center = center
                fenetre.blit(img1b,rect)
            else:
                pygame.draw.rect(fenetre,gris,(0,0,1000,350))
            
            if 498<=x_s<=659 and 132<=y_s<=341: #Tiplouf contour
                center = largeur//2, hauteur//4
                rect = img2b.get_rect()
                rect.center = center
                fenetre.blit(img2b,rect)


            if 768<=x_s<=953 and 90<=y_s<=341: #Tortipousse contour
                center = largeur//2+largeur//4, hauteur//4
                rect = img3b.get_rect()
                rect.center = center
                fenetre.blit(img3b,rect)
                
            contour_s(967,1122,702,738)
            
            #affiche les pokemons basiques
            center = largeur//4, hauteur//4
            rect = img1.get_rect()
            rect.center = center
            fenetre.blit(img1,rect)
            
            center = largeur//2, hauteur//4
            rect = img2.get_rect()
            rect.center = center
            fenetre.blit(img2,rect)
            
            center = largeur//2+largeur//4, hauteur//4
            rect = img3.get_rect()
            rect.center = center
            fenetre.blit(img3,(rect))
            
            resumequipe()
            
            Suivant()
            rectTexte = texte.get_rect()
            rectTexte.center = rectFenetre.center
            
            for event in pygame.event.get(): # on prend le premier événement de la pile
                if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                    continuer = False
                if event.type==MOUSEBUTTONDOWN:
                    x,y=event.pos
                    if 198<=x<=377 and 72<=y<=341: # Img\Combat\Ouisticram est choisi
                        fenetre.fill(gris)
                        Aff_centre("Tu as choisi Ouisticram",40,blanc)
                        equipe[0]="Ouisticram"
                        pok=1
                        clc1.play()
                    elif 498<=x<=659 and 132<=y<=341: # Tiplouf est choisi
                        fenetre.fill(gris)
                        Aff_centre("Tu as choisi Tiplouf",40,blanc)
                        equipe[0]="Tiplouf"
                        pok=1
                        clc1.play()
                    elif 768<=x<=953 and 90<=y<=341: # Tortipousse est choisi
                        fenetre.fill(gris)
                        Aff_centre("Tu as choisi Tortipousse",40,blanc)
                        equipe[0]="Tortipousse"
                        pok=1
                        clc1.play()
                    elif 967<=x<=1122 and 702<=y<=738: # fenetre suivante
                        if pok==1:
                            clc3.play()
                            fenetre.fill(gris)
                            nfenetre=2
                        else:
                            Aff_centre("Tu dois choisir un pokémon",40,blanc) # aucun pokemon choisi
                            
                            
#--------- Fenetre numéro 2 -----------#
                            
                            
        elif nfenetre==2:
            #redimension des images
            img4b = pygame.transform.scale(image4b, (312, 312))
            img5b = pygame.transform.scale(image5b, (312, 312))
            img6b = pygame.transform.scale(image6b, (312, 312))
            x_s, y_s = pygame.mouse.get_pos()
            if 172<=x_s<=408 and 99<=y_s<=341: #galopa contour
                center = largeur//4, hauteur//4
                rect = img4b.get_rect()
                rect.center = center
                fenetre.blit(img4b,rect)
            else:
                pygame.draw.rect(fenetre,gris,(0,0,1000,350))
            
            if 440<=x_s<=708 and 126<=y_s<=341: #bouldeneu contour
                center = largeur//2, hauteur//4
                rect = img5b.get_rect()
                rect.center = center
                fenetre.blit(img5b,rect)

            if 731<=x_s<=967 and 132<=y_s<=340: #tentacruel contour
                center = largeur//2+largeur//4, hauteur//4
                rect = img6b.get_rect()
                rect.center = center
                fenetre.blit(img6b,rect)
                
            contour_r(30,185,700,738)
            contour_s(967,1122,702,738)
            
        #affiche les pokemons
            img4 = pygame.transform.scale(image4, (300, 300))
            img5 = pygame.transform.scale(image5, (300, 300))
            img6 = pygame.transform.scale(image6, (300, 300))
            
            center = largeur//4, hauteur//4
            rect = img4.get_rect()
            rect.center = center
            fenetre.blit(img4,rect)
            
            center = largeur//2, hauteur//4
            rect = img5.get_rect()
            rect.center = center
            fenetre.blit(img5,rect)
            
            center = largeur//2+largeur//4, hauteur//4
            rect = img6.get_rect()
            rect.center = center
            fenetre.blit(img6,(rect))
            
            resumequipe()
            
            Suivant()
            Retour()
            
            for event in pygame.event.get(): # on prend le premier événement de la pile
                if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                    continuer = False
                if event.type==MOUSEBUTTONDOWN:
                    x,y=event.pos
                    if 172<=x<=408 and 99<=y<=341: # Galopa est choisi
                        fenetre.fill(gris)
                        Aff_centre("Tu as choisi Galopa",40,blanc)
                        equipe[1]="Galopa"
                        pok=2
                        clc1.play()
                    elif 440<=x<=708 and 126<=y<=341: # Bouldeneu est choisi
                        fenetre.fill(gris)
                        Aff_centre("Tu as choisi Bouldeneu",40,blanc)
                        equipe[1]="Bouldeneu"
                        pok=2
                        clc1.play()
                    elif 731<=x<=967 and 132<=y<=340: # Tentacruel est choisi
                        fenetre.fill(gris)
                        Aff_centre("Tu as choisi Tentacruel",40,blanc)
                        equipe[1]="Tentacruel"
                        pok=2
                        clc1.play()
                    elif 967<=x<=1122 and 702<=y<=738: # Suivant
                        if pok==2:
                            clc3.play()
                            fenetre.fill(gris)
                            nfenetre=3
                        else:
                            Aff_centre("Tu dois choisir un pokémon",40,blanc) # Aucun pokemon choisit
                    elif 32<=x<=174 and 702<=y<=739: # Retour
                        clc2.play()
                        fenetre.fill(gris)
                        nfenetre=1
                        
                        
#--------- Fenetre numéro 3 -----------#
                        
                        
        elif nfenetre==3:
            #redimension des images
            img7b = pygame.transform.scale(image7b, (312, 312))
            img8b = pygame.transform.scale(image8b, (312, 312))
            img9b = pygame.transform.scale(image9b, (312, 312))
            x_s, y_s = pygame.mouse.get_pos()
            if 157<=x_s<=397 and 110<=y_s<=341: #Leviator contour
                center = largeur//4, hauteur//4
                rect = img7b.get_rect()
                rect.center = center
                fenetre.blit(img7b,rect)
            else:
                pygame.draw.rect(fenetre,gris,(0,0,1000,350))
            
            if 456<=x_s<=705 and 99<=y_s<=341: #Tropius contour
                center = largeur//2, hauteur//4
                rect = img8b.get_rect()
                rect.center = center
                fenetre.blit(img8b,rect)


            if 765<=x_s<=965 and 121<=y_s<=340: #  Maganon contour
                center = largeur//2+largeur//4, hauteur//4
                rect = img9b.get_rect()
                rect.center = center
                fenetre.blit(img9b,rect)
            contour_r(30,185,700,738)
            contour_s(967,1122,702,738)
            #affichage des pokemons
            img7 = pygame.transform.scale(image7, (300, 300))
            img8 = pygame.transform.scale(image8, (300, 300))
            img9 = pygame.transform.scale(image9, (300, 300))
            
            center = largeur//4, hauteur//4
            rect = img7.get_rect()
            rect.center = center
            fenetre.blit(img7,rect)
            
            center = largeur//2, hauteur//4
            rect = img8.get_rect()
            rect.center = center
            fenetre.blit(img8,rect)
            
            center = largeur//2+largeur//4, hauteur//4
            rect = img9.get_rect()
            rect.center = center
            fenetre.blit(img9,(rect))
            
            resumequipe()
            
            Suivant()
            Retour()
            
            for event in pygame.event.get(): # on prend le premier événement de la pile
                if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                    continuer = False
                if event.type==MOUSEBUTTONDOWN:
                    x,y=event.pos
                    if 157<=x<=397 and 110<=y<=341: # Leviator est choisi
                        fenetre.fill(gris)
                        Aff_centre("Tu as choisi Leviator",40,blanc)
                        equipe[2]="Leviator"
                        pok=3
                        clc1.play()
                    elif 456<=x<=705 and 99<=y<=341: # Tropius est choisi
                        fenetre.fill(gris)
                        Aff_centre("Tu as choisi Tropius",40,blanc)
                        equipe[2]="Tropius"
                        pok=3
                        clc1.play()
                    elif 765<=x<=965 and 121<=y<=340: # Maganon est choisi
                        fenetre.fill(gris)
                        Aff_centre("Tu as choisi Maganon",40,blanc)
                        equipe[2]="Maganon"
                        pok=3
                        clc1.play()
                    elif 967<=x<=1122 and 702<=y<=738: # Suivant
                        if pok==3:
                            clc3.play()
                            fenetre.fill(gris)
                            nfenetre=4
                            equipe,equipeEnnemie = codeMMS.Equipe(equipe)
                            sac,sacEnnemie = codeMMS.Sac()
                            print(equipe[0].nom,",",equipe[1].nom,",",equipe[2].nom)
                        else:
                            Aff_centre("Tu dois choisir un pokémon",40,blanc) #aucun pokemon choisit
                    elif 32<=x<=174 and 702<=y<=739: # Retour
                        clc2.play()
                        fenetre.fill(gris)
                        nfenetre=2
                        

#--------- Fenetre avant-combat -----------#
                        
                        
        elif nfenetre==4:
            #redimension des images
            img12 = pygame.transform.scale(image12, (2001, 782))
            img13 = pygame.transform.scale(image13, (390, 468))
            if c==0:
                center = largeur//2, hauteur//2
                rect = img12.get_rect()
                rect.center = center
                fenetre.blit(img12,rect)
                center = largeur//2, hauteur//2
                rect = img13.get_rect()
                rect.center = center
                fenetre.blit(img13,rect)
            for event in pygame.event.get(): # on prend le premier événement de la pile
                if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                    continuer = False
                if event.type==MOUSEBUTTONDOWN:
                    x,y=event.pos
                    if 0<=x<=1152 and 0<=y<=768: # Transition vers le combat
                        clc1.play()
                        if k==0:
                            text_animation("C'est dangereux de se balader seul dans les bois",blanc,(38,700),30)
                            k=1
                    
                        c=c+1
                        if c==2:
                            nfenetre=5
                            cb_pok.play(loops=-1, maxtime=0, fade_ms=0)
                            b=0
                            f=0
                            P0=217/equipe[0].pvBase
                            P1=217/equipe[1].pvBase
                            P2=217/equipe[2].pvBase
        
#--------- Fenetre combat -----------#
                        
        elif nfenetre==5:
            # Vérification d'un possible défaite/victoire
            if equipe[0].pv<=0 and equipe[1].pv<=0 and equipe[2].pv<=0:
                nfenetre=6
            if equipeEnnemie==["vide","vide","vide"]:
                victoire=True
                nfenetre=6
            else:
                pok_ennemi= equipeEnnemie[0].nom
                pok_act= equipe[0].nom
                # Mis à jour des point de vie (pv)
                if d==0:
                    if equipe[0].pv>=0:
                        P=207/equipe[0].pvBase
                        d=1
                if D==0:
                    if equipeEnnemie[0].pv>=0:
                        M=217/equipeEnnemie[0].pvBase
                        D=1
                if F==0:
                    P0=217/equipe[0].pvBase
                    P1=217/equipe[1].pvBase
                    P2=217/equipe[2].pvBase
                    F=5
                
            if equipe[0].pv<=0:
                fenetre.blit(img20,rect)
                base_inter=False
                Pokemon=True
                pv=0
                d=0
                F=0
                if h1==0:
                    h=0
                    h1=1
            else:
                pvm=equipe[0].pvBase
                pv=1
            if h==0 and not (equipe[0].pv<=0 and equipe[1].pv<=0 and equipe[2].pv<=0):
                text_animation(equipe[0].nom+" est K.O",blanc,(40,615),20)
                text_animation("Choisissez un nouveau pokemon",blanc,(40,645),20)
                pygame.time.wait(750)
                h=1
            
            img11= pygame.transform.scale(image11, (1152, 768))
            img20 = pygame.transform.scale(image20, (1152, 768))
            rect = img11.get_rect()
            rect.center = center
            if k==1:
                fenetre.blit(img11,rect)
                text_animation("Vous envoyez "+pok_act+" !",blanc,(40,615),20)
                pygame.time.wait(750)
                k=2
            
            #executions des attaques 
            if charge==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].charge(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                charge=False
                Action_bot=True
            if vive_attaque==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].vive_attaque(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                vive_attaque=False
                Action_bot=True
            if flammeche==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].flammeche(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                flammeche=False
                Action_bot=True
            if vol_vie==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].vol_vie(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                vol_vie=False
                Action_bot=True
            if ecume==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].ecume(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                ecume=False
                Action_bot=True
            if ecrasement==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].ecrasement(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                ecrasement=False
                Action_bot=True
            if nitrocharge==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].nitrocharge(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                nitrocharge=False
                Action_bot=True
            if roue_de_feu==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].roue_de_feu(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                roue_de_feu=False
                Action_bot=True
            if feinte==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].feinte(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                feinte=False
                Action_bot=True
            if fouet_lianes==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].fouet_lianes(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                fouet_lianes=False
                Action_bot=True
            if bulle_dO==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].bulle_dO(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                bulle_dO=False
                Action_bot=True
            if lance_soleil==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].lance_soleil(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                lance_soleil=False
                Action_bot=True
            if lance_flammes==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].lance_flammes(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                lance_flammes=False
                Action_bot=True
            if ligotage==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].ligotage(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                ligotage=False
                Action_bot=True
            if poing_de_feu==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].poing_de_feu(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                poing_de_feu=False
                Action_bot=True
            if surf==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].surf(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                surf=False
                Action_bot=True
            if vibraqua==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].vibraqua(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                vibraqua=False
                Action_bot=True
            if etreinte==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].etreinte(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                etreinte=False
                Action_bot=True
            if hydro_queue==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].hydro_queue(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                hydro_queue=False
                Action_bot=True
            if feuille_magik==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].feuille_magik(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                feuille_magik=False
                Action_bot=True
                
                
                
            if grincement==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].grincement(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                grincement=False
                Action_bot=True
            if hate==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].hate()
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                hate=False
                Action_bot=True
            if rugissement==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].rugissement(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                rugissement=False
                Action_bot=True
            if croissance==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].croissance()
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                croissance=False
                Action_bot=True
            if grimace==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].grimace(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                grimace=False
                Action_bot=True
            if gros_yeux==True:
                fenetre.blit(img20,rect)
                a,b=equipe[0].groz_yeux(equipeEnnemie[0])
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                gros_yeux=False
                Action_bot=True
                                 
                
            if f==0:
                def Animation_ennemi(): #affichage des animations de pokemon
                    if pok_ennemi=="Ouisticram":
                        animation.ouisticram2_anim.attack()
                        animation.moving_sprites_ouisticram2.draw(fenetre)
                        texte = police.render("Ouisticram",True,(60,60,60))
                        fenetre.blit(texte,(15,118))
                        texte = police.render("Ouisticram",True,blanc)
                        fenetre.blit(texte,(11,114))
                        pygame.display.flip()  
                    if pok_ennemi=="Tiplouf":
                        animation.tiplouf2_anim.attack()
                        animation.moving_sprites_tiplouf2.draw(fenetre)
                        texte = police.render("Tiplouf",True,(60,60,60))
                        fenetre.blit(texte,(15,118))
                        texte = police.render("Tiplouf",True,blanc)
                        fenetre.blit(texte,(11,114))
                        pygame.display.flip()            
                    if pok_ennemi=="Tortipousse":
                        animation.tortipousse2_anim.attack()
                        animation.moving_sprites_tortipousse2.draw(fenetre)
                        texte = police.render("Tortipousse",True,(60,60,60))
                        fenetre.blit(texte,(15,118))
                        texte = police.render("Tortipousse",True,blanc)
                        fenetre.blit(texte,(11,114))
                        pygame.display.flip()
                    if pok_ennemi=="Galopa":
                        animation.galopa2_anim.attack()
                        animation.moving_sprites_galopa2.draw(fenetre)
                        texte = police.render("Galopa",True,(60,60,60))
                        fenetre.blit(texte,(15,118))
                        texte = police.render("Galopa",True,blanc)
                        fenetre.blit(texte,(11,114))
                        pygame.display.flip()
                    if pok_ennemi=="Bouldeneu":
                        animation.bouldeneu2_anim.attack()
                        animation.moving_sprites_bouldeneu2.draw(fenetre)
                        texte = police.render("Bouldeneu",True,(60,60,60))
                        fenetre.blit(texte,(15,118))
                        texte = police.render("Bouldeneu",True,blanc)
                        fenetre.blit(texte,(11,114))
                        pygame.display.flip()
                    if pok_ennemi=="Tentacruel":
                        animation.tentacruel2_anim.attack()
                        animation.moving_sprites_tentacruel2.draw(fenetre)
                        texte = police.render("Tentacruel",True,(60,60,60))
                        fenetre.blit(texte,(15,118))
                        texte = police.render("Tentacruel",True,blanc)
                        fenetre.blit(texte,(11,114))
                        pygame.display.flip()
                    if pok_ennemi=="Leviator":
                        animation.leviator2_anim.attack()
                        animation.moving_sprites_leviator2.draw(fenetre)
                        texte = police.render("Leviator",True,(60,60,60))
                        fenetre.blit(texte,(15,118))
                        texte = police.render("Leviator",True,blanc)
                        fenetre.blit(texte,(11,114))
                        pygame.display.flip()
                    if pok_ennemi=="Tropius":
                        animation.tropius2_anim.attack()
                        animation.moving_sprites_tropius2.draw(fenetre)
                        texte = police.render("Tropius",True,(60,60,60))
                        fenetre.blit(texte,(15,118))
                        texte = police.render("Tropius",True,blanc)
                        fenetre.blit(texte,(11,114))
                        pygame.display.flip()
                    if pok_ennemi=="Maganon":
                        animation.maganon2_anim.attack()
                        animation.moving_sprites_maganon2.draw(fenetre)
                        texte = police.render("Maganon",True,(60,60,60))
                        fenetre.blit(texte,(15,118))
                        texte = police.render("Maganon",True,blanc)
                        fenetre.blit(texte,(11,114))
                        pygame.display.flip()
                f=1
                
            img10 = pygame.transform.scale(image10, (1152, 768))
            img15 = pygame.transform.scale(image15, (15, 25))
            img16 = pygame.transform.scale(image16, (1152, 768))
            img17 = pygame.transform.scale(image17, (1152, 768))
            img18 = pygame.transform.scale(image18, (1152, 768))
            img19 = pygame.transform.scale(image19, (1152, 768))
            img21 = pygame.transform.scale(image21, (1152, 768))
            
            police = pygame.font.Font("police/Pokemon.ttf",30)
            
            x_s, y_s = pygame.mouse.get_pos()
            # affichage de la base du combat
            if base_inter==True:
                impossible_pok=False
                anim_combat=True
                center = largeur//2, hauteur//2
                rect = img10.get_rect()
                rect.center = center
                fenetre.blit(img10,rect)
                police = pygame.font.Font("police/Pokemon.ttf",30)
                if 648<=x_s<=824 and 621<=y_s<=650:
                    fenetre.blit(img15,(623,624))
                texte = police.render("Attaque",True,noir)
                fenetre.blit(texte,(648,618))
                
               
                if 946<=x_s<=1025 and 621<=y_s<=648:
                    fenetre.blit(img15,(919,624))
                texte = police.render("Sac",True,noir)
                fenetre.blit(texte,(945,618))
                
                
                if 648<=x_s<=835 and 696<=y_s<=724:
                    fenetre.blit(img15,(623,700))
                texte = police.render("Pokemon",True,noir)
                fenetre.blit(texte,(648,695))
                
                
                if 946<=x_s<=1052 and 696<=y_s<=724:
                    fenetre.blit(img15,(920,700))
                texte = police.render("Fuite",True,noir)
                fenetre.blit(texte,(945,695))
            
            
            # affichage des attaques possibles propres a chaques pokemons
            if Attaque==True:
                if pok_act=="Ouisticram":
                    fenetre.blit(img17,rect)
                    texte = police.render("Charge",True,noir)
                    fenetre.blit(texte,(70,620))                        
                    texte = police.render("Vive-attaque",True,noir)
                    fenetre.blit(texte,(450,620))   
                    texte = police.render("Flammeche",True,noir)
                    fenetre.blit(texte,(70,695))   
                    texte = police.render("Hate",True,noir)
                    fenetre.blit(texte,(450,695))    

                if pok_act=="Tortipousse":
                    fenetre.blit(img17,rect)
                    texte = police.render("Charge",True,noir)
                    fenetre.blit(texte,(70,620))       
                    texte = police.render("Vive-attaque",True,noir)
                    fenetre.blit(texte,(450,620))       
                    texte = police.render("Vol-vie",True,noir)
                    fenetre.blit(texte,(70,695))                          
                    texte = police.render("Rugissement",True,noir)
                    fenetre.blit(texte,(450,695))    
                
                if pok_act=="Tiplouf":
                    fenetre.blit(img17,rect)
                    texte = police.render("Charge",True,noir)
                    fenetre.blit(texte,(70,620))                       
                    texte = police.render("Vive-attaque",True,noir)
                    fenetre.blit(texte,(450,620))   
                    texte = police.render("Ecume",True,noir)
                    fenetre.blit(texte,(70,695))   
                    texte = police.render("Rugissement",True,noir)
                    fenetre.blit(texte,(450,695))    
                
                if pok_act=="Galopa":
                    fenetre.blit(img17,rect)
                    texte = police.render("Ecrasement",True,noir)
                    fenetre.blit(texte,(70,620))  
                    texte = police.render("Roue de Feu",True,noir)
                    fenetre.blit(texte,(450,620))                          
                    texte = police.render("Nitrocharge",True,noir)
                    fenetre.blit(texte,(70,695))   
                    texte = police.render("Hate",True,noir)
                    fenetre.blit(texte,(450,695))
                    
                if pok_act=="Bouldeneu":
                    fenetre.blit(img17,rect)
                    texte = police.render("Feinte",True,noir)
                    fenetre.blit(texte,(70,620))                    
                    texte = police.render("Fouet-Lianes",True,noir)
                    fenetre.blit(texte,(450,620))               
                    texte = police.render("Vol-Vie",True,noir)
                    fenetre.blit(texte,(70,695))         
                    texte = police.render("Croissance",True,noir)
                    fenetre.blit(texte,(450,695))
                    
                if pok_act=="Tentacruel":
                    fenetre.blit(img17,rect)
                    texte = police.render("Ligotage",True,noir)
                    fenetre.blit(texte,(70,620))
                    texte = police.render("Bulle d'O",True,noir)
                    fenetre.blit(texte,(450,620))   
                    texte = police.render("Vibraqua",True,noir)
                    fenetre.blit(texte,(70,695))   
                    texte = police.render("Grincement",True,noir)
                    fenetre.blit(texte,(450,695))
                    
                if pok_act=="Tropius":
                    fenetre.blit(img17,rect)
                    texte = police.render("Ecrasement",True,noir)
                    fenetre.blit(texte,(70,620))
                    texte = police.render("Feuille Magik",True,noir)
                    fenetre.blit(texte,(450,620))   
                    texte = police.render("Lance-Soleil",True,noir)
                    fenetre.blit(texte,(70,695))   
                    texte = police.render("Croissance",True,noir)
                    fenetre.blit(texte,(450,695))    

                if pok_act=="Leviator":
                    fenetre.blit(img17,rect)
                    texte = police.render("Etreinte",True,noir)
                    fenetre.blit(texte,(70,620))
                    texte = police.render("Hydro-queue",True,noir)
                    fenetre.blit(texte,(450,620))   
                    texte = police.render("Surf",True,noir)
                    fenetre.blit(texte,(70,695))   
                    texte = police.render("Grimace",True,noir)
                    fenetre.blit(texte,(450,695))    

                if pok_act=="Maganon":
                    fenetre.blit(img17,rect)
                    texte = police.render("Feinte",True,noir)
                    fenetre.blit(texte,(70,620))
                    texte = police.render("Poing de feu",True,noir)
                    fenetre.blit(texte,(450,620))   
                    texte = police.render("Lance-flammes",True,noir)
                    fenetre.blit(texte,(70,695))   
                    texte = police.render("Groz'Yeux",True,noir)
                    fenetre.blit(texte,(450,695))
                    
                texte = police.render("Retour",True,noir) 
                fenetre.blit(texte,(915,655))
                if 854<=x_s<=1126 and 596<=y_s<=752:
                    fenetre.blit(img15,(890,660))
                    
                    
                if 70<=x_s<=419 and 596<=y_s<=674:
                    fenetre.blit(img15,(45,625))
                if 420<=x_s<=795 and 596<=y_s<=674:
                    fenetre.blit(img15,(425,625))                         
                if 70<=x_s<=419 and 675<=y_s<=754:
                    fenetre.blit(img15,(45,700))                       
                if 420<=x_s<=795 and 675<=y_s<=754:
                    fenetre.blit(img15,(425,700))
        
            #definition de la vitesse de l'animation
            animation.moving_sprites_ouisticram.update(0.48)
            animation.moving_sprites_tortipousse.update(0.39)
            animation.moving_sprites_tiplouf.update(0.30)
            animation.moving_sprites_galopa.update(0.46)
            animation.moving_sprites_bouldeneu.update(0.28)
            animation.moving_sprites_tentacruel.update(0.50)
            animation.moving_sprites_leviator.update(0.32)
            animation.moving_sprites_tropius.update(0.30)
            animation.moving_sprites_maganon.update(0.44)
            
            animation.moving_sprites_ouisticram2.update(0.50)
            animation.moving_sprites_tortipousse2.update(0.40)
            animation.moving_sprites_tiplouf2.update(0.30)
            animation.moving_sprites_galopa2.update(0.46)
            animation.moving_sprites_bouldeneu2.update(0.28)
            animation.moving_sprites_tentacruel2.update(0.50)
            animation.moving_sprites_leviator2.update(0.32)
            animation.moving_sprites_tropius2.update(0.30)
            animation.moving_sprites_maganon2.update(0.44)
            
            animation.moving_sprites_tropius1_pokemon.update(0.30)
            animation.moving_sprites_tropius2_pokemon.update(0.30)
            animation.moving_sprites_tropius3_pokemon.update(0.30)
            animation.moving_sprites_leviator1_pokemon.update(0.20)
            animation.moving_sprites_leviator2_pokemon.update(0.20)
            animation.moving_sprites_leviator3_pokemon.update(0.20)
            animation.moving_sprites_maganon1_pokemon.update(0.10)
            animation.moving_sprites_maganon2_pokemon.update(0.10)
            animation.moving_sprites_maganon3_pokemon.update(0.10)
            animation.moving_sprites_tentacruel1_pokemon.update(0.26)
            animation.moving_sprites_tentacruel2_pokemon.update(0.26)
            animation.moving_sprites_tentacruel3_pokemon.update(0.26)
            animation.moving_sprites_bouldeneu1_pokemon.update(0.08)
            animation.moving_sprites_bouldeneu2_pokemon.update(0.08)
            animation.moving_sprites_bouldeneu3_pokemon.update(0.08)
            animation.moving_sprites_galopa1_pokemon.update(0.30)
            animation.moving_sprites_galopa2_pokemon.update(0.30)
            animation.moving_sprites_galopa3_pokemon.update(0.30)
            animation.moving_sprites_tortipousse1_pokemon.update(0.12)
            animation.moving_sprites_tortipousse2_pokemon.update(0.12)
            animation.moving_sprites_tortipousse3_pokemon.update(0.12)
            animation.moving_sprites_ouisticram1_pokemon.update(0.10)
            animation.moving_sprites_ouisticram2_pokemon.update(0.10)
            animation.moving_sprites_ouisticram3_pokemon.update(0.10)
            animation.moving_sprites_tiplouf1_pokemon.update(0.24)
            animation.moving_sprites_tiplouf2_pokemon.update(0.24)
            animation.moving_sprites_tiplouf3_pokemon.update(0.24)
            
           
            
            if anim_combat==True: # barre des pv en combat
                if not (equipe[0].pv<=0 and equipe[1].pv<=0 and equipe[2].pv<=0):
                    if equipe[0].pv>0:
                        bar_length = min(abs(equipe[0].pv), equipe[0].pvBase)
                        bar_percentage = bar_length/equipe[0].pvBase
                        h, s, v = 0.33*bar_percentage, 1, 1
                        red,green,blue = colorsys.hsv_to_rgb(h, s, v)
                        colour = [int(255*red),int(255*green),int(255*blue)]
                        pygame.draw.line(fenetre, colour, (909, 483), (909+equipe[0].pv*P,483),8)
                    

                if equipeEnnemie!=["vide","vide","vide"]:
                    if equipeEnnemie[0].pv>0:
                        bar_length = min(abs(equipeEnnemie[0].pv), equipeEnnemie[0].pvBase)
                        bar_percentage = bar_length/equipeEnnemie[0].pvBase
                        h, s, v = 0.33*bar_percentage, 1, 1
                        red,green,blue = colorsys.hsv_to_rgb(h, s, v)
                        colour = [int(255*red),int(255*green),int(255*blue)]
                        pygame.draw.line(fenetre, colour, (226, 179), (226+equipeEnnemie[0].pv*M,179),8)
                        
                
                if pv==1:
                    nb_pv()
                    nb_pvm()
                # affichage des noms de pokemon
                if pok_act=="Ouisticram":
                    animation.ouisticram_anim.attack()
                    animation.moving_sprites_ouisticram.draw(fenetre)
                    texte = police.render("Ouisticram",True,(60,60,60))
                    fenetre.blit(texte,(715,422))
                    texte = police.render("Ouisticram",True,blanc)
                    fenetre.blit(texte,(711,418))
                    
                    Animation_ennemi()
                    pygame.display.flip()
                if pok_act=="Tiplouf":
                    animation.tiplouf_anim.attack()
                    animation.moving_sprites_tiplouf.draw(fenetre)
                    texte = police.render("Tiplouf",True,(60,60,60))
                    fenetre.blit(texte,(715,422))
                    texte = police.render("Tiplouf",True,blanc)
                    fenetre.blit(texte,(711,418))
                    Animation_ennemi()
                    
                    pygame.display.flip()            
                if pok_act=="Tortipousse":
                    animation.tortipousse_anim.attack()
                    animation.moving_sprites_tortipousse.draw(fenetre)
                    texte = police.render("Tortipousse",True,(60,60,60))
                    fenetre.blit(texte,(715,422))
                    texte = police.render("Tortipousse",True,blanc)
                    fenetre.blit(texte,(711,418))
                    Animation_ennemi()
                    
                    pygame.display.flip()
                if pok_act=="Galopa":
                    animation.galopa_anim.attack()
                    animation.moving_sprites_galopa.draw(fenetre)
                    texte = police.render("Galopa",True,(60,60,60))
                    fenetre.blit(texte,(715,422))
                    texte = police.render("Galopa",True,blanc)
                    fenetre.blit(texte,(711,418))
                    Animation_ennemi()
                    pygame.display.flip()
                if pok_act=="Bouldeneu":
                    animation.bouldeneu_anim.attack()
                    animation.moving_sprites_bouldeneu.draw(fenetre)
                    texte = police.render("Bouldeneu",True,(60,60,60))
                    fenetre.blit(texte,(715,422))
                    texte = police.render("Bouldeneu",True,blanc)
                    fenetre.blit(texte,(711,418))
                    Animation_ennemi()
                    
                    pygame.display.flip()
                if pok_act=="Tentacruel":
                    animation.tentacruel_anim.attack()
                    animation.moving_sprites_tentacruel.draw(fenetre)
                    texte = police.render("Tentacruel",True,(60,60,60))
                    fenetre.blit(texte,(715,422))
                    texte = police.render("Tentacruel",True,blanc)
                    fenetre.blit(texte,(711,418))
                    Animation_ennemi()
                    
                    pygame.display.flip()
                if pok_act=="Leviator":
                    animation.leviator_anim.attack()
                    animation.moving_sprites_leviator.draw(fenetre)
                    texte = police.render("Leviator",True,(60,60,60))
                    fenetre.blit(texte,(715,422))
                    texte = police.render("Leviator",True,blanc)
                    fenetre.blit(texte,(711,418))
                    Animation_ennemi()
                    
                    pygame.display.flip()
                if pok_act=="Tropius":
                    animation.tropius_anim.attack()
                    animation.moving_sprites_tropius.draw(fenetre)
                    texte = police.render("Tropius",True,(60,60,60))
                    fenetre.blit(texte,(715,422))
                    texte = police.render("Tropius",True,blanc)
                    fenetre.blit(texte,(711,418))
                    Animation_ennemi()
                    
                    pygame.display.flip()
                if pok_act=="Maganon":
                    animation.maganon_anim.attack()
                    animation.moving_sprites_maganon.draw(fenetre)
                    texte = police.render("Maganon",True,(60,60,60))
                    fenetre.blit(texte,(715,422))
                    texte = police.render("Maganon",True,blanc)
                    fenetre.blit(texte,(711,418))
                    Animation_ennemi()
                    
                    pygame.display.flip()
                    
            if Action_bot==True: # tour du BOT
                fenetre.blit(img20,rect)
                if equipeEnnemie[0].pv<=0:
                    D=0
                a,b=equipeEnnemie[0].queFaire(equipe[0],equipeEnnemie,sacEnnemie)
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                pygame.time.delay(750)
                h1=0
                Action_bot=False
                
            if Pokemon==True: # affichage des pokemons pour changement ou soin
                anim_combat=False
                fenetre.blit(img19,rect)
                police = pygame.font.Font("police/Pokemon.ttf",20)
                texte = police.render(equipe[0].nom,True,blanc)
                fenetre.blit(texte,(18,145))
                texte = police.render(equipe[1].nom,True,blanc)
                fenetre.blit(texte,(595,178))
                texte = police.render(equipe[2].nom,True,blanc)
                fenetre.blit(texte,(18,338))
                police = pygame.font.Font("police/Pokemon.ttf",30)
                    
                texte = police.render("Retour",True,blanc) 
                fenetre.blit(texte,(945,688))
                texte = police.render("Choisi un pokemon.",True,noir) 
                fenetre.blit(texte,(50,688))
                if equipe[2].nom=="Maganon":
                    animation.maganon3_pokemon_anim.attack()
                    animation.moving_sprites_maganon3_pokemon.draw(fenetre)
                if equipe[2].nom=="Tropius":
                    animation.tropius3_pokemon_anim.attack()
                    animation.moving_sprites_tropius3_pokemon.draw(fenetre)
                if equipe[2].nom=="Leviator":
                    animation.leviator3_pokemon_anim.attack()
                    animation.moving_sprites_leviator3_pokemon.draw(fenetre)
                if equipe[2].nom=="Ouisticram":
                    animation.ouisticram3_pokemon_anim.attack()
                    animation.moving_sprites_ouisticram3_pokemon.draw(fenetre)
                if equipe[2].nom=="Tiplouf":
                    animation.tiplouf3_pokemon_anim.attack()
                    animation.moving_sprites_tiplouf3_pokemon.draw(fenetre)
                if equipe[2].nom=="Tortipousse":
                    animation.tortipousse3_pokemon_anim.attack()
                    animation.moving_sprites_tortipousse3_pokemon.draw(fenetre)
                if equipe[2].nom=="Tentacruel":
                    animation.tentacruel3_pokemon_anim.attack()
                    animation.moving_sprites_tentacruel3_pokemon.draw(fenetre)
                if equipe[2].nom=="Galopa":
                    animation.galopa3_pokemon_anim.attack()
                    animation.moving_sprites_galopa3_pokemon.draw(fenetre)
                if equipe[2].nom=="Bouldeneu":
                    animation.bouldeneu3_pokemon_anim.attack()
                    animation.moving_sprites_bouldeneu3_pokemon.draw(fenetre)
                    
                if equipe[1].nom=="Maganon":
                    animation.maganon2_pokemon_anim.attack()
                    animation.moving_sprites_maganon2_pokemon.draw(fenetre)
                if equipe[1].nom=="Tropius":
                    animation.tropius2_pokemon_anim.attack()
                    animation.moving_sprites_tropius2_pokemon.draw(fenetre)
                if equipe[1].nom=="Leviator":
                    animation.leviator2_pokemon_anim.attack()
                    animation.moving_sprites_leviator2_pokemon.draw(fenetre)
                if equipe[1].nom=="Ouisticram":
                    animation.ouisticram2_pokemon_anim.attack()
                    animation.moving_sprites_ouisticram2_pokemon.draw(fenetre)
                if equipe[1].nom=="Tiplouf":
                    animation.tiplouf2_pokemon_anim.attack()
                    animation.moving_sprites_tiplouf2_pokemon.draw(fenetre)
                if equipe[1].nom=="Tortipousse":
                    animation.tortipousse2_pokemon_anim.attack()
                    animation.moving_sprites_tortipousse2_pokemon.draw(fenetre)
                if equipe[1].nom=="Tentacruel":
                    animation.tentacruel2_pokemon_anim.attack()
                    animation.moving_sprites_tentacruel2_pokemon.draw(fenetre)
                if equipe[1].nom=="Galopa":
                    animation.galopa2_pokemon_anim.attack()
                    animation.moving_sprites_galopa2_pokemon.draw(fenetre)
                if equipe[1].nom=="Bouldeneu":
                    animation.bouldeneu2_pokemon_anim.attack()
                    animation.moving_sprites_bouldeneu2_pokemon.draw(fenetre)
                    
                if equipe[0].nom=="Maganon":
                    animation.maganon1_pokemon_anim.attack()
                    animation.moving_sprites_maganon1_pokemon.draw(fenetre)
                if equipe[0].nom=="Tropius":
                    animation.tropius1_pokemon_anim.attack()
                    animation.moving_sprites_tropius1_pokemon.draw(fenetre)
                if equipe[0].nom=="Leviator":
                    animation.leviator1_pokemon_anim.attack()
                    animation.moving_sprites_leviator1_pokemon.draw(fenetre)
                if equipe[0].nom=="Ouisticram":
                    animation.ouisticram1_pokemon_anim.attack()
                    animation.moving_sprites_ouisticram1_pokemon.draw(fenetre)
                if equipe[0].nom=="Tiplouf":
                    animation.tiplouf1_pokemon_anim.attack()
                    animation.moving_sprites_tiplouf1_pokemon.draw(fenetre)
                if equipe[0].nom=="Tortipousse":
                    animation.tortipousse1_pokemon_anim.attack()
                    animation.moving_sprites_tortipousse1_pokemon.draw(fenetre)
                if equipe[0].nom=="Tentacruel":
                    animation.tentacruel1_pokemon_anim.attack()
                    animation.moving_sprites_tentacruel1_pokemon.draw(fenetre)
                if equipe[0].nom=="Galopa":
                    animation.galopa1_pokemon_anim.attack()
                    animation.moving_sprites_galopa1_pokemon.draw(fenetre)
                if equipe[0].nom=="Bouldeneu":
                    animation.bouldeneu1_pokemon_anim.attack()
                    animation.moving_sprites_bouldeneu1_pokemon.draw(fenetre)
                    
                #bar de pv de chaques pokemon 
                
                if equipe[0].pv>0:
                    bar_length = min(abs(equipe[0].pv), equipe[0].pvBase)
                    bar_percentage = bar_length/equipe[0].pvBase
                    h, s, v = 0.33*bar_percentage, 1, 1
                    red,green,blue = colorsys.hsv_to_rgb(h, s, v)
                    colour = [int(255*red),int(255*green),int(255*blue)]
                    pygame.draw.line(fenetre, colour, (288, 112), (288+equipe[0].pv*P0,112),15)
                else:
                    None
                    

                if equipe[1].pv>0:
                    bar_length = min(abs(equipe[1].pv), equipe[1].pvBase)
                    bar_percentage = bar_length/equipe[1].pvBase
                    h, s, v = 0.33*bar_percentage, 1, 1
                    red,green,blue = colorsys.hsv_to_rgb(h, s, v)
                    colour = [int(255*red),int(255*green),int(255*blue)]
                    pygame.draw.line(fenetre, colour, (863, 144), (863+equipe[1].pv*P1,144),15)
                else:
                    None

                if equipe[2].pv>0:
                    bar_length = min(abs(equipe[2].pv), equipe[2].pvBase)
                    bar_percentage = bar_length/equipe[2].pvBase
                    h, s, v = 0.33*bar_percentage, 1, 1
                    red,green,blue = colorsys.hsv_to_rgb(h, s, v)
                    colour = [int(255*red),int(255*green),int(255*blue)]
                    pygame.draw.line(fenetre, colour, (288, 304), (288+equipe[2].pv*P2,304),15)
                else:
                    None
                    
                if 904<=x_s<=1134 and 670<=y_s<=738:
                    texte = police.render("Retour",True,gris) 
                    fenetre.blit(texte,(945,688))
                    
                if choix=="En cours":
                    fenetre.blit(img21,rect)
                    texte = police.render("Envoyer "+equipe[pok_choix].nom+" ?",True,blanc)
                    rectTexte = texte.get_rect()
                    rectTexte.center = rectFenetre.center
                    rectTexte[1]=rectTexte[1]-75
                    fenetre.blit(texte,rectTexte)
                    texte = police.render("Oui",True,blanc)
                    fenetre.blit(texte,(275,460))
                    texte = police.render("Non",True,blanc)
                    fenetre.blit(texte,(784,460))
                    
                
                
            if changement1==True:
                a,b = codeMMS.changer(equipe,0)
                if equipe[0].pv<=0:
                    impossible_pok=True
                else:
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    changement1=False
                
            if changement2==True:
                a,b = codeMMS.changer(equipe,1)
                if equipe[1].pv<=0:
                    impossible_pok=True
                else:
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    F=0
                    d=0
                    h=1
                    Action_bot=True
                    changement2=False

            if changement3==True:
                a,b = codeMMS.changer(equipe,2)
                if equipe[2].pv<=0:
                    impossible_pok=True
                else:
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    F=0
                    d=0
                    h=1
                    changement3=False
                    Action_bot=True

            if soigne1==True: # action possible dans le sac
                if action_sac=="potion":
                    a,b=equipe[0].potion(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne1=False
                    action_sac=None
                    Action_bot=True
                if action_sac=="super_potion":
                    a,b=equipe[0].super_potion(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne1=False
                    action_sac=None
                    Action_bot=True
                if action_sac=="hyper_potion":
                    a,b=equipe[0].hyper_potion(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne1=False
                    Action_bot=True
                if action_sac=="anti_para":
                    a,b=equipe[0].anti_para(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne1=False
                    Action_bot=True
                u=0

            
            if soigne2==True:
                if action_sac=="potion":
                    a,b=equipe[1].potion(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne2=False
                    action_sac=None
                    Action_bot=True
                if action_sac=="super_potion":
                    a,b=equipe[1].super_potion(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne2=False
                    action_sac=None
                    Action_bot=True
                if action_sac=="hyper_potion":
                    a,b=equipe[1].hyper_potion(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne2=False
                    Action_bot=True
                if action_sac=="anti_para":
                    a,b=equipe[1].anti_para(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne2=False
                    Action_bot=True
                u=0
            
            if soigne3==True:
                if action_sac=="potion":
                    a,b=equipe[2].potion(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne3=False
                    action_sac=None
                    Action_bot=True
                if action_sac=="super_potion":
                    a,b=equipe[2].super_potion(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne3=False
                    action_sac=None
                    Action_bot=True
                if action_sac=="hyper_potion":
                    a,b=equipe[2].hyper_potion(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne3=False
                    Action_bot=True
                if action_sac=="anti_para":
                    a,b=equipe[2].anti_para(sac)
                    text_animation(a,blanc,(40,615),20)
                    text_animation(b,blanc,(40,645),20)
                    pygame.time.wait(750)
                    soigne3=False
                    Action_bot=True
                u=0
                

                
            if Sac==True: # affichage du sac
                anim_combat=False
                fenetre.blit(img18,rect)
                texte = police.render("Retour",True,noir) 
                fenetre.blit(texte,(945,650))
                texte = police.render("Objets",True,noir) 
                fenetre.blit(texte,(220,408))
                if 945<=x_s<=1096 and 650<=y_s<=678:
                    texte = police.render("Retour",True,blanc) 
                    fenetre.blit(texte,(945,650))
                if 539<=x_s<=1114 and 84<=y_s<=166 and sac[0]=="Potion":
                    texte = police.render("Un spray qui soigne les",True,noir)
                    fenetre.blit(texte,(24,510))
                    texte = police.render("blessures. Restaure",True,noir)
                    fenetre.blit(texte,(24,550))
                    texte = police.render("20 PV a un Pokemon.",True,noir)
                    fenetre.blit(texte,(24,590)) 
                if 539<=x_s<=1114 and 167<=y_s<=236 and sac[1]=="Super-potion":
                    texte = police.render("Un spray qui soigne les",True,noir)
                    fenetre.blit(texte,(24,510))
                    texte = police.render("blessures. Restaure",True,noir)
                    fenetre.blit(texte,(24,550))
                    texte = police.render("50 PV a un Pokemon.",True,noir)
                    fenetre.blit(texte,(24,590)) 
                if 539<=x_s<=1114 and 237<=y_s<=300 and sac[2]=="Hyper-potion":
                    texte = police.render("Un spray qui soigne les",True,noir)
                    fenetre.blit(texte,(24,510))
                    texte = police.render("blessures. Restaure",True,noir)
                    fenetre.blit(texte,(24,550))
                    texte = police.render("100 PV a un Pokemon.",True,noir)
                    fenetre.blit(texte,(24,590))
                if 539<=x_s<=1114 and 301<=y_s<=373 and sac[3]=="Anti-para":
                    texte = police.render("Un medicament sous",True,noir)
                    fenetre.blit(texte,(24,510))
                    texte = police.render("forme de spray.",True,noir)
                    fenetre.blit(texte,(24,550))
                    texte = police.render("Soigne un Pokemon",True,noir)
                    fenetre.blit(texte,(24,590))
                    texte = police.render("de la paralysie.",True,noir)
                    fenetre.blit(texte,(24,630))
                    
                texte = police.render(sac[0],True,noir)
                fenetre.blit(texte,(560,110))   
                texte = police.render(sac[1],True,noir) 
                fenetre.blit(texte,(560,180))
                texte = police.render(sac[2],True,noir) 
                fenetre.blit(texte,(560,250))
                texte = police.render(sac[3],True,noir) 
                fenetre.blit(texte,(560,320))
            
            if test==True:
                text_animation(a,blanc,(40,615),20)
                text_animation(b,blanc,(40,645),20)
                test=False
                
            if impossible_pok==True:
                if equipe[0].pv<=0:
                    fenetre.blit(img21,rect)
                    texte = police.render(a,True,blanc)
                    rectTexte = texte.get_rect()
                    rectTexte.center = rectFenetre.center
                    rectTexte[1]=rectTexte[1]-75
                    fenetre.blit(texte,rectTexte)
                    texte = police.render(b,True,blanc)
                    rectTexte = texte.get_rect()
                    rectTexte.center = rectFenetre.center
                    fenetre.blit(texte,rectTexte)
                else:
                    base_inter=True
                    Pokemon=False
                    choix=False
                    test=True
                    impossible_pok=False
                changement1=False
                changement2=False
                changement3=False
                
                
            
            
            for event in pygame.event.get(): # on prend le premier événement de la pile
                if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                    continuer = False
                if event.type==MOUSEBUTTONDOWN:
                    if base_inter==True: # zones cliquables dans l'interface de combat basique
                        if 648<=x_s<=824 and 621<=y_s<=650:
                            base_inter=False
                            Attaque=True
                            x_s=0
                        if 946<=x_s<=1025 and 621<=y_s<=648:
                            base_inter=False
                            Sac=True
                        if 648<=x_s<=835 and 696<=y_s<=724:
                            base_inter=False
                            Pokemon=True
                        if 946<=x_s<=1052 and 696<=y_s<=724:
                            text_animation("Battez-vous comme un homme !",blanc,(40,615),20)
                            pygame.time.wait(750)
                            
                    if Attaque==True: # zones cliquables dans l'interface de combat Attaque
                        if 854<=x_s<=1126 and 596<=y_s<=752:
                                Attaque=False
                                base_inter=True
                                
                        if pok_act=="Ouisticram":                             
                            if 70<=x_s<=419 and 596<=y_s<=674:
                                Attaque=False
                                base_inter=True
                                charge=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 596<=y_s<=674:                               
                                Attaque=False
                                base_inter=True
                                vive_attaque=True
                                fenetre.blit(img20,rect)
                            if 70<=x_s<=419 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                flammeche=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                hate=True
                                fenetre.blit(img20,rect)
                        if pok_act=="Tiplouf":                             
                            if 70<=x_s<=419 and 596<=y_s<=674:
                                Attaque=False
                                base_inter=True
                                charge=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 596<=y_s<=674:                               
                                Attaque=False
                                base_inter=True
                                vive_attaque=True
                                fenetre.blit(img20,rect)
                            if 70<=x_s<=419 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                ecume=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                rugissement=True
                                fenetre.blit(img20,rect)
                        if pok_act=="Tortipousse":                             
                            if 70<=x_s<=419 and 596<=y_s<=674:
                                Attaque=False
                                base_inter=True
                                charge=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 596<=y_s<=674:                               
                                Attaque=False
                                base_inter=True
                                vive_attaque=True
                                fenetre.blit(img20,rect)
                            if 70<=x_s<=419 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                vol_vie=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                rugissement=True
                                fenetre.blit(img20,rect)
                        if pok_act=="Bouldeneu":                             
                            if 70<=x_s<=419 and 596<=y_s<=674:
                                Attaque=False
                                base_inter=True
                                feinte=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 596<=y_s<=674:                               
                                Attaque=False
                                base_inter=True
                                fouet_lianes=True
                                fenetre.blit(img20,rect)
                            if 70<=x_s<=419 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                vol_vie=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                croissance=True
                                fenetre.blit(img20,rect)
                        if pok_act=="Galopa":                             
                            if 70<=x_s<=419 and 596<=y_s<=674:
                                Attaque=False
                                base_inter=True
                                ecrasement=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 596<=y_s<=674:                               
                                Attaque=False
                                base_inter=True
                                roue_de_feu=True
                                fenetre.blit(img20,rect)
                            if 70<=x_s<=419 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                nitrocharge=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                hate=True
                                fenetre.blit(img20,rect)
                        if pok_act=="Tentacruel":                             
                            if 70<=x_s<=419 and 596<=y_s<=674:
                                Attaque=False
                                base_inter=True
                                ligotage=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 596<=y_s<=674:                               
                                Attaque=False
                                base_inter=True
                                bulle_dO=True
                                fenetre.blit(img20,rect)
                            if 70<=x_s<=419 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                vibraqua=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                grincement=True
                                fenetre.blit(img20,rect)
                        if pok_act=="Tropius":                             
                            if 70<=x_s<=419 and 596<=y_s<=674:
                                Attaque=False
                                base_inter=True
                                ecrasement=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 596<=y_s<=674:                               
                                Attaque=False
                                base_inter=True
                                feuille_magik=True
                                fenetre.blit(img20,rect)
                            if 70<=x_s<=419 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                lance_soleil=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                croissance=True
                                fenetre.blit(img20,rect)
                        if pok_act=="Maganon":                             
                            if 70<=x_s<=419 and 596<=y_s<=674:
                                Attaque=False
                                base_inter=True
                                feinte=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 596<=y_s<=674:                               
                                Attaque=False
                                base_inter=True
                                poing_de_feu=True
                                fenetre.blit(img20,rect)
                            if 70<=x_s<=419 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                lance_flammes=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                gros_yeux=True
                                fenetre.blit(img20,rect)
                        if pok_act=="Leviator":                             
                            if 70<=x_s<=419 and 596<=y_s<=674:
                                Attaque=False
                                base_inter=True
                                etreinte=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 596<=y_s<=674:                               
                                Attaque=False
                                base_inter=True
                                hydro_queue=True
                                fenetre.blit(img20,rect)
                            if 70<=x_s<=419 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                surf=True
                                fenetre.blit(img20,rect)
                            if 420<=x_s<=795 and 675<=y_s<=754:
                                Attaque=False
                                base_inter=True
                                grimace=True
                                fenetre.blit(img20,rect)
                                
                    if Sac==True: # zones cliquables dans l'interface de combat Sac
                        if 945<=x_s<=1096 and 650<=y_s<=678:
                            Sac=False
                            base_inter=True
                            action_sac=None
                        if 539<=x_s<=1114 and 84<=y_s<=166 and nb_pot==1:
                            Sac="En cours"
                            Pokemon=True
                            action_sac="potion"

                        if 539<=x_s<=1114 and 167<=y_s<=236 and nb_spot==1:
                            Sac="En cours"
                            Pokemon=True
                            action_sac="super_potion"

                        if 539<=x_s<=1114 and 237<=y_s<=300 and nb_hpot==1:
                            Sac="En cours"
                            Pokemon=True
                            action_sac="hyper_potion"

                        if 539<=x_s<=1114 and 301<=y_s<=373 and nb_para==1:
                            Sac="En cours"
                            Pokemon=True
                            action_sac="anti_para"
                    if Sac=="En cours":
                        if u==0:
                            x_s=0
                            u=1
                        if action_sac=="potion":
                            if 6<=x_s<=571 and 8<=y_s<=180:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne1=True
                                nb_pot=0

                            if 580<=x_s<=1146 and 40<=y_s<=212:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne2=True
                                nb_pot=0

                            if 6<=x_s<=571 and 201<=y_s<=375:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne3=True
                                nb_pot=0
                        
                        if action_sac=="super_potion":
                            if 6<=x_s<=571 and 8<=y_s<=180:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne1=True
                                nb_spot=0
            
                            if 580<=x_s<=1146 and 40<=y_s<=212:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne2=True
                                nb_spot=0

                            if 6<=x_s<=571 and 201<=y_s<=375:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne3=True
                                nb_spot=0
                                
                        if action_sac=="hyper_potion":
                            if 6<=x_s<=571 and 8<=y_s<=180:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne1=True
                                nb_hpot=0           

                            if 580<=x_s<=1146 and 40<=y_s<=212:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne2=True
                                nb_hpot=0

                            if 6<=x_s<=571 and 201<=y_s<=375:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne3=True
                                nb_hpot=0
                            
                        if action_sac=="anti_para":
                            if 6<=x_s<=571 and 8<=y_s<=180:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne1=True
                                nb_para=0
            
                            if 580<=x_s<=1146 and 40<=y_s<=212:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne2=True
                                nb_para=0

                            if 6<=x_s<=571 and 201<=y_s<=375:
                                Pokemon=False
                                Sac=False
                                base_inter=True
                                soigne3=True
                                nb_para=0
                                

                    if Pokemon==True: # zones cliquables dans l'interface de combat Pokemon
                        if 904<=x_s<=1134 and 670<=y_s<=738:
                            base_inter=True
                            choix=False
                            Pokemon=False
                            impossible_pok=False
                        if not Sac=="En cours":
                            if choix==False and impossible_pok==False:
                                if 6<=x_s<=571 and 8<=y_s<=180:
                                    pok_choix=0
                                    choix="En cours"
                                if 580<=x_s<=1146 and 40<=y_s<=212:
                                    pok_choix=1
                                    choix="En cours"
                                if 6<=x_s<=571 and 201<=y_s<=375:
                                    pok_choix=2
                                    choix="En cours"
                                    
                            if choix=="En cours":
                                if 274<=x_s<=332 and 463<=y_s<=490:
                                    choix=True
                                if 784<=x_s<=860 and 463<=y_s<=490:
                                    choix=False
                                
                            
                            
                        if choix==True:
                            if pok_choix==0:
                                impossible_pok=False
                                Pokemon=False
                                base_inter=True
                                changement1=True
                                choix=False
                            if pok_choix==1:
                                impossible_pok=False
                                Pokemon=False
                                base_inter=True
                                changement2=True
                                choix=False
                            if pok_choix==2:
                                impossible_pok=False
                                Pokemon=False
                                base_inter=True
                                changement3=True
                                choix=False
                            
                            Pokemon=False
                            base_inter=True
                            
                            


                        
                    if impossible_pok==True:
                        if 246<=x_s<=891 and 261<=y_s<=515:
                            impossible_pok=False
                            
#--------- Fenetre Fin -----------#
                            
        elif nfenetre==6:
            x_s, y_s = pygame.mouse.get_pos()
            fenetre.fill(gris)
            if victoire==True:
                Aff_centre("Vous avez gagné !",50,blanc)
            else:
                Aff_centre("Vous avez perdue...",50,blanc)
            
            if 65<=x_s<=321 and 703<=y_s<=748: # coutour
                pygame.draw.rect(fenetre,blanc,(65,685,255,75))
                pygame.draw.rect(fenetre,gris,(40,695,285,55))
            if 765<=x_s<=1111 and 703<=y_s<=748:   
                pygame.draw.rect(fenetre,blanc,(765,685,350,75))
                pygame.draw.rect(fenetre,gris,(745,695,375,55))
                
            police = pygame.font.Font("police/Pixellari.ttf",50)
            texte = police.render("Statistiques",True,blanc)
            fenetre.blit(texte,(65,700))
            police = pygame.font.Font("police/Pixellari.ttf",50)
            texte = police.render("Menu principale",True,blanc)
            fenetre.blit(texte,(765,700))
                
            for event in pygame.event.get(): # on prend le premier événement de la pile
                if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                    continuer = False
                if event.type==MOUSEBUTTONDOWN:
                    if 65<=x_s<=321 and 703<=y_s<=748: # Stats
                        nfenetre=7
                    if 765<=x_s<=1111 and 703<=y_s<=748: # Menu principale
                        nfenetre=0
                        
#--------- Fenetre Statistique -----------#
                        
        if nfenetre==7:
            x_s, y_s = pygame.mouse.get_pos()
            fenetre.fill(gris)
            Aff_centre("En développement",50,blanc)
            if 32<=x_s<=174 and 702<=y_s<=739:
                contour_r(30,185,700,738)
            Retour()
            for event in pygame.event.get(): # on prend le premier événement de la pile
                if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                    continuer = False
                if event.type==MOUSEBUTTONDOWN: # Retour
                    if 32<=x_s<=174 and 702<=y_s<=739:
                        nfenetre=6
                    
            

                                    
            
                    
                            
                        
                        
                        
                            
                
                

finally:
    pygame.quit()