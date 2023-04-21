import pygame
def Aff_centre(text,taille,couleur):
    police = pygame.font.Font("police/Pixellari.ttf",taille) 
    texte = police.render(text,True,couleur)
    rectTexte = texte.get_rect()
    rectTexte.center = interfaceMMS.rectFenetre.center
    fenetre.blit(texte,rectTexte)
    
def Suivant():
    police = pygame.font.Font("police/Pixellari.ttf",50)
    texte = police.render("Suivant",True,blanc)
    fenetre.blit(texte,(965,700))
    
def Retour():
    police = pygame.font.Font("police/Pixellari.ttf",50)
    texte = police.render("Retour",True,blanc)
    fenetre.blit(texte,(30,700))
    
    
def posimg(l,h):
    center = l,h
    rect = image2.get_rect()
    rect.center = center
    
    
def contour_pe(x_s1,x_s2,y_s1,y_s2):
    x_s, y_s = pygame.mouse.get_pos()
    if x_s1<=x_s<=x_s2 and y_s1<=y_s<=y_s2:
        pygame.draw.rect(fenetre,blanc,(largeur//2-(x_s2-x_s1)//2,hauteur//2-(y_s2-y_s1)//2-34,x_s2-x_s1,y_s2-y_s1+60))
        pygame.draw.rect(fenetre,gris,(largeur//2-(x_s2-x_s1)//2,hauteur//2-(y_s2-y_s1)//2-21,x_s2-x_s1,y_s2-y_s1+34))
    else:
        fenetre.fill(gris)
            
def contour_q(x_s1,x_s2,y_s1,y_s2):
    x_s, y_s = pygame.mouse.get_pos()
    if x_s1<=x_s<=x_s2 and y_s1<=y_s<=y_s2:
        pygame.draw.rect(fenetre,blanc,(30,687,x_s2-x_s1,y_s2-y_s1+30))
        pygame.draw.rect(fenetre,gris,(30,694,x_s2-x_s1,y_s2-y_s1+15))
        
def contour_r(x_s1,x_s2,y_s1,y_s2):
    x_s, y_s = pygame.mouse.get_pos()
    if x_s1<=x_s<=x_s2 and y_s1<=y_s<=y_s2:
        pygame.draw.rect(fenetre,blanc,(30,687,x_s2-x_s1-10,y_s2-y_s1+30))
        pygame.draw.rect(fenetre,gris,(30,694,x_s2-x_s1-10,y_s2-y_s1+15))
    else:
        pygame.draw.rect(fenetre,gris,(30,687,x_s2-x_s1-10,y_s2-y_s1+30))

def contour_s(x_s1,x_s2,y_s1,y_s2):
    x_s, y_s = pygame.mouse.get_pos()
    if x_s1<=x_s<=x_s2 and y_s1<=y_s<=y_s2:
        pygame.draw.rect(fenetre,blanc,(965,687,x_s2-x_s1,y_s2-y_s1+30))
        pygame.draw.rect(fenetre,gris,(965,694,x_s2-x_s1,y_s2-y_s1+15))
    else:
        pygame.draw.rect(fenetre,gris,(965,687,x_s2-x_s1,y_s2-y_s1+30))
        
def resumequipe():
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
        text=''
        for i in range(len(texte)):
            text+=texte[i]
            police=pygame.font.Font("police/pokemon.ttf",taille)
            text_surface=police.render(text,True,couleur)
            fenetre.blit(text_surface,pos)
            pygame.display.update()
            pygame.time.wait(35)