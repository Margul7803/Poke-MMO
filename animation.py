import pygame
class Tiplouf_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tiploufanimation = False
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/Tiplouf-0.png"), (145, 205)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/Tiplouf-1.png"), (145, 205)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/Tiplouf-2.png"), (145, 205)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/Tiplouf-3.png"), (145, 205)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/Tiplouf-4.png"), (145, 205)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/Tiplouf-5.png"), (145, 205)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/Tiplouf-6.png"), (145, 205)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/Tiplouf-7.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-0.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-1.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-2.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-3.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-4.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-5.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-6.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-7.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-8.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-9.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-10.png"), (145, 205)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Derrière/_Tiplouf-11.png"), (145, 205)))

            
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tiploufanimation = True

    def update(self,speed):
        if self.Tiploufanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tiploufanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tiplouf = pygame.sprite.Group()
tiplouf_anim = Tiplouf_anim(175,365)
moving_sprites_tiplouf.add(tiplouf_anim)

class Ouisticram_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Ouisticramanimation = False
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-0.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-1.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-2.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-3.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-4.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-5.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-6.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-7.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-8.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-9.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-10.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-11.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-12.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-13.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-14.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-15.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/Ouisticram-16.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-1.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-2.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-3.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-4.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-5.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-6.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-7.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-8.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-9.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-10.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-11.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-12.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-13.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-14.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-15.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-16.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-17.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-18.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-19.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-20.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-21.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-22.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-23.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-24.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-25.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-26.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-27.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-28.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-29.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-30.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-31.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-32.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-33.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-34.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-35.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-36.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Derrière/_Ouisticram-37.png"), (180, 216)))
            
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Ouisticramanimation = True

    def update(self,speed):
        if self.Ouisticramanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Ouisticramanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_ouisticram = pygame.sprite.Group()
ouisticram_anim = Ouisticram_anim(180,355)
moving_sprites_ouisticram.add(ouisticram_anim)



#-----------------------------------------------------------------------------------------

class Tortipousse_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tortipousseanimation = False
        self.sprites = []
        for i in range(2):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-0.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-1.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-2.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-3.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-4.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-5.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-6.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-7.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-8.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-9.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-10.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-11.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-12.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-13.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-14.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-15.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-16.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-17.png"), (158, 202)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/Tortipousse-18.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-0.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-1.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-2.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-3.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-4.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-5.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-6.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-7.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-8.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-9.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-10.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-11.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-12.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-13.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-14.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-15.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-16.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-17.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-18.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-19.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-20.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-21.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-22.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-23.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-24.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-25.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-26.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-27.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-28.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-29.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-30.png"), (158, 202)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Derrière/_Tortipousse-31.png"), (158, 202)))


        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tortipousseanimation = True

    def update(self,speed):
        if self.Tortipousseanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tortipousseanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tortipousse = pygame.sprite.Group()
tortipousse_anim = Tortipousse_anim(175,365)
moving_sprites_tortipousse.add(tortipousse_anim)

#-----------------------------------------------------------------------------

class Galopa_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Galopaanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-0.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-1.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-2.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-3.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-4.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-5.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-6.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-7.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-8.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-9.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-10.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-11.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-12.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-13.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-14.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-15.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-16.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-17.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-18.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-19.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-20.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-21.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-22.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-23.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-24.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-25.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-26.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-27.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-28.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-29.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-30.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-31.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-32.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-33.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-34.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-35.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-36.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-37.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-38.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-39.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-40.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-41.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-42.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-43.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-44.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-45.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-46.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Derrière/Galopa-47.png"), (350 ,350)))
        
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Galopaanimation = True

    def update(self,speed):
        if self.Galopaanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Galopaanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_galopa = pygame.sprite.Group()
galopa_anim = Galopa_anim(60,218)
moving_sprites_galopa.add(galopa_anim)



#-----------------------------------------------------------------------------------------
class Bouldeneu_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Bouldeneuanimation = False
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/Bouldeneu-1.png"), (490, 335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/Bouldeneu-2.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/Bouldeneu-3.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/Bouldeneu-4.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/Bouldeneu-5.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/Bouldeneu-6.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/Bouldeneu-7.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/Bouldeneu-8.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-1.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-2.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-3.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-4.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-5.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-6.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-7.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-8.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-9.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-10.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-11.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-12.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-13.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-14.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-15.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-16.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-17.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-18.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-19.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-20.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-21.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-22.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-23.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-24.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-25.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-26.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-27.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-28.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-29.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-30.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-31.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Derrière/_Bouldeneu-32.png"), (490,  335)))

        
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Bouldeneuanimation = True

    def update(self,speed):
        if self.Bouldeneuanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Bouldeneuanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_bouldeneu = pygame.sprite.Group()
bouldeneu_anim = Bouldeneu_anim(25,235)
moving_sprites_bouldeneu.add(bouldeneu_anim)

#-----------------------------------------------------------------------------
class Tentacruel_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tentacruelanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-0.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-1.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-2.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-3.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-4.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-5.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-6.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-7.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-8.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-9.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-10.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-11.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-12.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-13.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-14.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-15.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-16.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-17.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-18.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-19.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-20.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-21.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-22.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-23.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-24.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-25.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-26.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-27.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-28.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-29.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-30.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-31.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-32.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-33.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-34.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-35.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-36.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-37.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-38.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-39.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-40.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-41.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-42.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-43.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-44.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-45.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-46.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-47.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-48.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-49.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-50.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-51.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-52.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-53.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-54.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-55.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-56.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-57.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-58.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-59.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-60.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-61.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-62.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-63.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-64.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-65.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-66.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-67.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-68.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-69.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-70.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-71.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-72.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-73.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-74.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-75.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-76.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-77.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-78.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Derrière/Tentacruel-79.png"), (350, 350)))
        

        
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tentacruelanimation = True

    def update(self,speed):
        if self.Tentacruelanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tentacruelanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tentacruel = pygame.sprite.Group()
tentacruel_anim = Tentacruel_anim(70,220)
moving_sprites_tentacruel.add(tentacruel_anim)

#-----------------------------------------------------------------------------
class Leviator_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Leviatoranimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-0.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-1.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-2.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-3.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-4.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-5.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-6.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-7.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-8.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-9.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-10.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Derrière/Leviator-11.png"), (464, 350)))
        
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Leviatoranimation = True

    def update(self,speed):
        if self.Leviatoranimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Leviatoranimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_leviator = pygame.sprite.Group()
leviator_anim = Leviator_anim(50,220)
moving_sprites_leviator.add(leviator_anim)

#-----------------------------------------------------------------------------
class Maganon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Maganonanimation = False
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-0.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-1.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-2.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-3.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-4.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-5.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-6.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-7.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-8.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-9.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-10.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-11.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-12.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-13.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-14.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-15.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-16.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-17.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-18.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-19.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-20.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-21.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-22.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-23.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/Maganon-24.png"), (409, 350)))

        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-0.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-1.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-2.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-3.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-4.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-5.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-6.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-7.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-8.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-9.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-10.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-11.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-12.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-13.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-14.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-15.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-16.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-17.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-18.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-19.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-20.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-21.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-22.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-23.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-24.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-25.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-26.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-27.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-28.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-29.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-30.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-31.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-32.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-33.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-34.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-35.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-36.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-37.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-38.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Derrière/_Maganon-39.png"), (409, 350)))

        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Maganonanimation = True

    def update(self,speed):
        if self.Maganonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Maganonanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_maganon = pygame.sprite.Group()
maganon_anim = Maganon_anim(80,220)
moving_sprites_maganon.add(maganon_anim)

#-----------------------------------------------------------------------------
class Tropius_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tropiusanimation = False
        self.sprites = []
        for i in range(2):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-0.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-1.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-2.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-3.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-4.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-5.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-6.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-7.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-8.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-9.png"), (350, 350)))      
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-10.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-11.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-12.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-13.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-14.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-15.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/tropius-16.png"), (350, 350)))

        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-0.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-1.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-2.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-3.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-4.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-5.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-6.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-7.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-8.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-9.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-10.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-11.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-12.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-13.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-14.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Derrière/_tropius-15.png"), (350, 350)))
                   
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tropiusanimation = True

    def update(self,speed):
        if self.Tropiusanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tropiusanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tropius = pygame.sprite.Group()
tropius_anim = Tropius_anim(90,220)
moving_sprites_tropius.add(tropius_anim)

#-----------------------------------------------------------------------------
class Tiplouf2_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tiplouf2animation = False
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/Tiplouf-0.png"), (120, 164)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/Tiplouf-1.png"), (120, 164)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/Tiplouf-2.png"), (120, 164)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/Tiplouf-3.png"), (120, 164)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/Tiplouf-4.png"), (120, 164)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/Tiplouf-5.png"), (120, 164)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/Tiplouf-6.png"), (120, 164)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/Tiplouf-7.png"), (120, 164)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/_Tiplouf-0.png"), (120, 164)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/_Tiplouf-1.png"), (120, 164)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/_Tiplouf-2.png"), (120, 164)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/_Tiplouf-3.png"), (120, 164)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/_Tiplouf-4.png"), (120, 164)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/_Tiplouf-5.png"), (120, 164)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/_Tiplouf-6.png"), (120, 164)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/_Tiplouf-7.png"), (120, 164)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tiplouf/Devant/_Tiplouf-8.png"), (120, 164)))


        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tiplouf2animation = True

    def update(self,speed):
        if self.Tiplouf2animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tiplouf2animation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tiplouf2 = pygame.sprite.Group()
tiplouf2_anim = Tiplouf2_anim(800,200)
moving_sprites_tiplouf2.add(tiplouf2_anim)

#-----------------------------------------------------------------------

class Ouisticram2_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Ouisticram2animation = False
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-0.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-1.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-2.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-3.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-4.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-5.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-6.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-7.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-8.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-9.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-10.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-11.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-12.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-13.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-14.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-15.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-16.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-17.png"), (180, 216)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/Ouisticram-18.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-1.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-2.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-3.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-4.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-5.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-6.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-7.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-8.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-9.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-10.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-11.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-12.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-13.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-14.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-15.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-16.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-18.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-19.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-20.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-21.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-22.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-23.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-25.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-26.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-27.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-28.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-29.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-30.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-31.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-32.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-33.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-34.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-35.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-36.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-37.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-38.png"), (180, 216)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Ouisticram/Devant/_Ouisticram-39.png"), (180, 216)))
        
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Ouisticram2animation = True

    def update(self,speed):
        if self.Ouisticram2animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Ouisticram2animation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_ouisticram2 = pygame.sprite.Group()
ouisticram2_anim = Ouisticram2_anim(780,150)
moving_sprites_ouisticram2.add(ouisticram2_anim)



#-----------------------------------------------------------------------------------------

class Tortipousse2_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tortipousse2animation = False
        self.sprites = []
        for i in range(2):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-0.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-1.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-2.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-3.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-4.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-5.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-6.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-7.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-8.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-9.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-10.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-11.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-12.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-13.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-14.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-15.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-16.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-17.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-18.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-20.png"), (124, 168)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/Tortipousse-20.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-0.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-1.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-2.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-3.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-4.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-5.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-6.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-7.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-8.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-9.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-10.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-11.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-12.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-13.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-14.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-15.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-16.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-18.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-19.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-20.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-21.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-22.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-23.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-24.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-25.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-26.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-27.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-28.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-29.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-30.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-31.png"), (124, 168)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tortipousse/Devant/_Tortipousse-32.png"), (124, 168)))
            
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tortipousse2animation = True

    def update(self,speed):
        if self.Tortipousse2animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tortipousse2animation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tortipousse2 = pygame.sprite.Group()
tortipousse2_anim = Tortipousse2_anim(790,200)
moving_sprites_tortipousse2.add(tortipousse2_anim)

#-----------------------------------------------------------------------------

class Galopa2_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Galopa2animation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-0.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-1.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-2.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-3.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-4.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-5.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-6.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-7.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-8.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-9.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-10.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-11.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-12.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-13.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-14.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-15.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-16.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-17.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-18.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-19.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-20.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-21.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-22.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-23.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-24.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-25.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-26.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-27.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-28.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-29.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-30.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-31.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-32.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-33.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-34.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-35.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-36.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-37.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-38.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-39.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-40.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-41.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-42.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-43.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-44.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-45.png"), (350 ,350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Galopa/Devant/Galopa-46.png"), (350 ,350)))        
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Galopa2animation = True

    def update(self,speed):
        if self.Galopa2animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Galopa2animation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_galopa2 = pygame.sprite.Group()
galopa2_anim = Galopa2_anim(700,20)
moving_sprites_galopa2.add(galopa2_anim)



#-----------------------------------------------------------------------------------------
class Bouldeneu2_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Bouldeneu2animation = False
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/Bouldeneu-0.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/Bouldeneu-1.png"), (490, 335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/Bouldeneu-2.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/Bouldeneu-3.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/Bouldeneu-4.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/Bouldeneu-5.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/Bouldeneu-6.png"), (490,  335)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/Bouldeneu-7.png"), (490,  335)))

        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-0.png"), (490,  335)))            
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-1.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-2.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-3.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-4.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-5.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-6.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-7.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-8.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-9.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-10.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-11.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-12.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-13.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-14.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-15.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-16.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-17.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-18.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-19.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-20.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-21.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-22.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-23.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-24.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-25.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-26.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-27.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-28.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-29.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-30.png"), (490,  335)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Bouldeneu/Devant/_Bouldeneu-31.png"), (490,  335)))

        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Bouldeneu2animation = True

    def update(self,speed):
        if self.Bouldeneu2animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Bouldeneu2animation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_bouldeneu2 = pygame.sprite.Group()
bouldeneu2_anim = Bouldeneu2_anim(650,50)
moving_sprites_bouldeneu2.add(bouldeneu2_anim)

#-----------------------------------------------------------------------------
class Tentacruel2_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tentacruel2animation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-0.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-1.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-2.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-3.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-4.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-5.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-6.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-7.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-8.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-9.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-10.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-11.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-12.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-13.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-14.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-15.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-16.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-17.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-18.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-19.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-20.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-21.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-22.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-23.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-24.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-25.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-26.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-27.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-28.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-29.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-30.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-31.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-32.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-33.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-34.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-35.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-36.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-37.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-38.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-39.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-40.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-41.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-42.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-43.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-44.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-45.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-46.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-47.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-48.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-49.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-50.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-51.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-52.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-53.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-54.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-55.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-56.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-57.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-58.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-59.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-60.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-61.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-62.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-63.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-64.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-65.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-66.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-67.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-68.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-69.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-70.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-71.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-72.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-73.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-74.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-75.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-76.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-77.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-78.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tentacruel/Devant/Tentacruel-79.png"), (350, 350)))
        
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tentacruel2animation = True

    def update(self,speed):
        if self.Tentacruel2animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tentacruel2animation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tentacruel2 = pygame.sprite.Group()
tentacruel2_anim = Tentacruel2_anim(650,25)
moving_sprites_tentacruel2.add(tentacruel2_anim)

#-----------------------------------------------------------------------------
class Leviator2_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Leviator2animation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-0.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-1.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-2.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-3.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-4.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-5.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-6.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-7.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-8.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-9.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-10.png"), (464, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Leviator/Devant/Leviator-11.png"), (464, 350)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Leviator2animation = True

    def update(self,speed):
        if self.Leviator2animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Leviator2animation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_leviator2 = pygame.sprite.Group()
leviator2_anim = Leviator2_anim(650,30)
moving_sprites_leviator2.add(leviator2_anim)

#-----------------------------------------------------------------------------
class Maganon2_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Maganon2animation = False
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-0.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-1.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-2.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-3.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-4.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-5.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-6.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-7.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-8.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-9.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-10.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-11.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-12.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-13.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-14.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-15.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-16.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-17.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-18.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-19.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-20.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-21.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-22.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-23.png"), (409, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/Maganon-24.png"), (409, 350)))

        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-0.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-1.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-2.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-3.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-4.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-5.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-6.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-7.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-8.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-9.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-10.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-11.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-12.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-13.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-14.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-15.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-16.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-17.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-18.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-19.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-20.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-21.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-22.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-23.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-24.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-25.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-26.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-27.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-28.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-29.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-30.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-31.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-32.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-33.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-34.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-35.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-36.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-37.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-38.png"), (409, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Maganon/Devant/_Maganon-39.png"), (409, 350)))        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Maganon2animation = True

    def update(self,speed):
        if self.Maganon2animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Maganon2animation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_maganon2 = pygame.sprite.Group()
maganon2_anim = Maganon2_anim(700,20)
moving_sprites_maganon2.add(maganon2_anim)

#-----------------------------------------------------------------------------
class Tropius2_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tropius2animation = False
        self.sprites = []
        for i in range(2):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-0.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-1.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-2.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-3.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-4.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-5.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-6.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-7.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-8.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-9.png"), (350, 350)))      
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-10.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-11.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-12.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-13.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-14.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-15.png"), (350, 350)))
            self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/tropius-16.png"), (350, 350)))


        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-0.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-1.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-2.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-3.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-4.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-5.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-6.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-7.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-8.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-9.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-10.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-11.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-12.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-13.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-14.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-15.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-16.png"), (350, 350)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Combat/Tropius/Devant/_tropius-17.png"), (350, 350)))
                            
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tropius2animation = True

    def update(self,speed):
        if self.Tropius2animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tropius2animation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tropius2 = pygame.sprite.Group()
tropius2_anim = Tropius2_anim(710,20)
moving_sprites_tropius2.add(tropius2_anim)



class Leviator_pokemon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Leviator_pokemonanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Leviator1.png"), (108, 90)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Leviator2.png"), (108, 90)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Leviator_pokemonanimation = True

    def update(self,speed):
        if self.Leviator_pokemonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Leviator_pokemonanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_leviator1_pokemon = pygame.sprite.Group()
moving_sprites_leviator2_pokemon = pygame.sprite.Group()
moving_sprites_leviator3_pokemon = pygame.sprite.Group()
leviator1_pokemon_anim = Leviator_pokemon_anim(50,22)
leviator2_pokemon_anim = Leviator_pokemon_anim(625,54)
leviator3_pokemon_anim = Leviator_pokemon_anim(50,215)
moving_sprites_leviator1_pokemon.add(leviator1_pokemon_anim)
moving_sprites_leviator2_pokemon.add(leviator2_pokemon_anim)
moving_sprites_leviator3_pokemon.add(leviator3_pokemon_anim)

class Tropius_pokemon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tropius_pokemonanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Tropius1.png"), (125, 90)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Tropius2.png"), (125, 90)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tropius_pokemonanimation = True

    def update(self,speed):
        if self.Tropius_pokemonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tropius_pokemonanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tropius1_pokemon = pygame.sprite.Group()
moving_sprites_tropius2_pokemon = pygame.sprite.Group()
moving_sprites_tropius3_pokemon = pygame.sprite.Group()
tropius1_pokemon_anim = Tropius_pokemon_anim(50,26)
tropius2_pokemon_anim = Tropius_pokemon_anim(625,54)
tropius3_pokemon_anim = Tropius_pokemon_anim(50,215)
moving_sprites_tropius1_pokemon.add(tropius1_pokemon_anim)
moving_sprites_tropius2_pokemon.add(tropius2_pokemon_anim)
moving_sprites_tropius3_pokemon.add(tropius3_pokemon_anim)

class Maganon_pokemon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Maganon_pokemonanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Maganon1.png"), (115, 90)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Maganon2.png"), (115, 90)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Maganon_pokemonanimation = True

    def update(self,speed):
        if self.Maganon_pokemonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Maganon_pokemonanimation = False

        self.image = self.sprites[int(self.current_sprite)]

moving_sprites_maganon1_pokemon = pygame.sprite.Group()
moving_sprites_maganon2_pokemon = pygame.sprite.Group()
moving_sprites_maganon3_pokemon = pygame.sprite.Group()
maganon1_pokemon_anim = Maganon_pokemon_anim(50,26)
maganon2_pokemon_anim = Maganon_pokemon_anim(625,54)
maganon3_pokemon_anim = Maganon_pokemon_anim(50,215)
moving_sprites_maganon1_pokemon.add(maganon1_pokemon_anim)
moving_sprites_maganon2_pokemon.add(maganon2_pokemon_anim)
moving_sprites_maganon3_pokemon.add(maganon3_pokemon_anim)

class Tentacruel_pokemon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tentacruel_pokemonanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Tentacruel1.png"), (90, 90)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Tentacruel2.png"), (90, 90)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tentacruel_pokemonanimation = True

    def update(self,speed):
        if self.Tentacruel_pokemonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tentacruel_pokemonanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tentacruel1_pokemon = pygame.sprite.Group()
moving_sprites_tentacruel2_pokemon = pygame.sprite.Group()
moving_sprites_tentacruel3_pokemon = pygame.sprite.Group()
tentacruel1_pokemon_anim = Tentacruel_pokemon_anim(50,22)
tentacruel2_pokemon_anim = Tentacruel_pokemon_anim(625,54)
tentacruel3_pokemon_anim = Tentacruel_pokemon_anim(50,215)
moving_sprites_tentacruel1_pokemon.add(tentacruel1_pokemon_anim)
moving_sprites_tentacruel2_pokemon.add(tentacruel2_pokemon_anim)
moving_sprites_tentacruel3_pokemon.add(tentacruel3_pokemon_anim)

class Bouldeneu_pokemon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Bouldeneu_pokemonanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Bouldeneu1.png"), (115, 90)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Bouldeneu2.png"), (115, 90)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Bouldeneu_pokemonanimation = True

    def update(self,speed):
        if self.Bouldeneu_pokemonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Bouldeneu_pokemonanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_bouldeneu1_pokemon = pygame.sprite.Group()
moving_sprites_bouldeneu2_pokemon = pygame.sprite.Group()
moving_sprites_bouldeneu3_pokemon = pygame.sprite.Group()
bouldeneu1_pokemon_anim = Bouldeneu_pokemon_anim(50,26)
bouldeneu2_pokemon_anim = Bouldeneu_pokemon_anim(625,54)
bouldeneu3_pokemon_anim = Bouldeneu_pokemon_anim(50,215)
moving_sprites_bouldeneu1_pokemon.add(bouldeneu1_pokemon_anim)
moving_sprites_bouldeneu2_pokemon.add(bouldeneu2_pokemon_anim)
moving_sprites_bouldeneu3_pokemon.add(bouldeneu3_pokemon_anim)

class Galopa_pokemon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Galopa_pokemonanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Galopa1.png"), (115, 90)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Galopa2.png"), (115, 90)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Galopa_pokemonanimation = True

    def update(self,speed):
        if self.Galopa_pokemonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Galopa_pokemonanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_galopa1_pokemon = pygame.sprite.Group()
moving_sprites_galopa2_pokemon = pygame.sprite.Group()
moving_sprites_galopa3_pokemon = pygame.sprite.Group()
galopa1_pokemon_anim = Galopa_pokemon_anim(50,22)
galopa2_pokemon_anim = Galopa_pokemon_anim(625,54)
galopa3_pokemon_anim = Galopa_pokemon_anim(50,215)
moving_sprites_galopa1_pokemon.add(galopa1_pokemon_anim)
moving_sprites_galopa2_pokemon.add(galopa2_pokemon_anim)
moving_sprites_galopa3_pokemon.add(galopa3_pokemon_anim)

class Ouisticram_pokemon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Ouisticram_pokemonanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Ouisticram1.png"), (70, 70)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Ouisticram2.png"), (70, 70)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Ouisticram_pokemonanimation = True

    def update(self,speed):
        if self.Ouisticram_pokemonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Ouisticram_pokemonanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_ouisticram1_pokemon = pygame.sprite.Group()
moving_sprites_ouisticram2_pokemon = pygame.sprite.Group()
moving_sprites_ouisticram3_pokemon = pygame.sprite.Group()
ouisticram1_pokemon_anim = Ouisticram_pokemon_anim(50,40)
ouisticram2_pokemon_anim = Ouisticram_pokemon_anim(635,65)
ouisticram3_pokemon_anim = Ouisticram_pokemon_anim(50,232)
moving_sprites_ouisticram1_pokemon.add(ouisticram1_pokemon_anim)
moving_sprites_ouisticram2_pokemon.add(ouisticram2_pokemon_anim)
moving_sprites_ouisticram3_pokemon.add(ouisticram3_pokemon_anim)

class Tiplouf_pokemon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tiplouf_pokemonanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Tiplouf1.png"), (70, 70)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Tiplouf2.png"), (70, 70)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tiplouf_pokemonanimation = True

    def update(self,speed):
        if self.Tiplouf_pokemonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tiplouf_pokemonanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tiplouf1_pokemon = pygame.sprite.Group()
moving_sprites_tiplouf2_pokemon = pygame.sprite.Group()
moving_sprites_tiplouf3_pokemon = pygame.sprite.Group()
tiplouf1_pokemon_anim = Tiplouf_pokemon_anim(50,40)
tiplouf2_pokemon_anim = Tiplouf_pokemon_anim(625,72)
tiplouf3_pokemon_anim = Tiplouf_pokemon_anim(50,232)
moving_sprites_tiplouf1_pokemon.add(tiplouf1_pokemon_anim)
moving_sprites_tiplouf2_pokemon.add(tiplouf2_pokemon_anim)
moving_sprites_tiplouf3_pokemon.add(tiplouf3_pokemon_anim)



class Tortipousse_pokemon_anim(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Tortipousse_pokemonanimation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Tortipousse1.png"), (70, 70)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("Animation/Miniature/Tortipousse2.png"), (70, 70)))
                    
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.Tortipousse_pokemonanimation = True

    def update(self,speed):
        if self.Tortipousse_pokemonanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.Tortipousse_pokemonanimation = False

        self.image = self.sprites[int(self.current_sprite)]


moving_sprites_tortipousse1_pokemon = pygame.sprite.Group()
moving_sprites_tortipousse2_pokemon = pygame.sprite.Group()
moving_sprites_tortipousse3_pokemon = pygame.sprite.Group()
tortipousse1_pokemon_anim = Tortipousse_pokemon_anim(50,40)
tortipousse2_pokemon_anim = Tortipousse_pokemon_anim(620,72)
tortipousse3_pokemon_anim = Tortipousse_pokemon_anim(50,235)
moving_sprites_tortipousse1_pokemon.add(tortipousse1_pokemon_anim)
moving_sprites_tortipousse2_pokemon.add(tortipousse2_pokemon_anim)
moving_sprites_tortipousse3_pokemon.add(tortipousse3_pokemon_anim)

