import pyxel as px
from random import randint

########################
#       NIVEAUX        #
########################

NIVEAUX = [((1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1),
      (1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,1,0,2,0,0,0,0,2,0,1,0,0,1),
      (1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1),
      (1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1),
      (1,0,1,0,0,0,0,0,0,0,0,0,2,1,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1),
      (1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1),
      (1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1),
      (1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
      ),((1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1),
      (1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1),
      (1,0,0,1,2,0,0,0,0,0,0,2,1,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,1,3,0,0,0,0,3,1,0,0,0,1),
      (1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1),
      (1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1),
      (1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1),
      (1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1),
      (1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)),
      ((1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1),
      (1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1),
      (1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,1,1,2,0,0,0,0,2,1,1,0,0,1),
      (1,0,0,0,1,1,3,0,0,3,1,1,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,1,0,3,0,0,1,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1),
      (1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),
      (1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1),
      (1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1),
      (1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1),
      (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
      (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)),(
    (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,3,1,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1),
    (1,0,1,1,1,1,0,0,0,0,0,0,3,1,0,1),
    (1,0,1,3,0,0,0,0,0,0,1,1,1,1,0,1),
    (1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,1,3,0,1,1,0,3,1,0,0,0,1),
    (1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1),
    (1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1),
    (1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)),
    ((1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,2,0,0,0,0,3,3,0,0,0,0,2,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1),
    (1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1),
    (1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,1),
    (1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1),
    (1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1),
    (1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),
    (1,0,0,2,0,0,1,0,0,1,0,0,2,0,0,1),
    (1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0),
    (1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0),
    (1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0),
    (1,0,1,0,0,0,0,3,0,3,0,0,0,1,0,0),
    (1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0),
    (1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1),
    (1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1),
    (1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),
    (1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))]

########################
#      CONSTANTES      #
########################
BLOC_ACCESSIBLE = 0
BLOC_COLLISION = 1
FANTOME = 2
SQUELETTE = 3

COULEUR_TRANSPARENCE = 5

TILEMAP_FOND = 0
TILEMAP_MURS = 1
TILEMAP_DECOR = 2
TILESET_PERSO = 0

U_FANTOME=152
V_FANTOME=65
U_PERSO = 122
V_PERSO = 12
U_ARCHER =120
V_ARCHER = 32
U_SQUELETTE = 141
V_SQUELETTE = 65

COS_PERSO_DEPART = (60,104)
########################
#        CLASS         #
########################
class App:

    def __init__(self, h, l, titre):

        px.init(h, l, title = titre) # Création de la fenêtre # créé une fenêtre de 128x192 tuiles ( fond noir par défaut )
        px.load("5.pyxres")
        
        self.avancement = [1,1]
        self.debut_niveau(self.avancement)
        self.perso= Personnage(COS_PERSO_DEPART, self.ennemis)
        self.run =True
        px.playm(0, loop = True)
        
        px.run(self.update, self.draw) # A PLACER A LA FIN DU CONSTRUCTEUR

    def update(self):
        '''Modification des variables gérant le déplacement des sprites, du décor'''
        if self.run:
            if self.ennemis == []:
                if self.avancement[1]<5:
                    self.avancement[1]+=1
                    self.debut_niveau(self.avancement)
                else :
                    self.avancement = [self.avancement[0]+1,1]
                    self.perso.hp = 100 + 20*self.avancement[0]-20
                    self.debut_niveau(self.avancement)
            elif self.perso.hp<=0:
                self.run = False
            else:
                self.perso.update(self.avancement,self.ennemis, self.collisions)
                ennemi_pop = []
                for ennemi in self.ennemis:
                    ennemi.update(self.perso, self.avancement,self.ennemis, self.collisions)
                    if ennemi.isdead:
                        ennemi_pop.append(ennemi)
                for ind_en in ennemi_pop:
                    self.ennemis.pop(self.ennemis.index(ind_en))
                        
	
    def draw(self):
        '''Dessin des éléments du jeu dans la fenêtre'''
        if self.run:
            px.cls(0) # efface la fenêtre ( ici avec la couleur noire, celle par défaut )
            px.text(2, 0, str(self.avancement), 1)
            px.bltm(0, 0, TILEMAP_FOND, (self.avancement[1]-1)*128, 0, 128, 192, COULEUR_TRANSPARENCE)
            px.bltm(0, 0, TILEMAP_MURS, (self.avancement[1]-1)*128, 0, 128, 192, COULEUR_TRANSPARENCE)
            px.bltm(0, 0, TILEMAP_DECOR, (self.avancement[1]-1)*128, 0, 128, 192, COULEUR_TRANSPARENCE)
            self.perso.draw()
            for ennemi in self.ennemis:
                ennemi.draw()
            px.text(10, 10, str(self.avancement[0]) + " : " + str(self.avancement[1]), 1)
            px.blt(115, 8, 0, 140, 11, 9, 9, COULEUR_TRANSPARENCE)
        else:
            px.cls(0)
            px.text(46, 85, "GAME OVER", 7)
            px.text(50, 10, str(self.avancement[0]) + " : " + str(self.avancement[1]), 7)

    def debut_niveau(self, niveau):
        self.collisions = []
        self.ennemis = []
        for i in range (16):
            for j in range (24):
                if NIVEAUX[niveau[1]-1][j][i] == BLOC_COLLISION :
                    self.collisions.append((j,i))
                elif NIVEAUX[niveau[1]-1][j][i] == FANTOME :
                    self.ennemis.append(Fantome(niveau, (j*8,i*8)))
                elif NIVEAUX[niveau[1]-1][j][i] == SQUELETTE :
                    self.ennemis.append(Squelette(niveau, (j*8,i*8)))

class Personnage:

    def __init__(self, cos, ennemis):
        self.cos = [cos[0],cos[1]]
        self.cible = self.ennemi_proche(ennemis)
        self.vx = 0
        self.vy = 0
        self.projectile = []
        self.tir_time = px.frame_count
        self.hp = 100
        self.speed = 1

    def get_joueur_coord(self):
        return self.cos

    def hurt(self,dgt):
        self.hp-=dgt
        px.play(1, 5)

    def update(self,niveau,ennemis,collisions):
        '''
        Modification des variables gérant le déplacement du sprite
        '''
        proj_pop = []
        for proj in self.projectile:
            proj.update(collisions)
            if proj.is_dead():
                proj_pop.append(proj)
        for ind_proj in proj_pop:
            self.projectile.pop(self.projectile.index(ind_proj))
    
        if self.cible.hp <= 0:
            self.cible = self.ennemi_proche(ennemis)
        
        self.vx = 0
        self.vy = 0
        if px.btn(px.KEY_UP):
            self.vy = -self.speed
        if px.btn(px.KEY_DOWN):
            self.vy = self.speed
        if px.btn(px.KEY_RIGHT):
            self.vx = self.speed
        if px.btn(px.KEY_LEFT):
            self.vx = -self.speed
        if self.vx == 0 and self.vy == 0:
            self.tir()
            self.vx = 0
            self.vy = 0
            self.cible = self.ennemi_proche(ennemis)
            
                
        self.cos = check_collision(6,8,self.cos[0],self.cos[1],self.vx,self.vy,niveau)
        
    def ennemi_proche(self,ennemis):
        cible = ennemis[0]
        min = 500
        for ennemi in ennemis:
            dis = px.sqrt((ennemi.coord[0]-self.cos[0])**2+(ennemi.coord[1]-self.cos[1])**2)
            if dis < min:
                min = dis
                cible = ennemi
        return cible

    def tir(self):
        if px.frame_count-self.tir_time >= 30:
            dis = px.sqrt((self.cible.coord[0]-self.cos[0])**2+(self.cible.coord[1]-self.cos[1])**2)
            self.projectile.append(Projectile(self.cos,5,(self.cible.coord[0]-self.cos[0])/dis,(self.cible.coord[1]-self.cos[1])/dis,15, self.cible))
            self.tir_time = px.frame_count

    def draw(self):
        '''Dessin du personnage'''
        px.blt(self.cos[0], self.cos[1], TILESET_PERSO, U_PERSO, V_PERSO, 6, 8, COULEUR_TRANSPARENCE)
        for proj in self.projectile:
            proj.draw()
        px.text(100, 10, str(self.hp), 8)


class Fantome:
    def __init__(self,niveau,coord):
        """
        niveau = niveau actuel <tab> [niveau,monde]
        coord = coordonées <tab> [x,y]
        """
        self.hp = 10
        self.degats = randint(25+12.5*(niveau[0]-1),33+16.5*(niveau[0]-1))
        self.speed = randint(1+0.5*(niveau[0]-1),2+(niveau[0]-1))*0.3
        self.coord = coord
        self.u = U_FANTOME
        self.v = V_FANTOME
        self.isdead = False

    def is_dead(self):
        return self.isdead


    def get_coord(self):
        return self.coord
        
    def attack(self, joueur):
        joueur.hurt(self.degats)
        self.isdead = True

    def hurt(self, degats):
        self.hp -= degats
        if self.hp <= 0:
            self.isdead = True

    def update(self, joueur, niveau, ennemis, collision):
        """
        Déplace le fantome
        """
        joueur_coord = joueur.get_joueur_coord()
        x_pro = self.coord[0] + px.sgn(joueur_coord[0] - self.coord[0]) * self.speed
        if px.sgn(joueur_coord[0] - self.coord[0]) != px.sgn(joueur_coord[0]-x_pro):
            x_pro = joueur_coord[0]
        y_pro = self.coord[1] + px.sgn(joueur_coord[1] - self.coord[1]) * self.speed
        if px.sgn(joueur_coord[1] - self.coord[1]) != px.sgn(joueur_coord[1]-y_pro):
            y_pro = joueur_coord[1]        
        self.coord = [x_pro,y_pro]
        if joueur_coord == self.coord:
            self.attack(joueur)

    def draw(self):
        """
        Affiche le fantome
        """
        px.blt(self.coord[0], self.coord[1], TILESET_PERSO, self.u, self.v, 4, 7, COULEUR_TRANSPARENCE)

class Projectile():
    def __init__(self, coord, speed,vx,vy,degats, cible):
        """
        coord = coordonées <tab> [x,y]
        speed <int>
        vx <int>
        vy <int>
        """
        self.coord = coord
        self.speed = speed
        self.vx = vx
        self.vy = vy
        self.isdead = False
        self.meur = False
        self.degats = degats
        self.cible = cible


    def is_dead(self):
        return self.isdead


    def get_coord(self):
        return self.coord
        
    def attack(self, joueur):
        joueur.hurt(self.degats)
        self.isdead = True

    def update(self,collisions):
        cos = self.cible.get_coord()
        x_pro = self.coord[0] + px.sgn(cos[0] - self.coord[0]) * self.speed
        if px.sgn(cos[0] - self.coord[0]) != px.sgn(cos[0]-x_pro):
            x_pro = cos[0]
        y_pro = self.coord[1] + px.sgn(cos[1] - self.coord[1]) * self.speed
        if px.sgn(cos[1] - self.coord[1]) != px.sgn(cos[1]-y_pro):
            y_pro = cos[1]        
        self.coord = [x_pro,y_pro]
        if cos == self.coord:
            self.attack(self.cible)


    def draw(self):
        """
        Affiche le projectile
        """
        px.blt(self.coord[0], self.coord[1], TILESET_PERSO, 105, 97, 5, 5, COULEUR_TRANSPARENCE)


class Squelette:
    def __init__(self,niveau, coord):
        """
        niveau = niveau actuel <tab> [niveau,monde]
        coord = coordonées <tab> [x,y]
        """
        self.hp = 60
        self.degats = randint(1+0.5*(niveau[0]-1),2+(niveau[0]-1))*0.5
        self.speed = randint(1+0.5*(niveau[0]-1),2+(niveau[0]-1))*0.3
        self.coord = coord
        self.u = U_SQUELETTE
        self.v = V_SQUELETTE
        self.isdead = False

    def is_dead(self):
        return self.isdead


    def get_coord(self):
        return self.coord
        
    def attack(self, joueur):
        joueur.hurt(self.degats)

    def hurt(self, degats):
        self.hp -= degats
        if self.hp <= 0:
            self.isdead = True

    def update(self, joueur, niveau, ennemis, collisions):
        """
        Déplace le fantome
        """
        joueur_coord = joueur.get_joueur_coord()
        vx = px.sgn(joueur_coord[0] - self.coord[0]) * self.speed
        x_pro = self.coord[0] + px.sgn(joueur_coord[0] - self.coord[0]) * self.speed
        if px.sgn(joueur_coord[0] - self.coord[0]) != px.sgn(joueur_coord[0]-x_pro):
            x_pro = joueur_coord[0]
        vy = px.sgn(joueur_coord[1] - self.coord[1]) * self.speed
        y_pro = self.coord[1] + px.sgn(joueur_coord[1] - self.coord[1]) * self.speed
        if px.sgn(joueur_coord[1] - self.coord[1]) != px.sgn(joueur_coord[1]-y_pro):
            y_pro = joueur_coord[1]        
        self.coord = check_collision(6,8,self.coord[0],self.coord[1],vx,vy,niveau)
        dis = px.sqrt((joueur_coord[0]-self.coord[0])**2+(joueur_coord[1]-self.coord[1])**2)
        if dis<=4:
            self.attack(joueur)

    def draw(self):
        """
        Affiche le fantome
        """
        px.blt(self.coord[0], self.coord[1], TILESET_PERSO, self.u, self.v, 6, 8, COULEUR_TRANSPARENCE)

def check_collision(w,h,x,y,vx,vy,niveau):
    x_pro = x+vx
    y_pro = y + vy
    if NIVEAUX[niveau[1]-1][round(y//8)][round(x_pro//8)] == 1 and vx < 0 :
        x_pro = ((x_pro//8)+1)*8
    elif NIVEAUX[niveau[1]-1][round((y)//8)][round((x_pro+w)//8)] == 1 and vx > 0 :
        x_pro = ((x_pro+w)//8)*8-1-w
    if NIVEAUX[niveau[1]-1][round(y_pro//8)][round(x//8)] == 1 and vy < 0 :
        y_pro = ((y_pro//8)+1)*8
    
    elif NIVEAUX[niveau[1]-1][round((y_pro+h)//8)][round(x//8)] == 1 and vy > 0 :
        y_pro = ((y_pro+h)//8)*8-1-h
    return [x_pro,y_pro]

########################
#  PROGRAMME PRINCIPAL #
########################
App(128, 192, "Dungeon Shuriken")