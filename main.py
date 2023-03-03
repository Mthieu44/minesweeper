import sys
import pygame
import fonction as fc
import time

grille = fc.Grille(int(input("Grid size")))
d = int(input("Mine density (12 : beginner, 18 : intermediate, 24 : expert)"))
i = 1000
while i % grille.taille != 0:
    i += 1
size = [i, i]
centre = [i/2, i/2]
affi = False
print("--------------------")
print("Press h to play automatically")
print("Press i to show probabilities")
print("Press o to hide probabilities")
print("--------------------")
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Click to start")
case0_tmp = pygame.image.load("img/Case0.jpg")
case1_tmp = pygame.image.load("img/Case1.jpg")
case2_tmp = pygame.image.load("img/Case2.jpg")
case3_tmp = pygame.image.load("img/Case3.jpg")
case4_tmp = pygame.image.load("img/Case4.jpg")
case5_tmp = pygame.image.load("img/Case5.jpg")
case6_tmp = pygame.image.load("img/Case6.jpg")
case7_tmp = pygame.image.load("img/Case7.jpg")
case8_tmp = pygame.image.load("img/Case8.jpg")
casev_tmp = pygame.image.load("img/Case-1.jpg")
casem_tmp = pygame.image.load("img/CaseM.jpg")
cased_tmp = pygame.image.load("img/CaseD.jpg")
casel_tmp = pygame.image.load("img/CaseL.jpg")
casew_tmp = pygame.image.load("img/CaseW.jpg")

while 1:
    case0 = pygame.transform.scale(case0_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    case1 = pygame.transform.scale(case1_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    case2 = pygame.transform.scale(case2_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    case3 = pygame.transform.scale(case3_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    case4 = pygame.transform.scale(case4_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    case5 = pygame.transform.scale(case5_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    case6 = pygame.transform.scale(case6_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    case7 = pygame.transform.scale(case7_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    case8 = pygame.transform.scale(case8_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    casev = pygame.transform.scale(casev_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    casem = pygame.transform.scale(casem_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    cased = pygame.transform.scale(cased_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    casel = pygame.transform.scale(casel_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    casew = pygame.transform.scale(casew_tmp, (size[0] / grille.taille, size[0] / grille.taille))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                grille.proba = [[1 for j in range(grille.taille)] for i in range(grille.taille)]
                grille.solveur_proba()
                affi = True
            if event.key == pygame.K_h:
                grille.proba = [[1 for j in range(grille.taille)] for i in range(grille.taille)]
                grille.solveur_auto()
                affi = False
            if event.key == pygame.K_o:
                affi = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = coord = pygame.mouse.get_pos()
            x, y = x // (size[0] // grille.taille), y // (size[1] // grille.taille)
            if not grille.tab:
                if event.button == 1:
                    nbrMines = grille.creation(x, y, d)
                    grille.clicgauche(x, y)
                    pygame.display.set_caption((str(nbrMines) + " mines left"))
                    temps = time.time()

            else:
                if event.button == 1:
                    grille.clicgauche(x, y)
                elif event.button == 3:
                    nbrMines = grille.clicdroit(x, y, nbrMines)
                elif event.button == 2:
                    grille.clicmolette(x, y)

    for l in range(grille.taille):
        for c in range(grille.taille):
            pos = (c*size[0]/grille.taille, l*size[0]/grille.taille)
            if grille.retourne[l][c] == 0:
                screen.blit(case0, pos)
            elif grille.retourne[l][c] == 2:
                screen.blit(cased, pos)
            else:
                if grille.tab[l][c] == 0:
                    screen.blit(casev, pos)
                if grille.tab[l][c] == 1:
                    screen.blit(case1, pos)
                if grille.tab[l][c] == 2:
                    screen.blit(case2, pos)
                if grille.tab[l][c] == 3:
                    screen.blit(case3, pos)
                if grille.tab[l][c] == 4:
                    screen.blit(case4, pos)
                if grille.tab[l][c] == 5:
                    screen.blit(case5, pos)
                if grille.tab[l][c] == 6:
                    screen.blit(case6, pos)
                if grille.tab[l][c] == 7:
                    screen.blit(case7, pos)
                if grille.tab[l][c] == 8:
                    screen.blit(case8, pos)

                if grille.tab[l][c] == -1:
                    while 1:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                        for r in range(grille.taille):
                            for s in range(grille.taille):
                                if grille.tab[r][s] == -1:
                                    screen.blit(casem, (s * size[0]/grille.taille, r * size[0]/grille.taille))
                                screen.blit(casel, pos)
                        pygame.display.flip()
    if affi:
        for i in range(grille.taille):
            for j in range(grille.taille):
                if grille.proba[i][j] != 1:
                    r = pygame.Surface((size[0] / grille.taille, size[0] / grille.taille))
                    r.set_alpha(150)
                    if grille.proba[i][j] is None:
                        r.fill((0, 0, 255))
                    elif grille.proba[i][j] == 0:
                        r.fill((20, 20, 20))
                    else:
                        r.fill((255, grille.proba[i][j]*255, 0))
                    screen.blit(r, (j * size[0]/grille.taille, i * size[0]/grille.taille))

    if grille.safe:
        win = True
        for y, x in grille.safe:
            if grille.retourne[y][x] == 1:
                continue
            else:
                win = False
        if win:
            print("You finished in", time.time()-temps, "seconds.")
            print("Restart the program to play again.")
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                for i in range(grille.taille):
                    for j in range(grille.taille):
                        if grille.tab[i][j] == -1:
                            screen.blit(casew, (j * size[0]/grille.taille, i * size[0]/grille.taille))
                pygame.display.flip()

    if grille.tab:
        pygame.display.set_caption(("Il reste " + str(nbrMines) + " mines à placer"))

    pygame.display.flip()
