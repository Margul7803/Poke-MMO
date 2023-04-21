import pygame, sys
pygame.init()

GREY = (150, 150, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Arial", 16)


def lire_dans_le_fichier_et_trouver_highscore(nom_fichier):
    file = open(nom_fichier, 'r')
    lines=file.readlines()
    file.close
       
    premier_score = 0
    
    for line in lines:
        name, score = line.strip().split(",")
        score = int(score)

        if score > premier_score:
            premier_score = score
            premier_nom = name

    return premier_nom, premier_score


def ecrire_dans_le_fichier(nom_fichier, ton_nom, points):
    score_file = open(nom_fichier, 'a')
    print (ton_nom+",", points, file=score_file)
    score_file.close()
    

def top10(screen, nom_fichier):
    bx = 480  # x-taille de la boite
    by = 400  # y-taille de la boite
    
    file = open(nom_fichier, 'r')
    lines=file.readlines()
       
    all_score = []
    for line in lines:
        sep = line.index(',')
        name = line[:sep]
        score = int(line[sep+1:-1])
        all_score.append((score, name))
    file.close
    all_score.sort(reverse=True)  # range du plus grand au plus petit
    best = all_score[:10]  # top 10 des scores

    # ça fait la boite de présentation
    box = pygame.surface.Surface((bx, by)) 
    box.fill(GREY)
    pygame.draw.rect(box, WHITE, (50, 12, bx-100, 35), 0)
    pygame.draw.rect(box, WHITE, (50, by-60, bx-100, 42), 0)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = font.render("Meilleur score", True, BLACK)  # Le titre
    txt_rect = txt_surf.get_rect(center=(bx//2, 30))
    box.blit(txt_surf, txt_rect)
    txt_surf = font.render("Pressez Entrer pour continuer.", True, BLACK)  # le bas
    txt_rect = txt_surf.get_rect(center=(bx//2, 360))
    box.blit(txt_surf, txt_rect)

    # ça écrit les données du top 10 dans la boite
    for i, entry in enumerate(best):
        txt_surf = font.render(entry[1] + "  " + str(entry[0]), True, BLACK)
        txt_rect = txt_surf.get_rect(center=(bx//2, 30*i+60))
        box.blit(txt_surf, txt_rect)
    
    screen.blit(box, (0, 0))
    pygame.display.flip()
    
    while True:  # attends que l'utilisateur accepte
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                return
        pygame.time.wait(20)
    

def enterbox(screen, txt):

    def blink(screen):
        for color in [GREY, WHITE]:
            pygame.draw.circle(box, color, (bx//2, int(by*0.7)), 7, 0)
            screen.blit(box, (0, by//2))
            pygame.display.flip()
            pygame.time.wait(300)

    def show_name(screen, name):
        pygame.draw.rect(box, WHITE, (50, 60, bx-100, 20), 0)
        txt_surf = font.render(name, True, BLACK)
        txt_rect = txt_surf.get_rect(center=(bx//2, int(by*0.7)))
        box.blit(txt_surf, txt_rect)
        screen.blit(box, (0, by//2))
        pygame.display.flip()
        
    bx = 480
    by = 100

    # fait une boite
    box = pygame.surface.Surface((bx, by))
    box.fill(GREY)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = font.render(txt, True, BLACK)
    txt_rect = txt_surf.get_rect(center=(bx//2, int(by*0.3)))
    box.blit(txt_surf, txt_rect)

    name = ""
    show_name(screen, name)

    # la loop du input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                inkey = event.key
                if inkey in [13, 271]:  # touche  entrer et retour 
                    return name
                elif inkey == 8:  # pour la touche arrière
                    name = name[:-1]
                elif inkey <= 300:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT and 122 >= inkey >= 97:
                        inkey -= 32  # pour les CAPITALES
                    name += chr(inkey)

        if name == "":
            blink(screen)
        show_name(screen, name)


def highscore(screen, nom_fichier, tes_points):
    premier_nom, premier_score = lire_dans_le_fichier_et_trouver_highscore(nom_fichier)

    if tes_points > premier_score:
        ton_nom = enterbox(screen, "TU AS LE MEILLEUR SCORE !!- Quel est ton nom ?")
    
    elif tes_points == premier_score:
        ton_nom = enterbox(screen, "Tu as le même score que le premier ! - Quel est ton nom?")
    
    elif tes_points < premier_score:
        st1 = "Le meilleur score est de "
        st2 = " de "
        st3 = "   Quel est ton nom?"
        txt = st1+str(premier_score)+st2+premier_nom+st3
        ton_nom = enterbox(screen, txt)

    if ton_nom == None or len(ton_nom) == 0:
        return  # il ne faut pas sauvegarder le fichier sans qu'un nom ne soit écrit

    ecrire_dans_le_fichier(nom_fichier, ton_nom, tes_points)
    top10(screen, nom_fichier)
    return