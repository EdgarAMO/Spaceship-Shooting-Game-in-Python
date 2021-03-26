# Invaders
# Date: 30 / jan / 2021
# Author: Edgar A. M.

import pygame
import sys
import random

""" Objects """
class Player(pygame.sprite.Sprite):
    
    """ inherites from Sprite class """
    def __init__(self):
        super().__init__()

        # horizontal clearance
        self.hc = 64

        # vertical clearance
        self.vc = 32

        # speed
        self.speed = 0
        
        # amount of pixels to be moved
        self.amount = 5

        # current frame
        self.frame = 0

        # crash status
        self.crash = False
        
        # explode status
        self.explode = False

        # font
        self.font = pygame.font.SysFont('FixedSys', 32)

        # score
        self.score = 0

        # boom images
        self.sprites = []
        self.sprites.append(pygame.image.load('explosion1.png'))
        self.sprites.append(pygame.image.load('explosion2.png'))
        self.sprites.append(pygame.image.load('explosion3.png'))
        self.sprites.append(pygame.image.load('explosion4.png'))
        self.sprites.append(pygame.image.load('explosion5.png'))
        self.sprites.append(pygame.image.load('explosion6.png'))
        self.sprites.append(pygame.image.load('explosion7.png'))
        self.sprites.append(pygame.image.load('explosion8.png'))
        self.sprites.append(pygame.image.load('explosion9.png'))
        self.sprites.append(pygame.image.load('explosion10.png'))
        self.sprites.append(pygame.image.load('explosion11.png'))
        self.sprites.append(pygame.image.load('explosion12.png'))
        
        # spaceship image
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect(center=(self.hc, H/2))

        self.orig = pygame.image.load("ship.png")

        # sound
        self.laser = pygame.mixer.Sound('laser.wav')
        self.blast = pygame.mixer.Sound('blast.wav')

    def update(self, bullets):
        self.crash = self.check(bullets)

        text = str(self.score)
        color = (255, 255, 255)
        pos = (544, 16)
        screen.blit(self.font.render(text, True, color), pos)

        if self.crash:
            self.explode = True
        
        if self.explode:
            # stop moving
            self.speed = 0

            if self.frame >= len(self.sprites):
                # reset to initial frame
                self.frame = int(0)

                # play blast if explosion begins
                if self.frame == 0:
                    self.blast.play()

                # reset to original image
                self.image = self.orig
                x = self.rect.centerx
                y = self.rect.centery
                self.rect = self.image.get_rect(center=(x, y))

                # stop explosion
                self.explode = False

                # give one point to the opponent
                self.score += 1
            else:
                self.image = self.sprites[ int(self.frame) ]

            self.frame += 0.25
            
        else:
            self.move()
            
    def move(self):
        self.rect.centery += self.speed
        
        if self.rect.top <= self.vc:
            self.rect.top = self.vc
            
        if self.rect.bottom >= H - self.vc:
            self.rect.bottom = H - self.vc

    def check(self, bullets):
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                return True
            
    def shoot(self):
        self.laser.play()
        return Bullet(self)



class Enemy(pygame.sprite.Sprite):
    
    """ inherites from Sprite class """
    def __init__(self):
        super().__init__()

        # horizontal clearance
        self.hc = 64

        # vertical clearance
        self.vc = 32

        # amount of pixels to be moved
        self.amount = 7
        
        # speed
        self.speed = self.amount

        # shoot interval
        self.dt = 50

        # current frame
        self.frame = 0

        # crash status
        self.crash = False
        
        # explode status
        self.explode = False

        # font
        self.font = pygame.font.SysFont('FixedSys', 32)

        # score
        self.score = 0

        # boom images
        self.sprites = []
        self.sprites.append(pygame.image.load('explosion1.png'))
        self.sprites.append(pygame.image.load('explosion2.png'))
        self.sprites.append(pygame.image.load('explosion3.png'))
        self.sprites.append(pygame.image.load('explosion4.png'))
        self.sprites.append(pygame.image.load('explosion5.png'))
        self.sprites.append(pygame.image.load('explosion6.png'))
        self.sprites.append(pygame.image.load('explosion7.png'))
        self.sprites.append(pygame.image.load('explosion8.png'))
        self.sprites.append(pygame.image.load('explosion9.png'))
        self.sprites.append(pygame.image.load('explosion10.png'))
        self.sprites.append(pygame.image.load('explosion11.png'))
        self.sprites.append(pygame.image.load('explosion12.png'))

        # spaceship image
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.flip(self.image, 0, 1)
        self.rect = self.image.get_rect(center=(W-self.hc, H/2))

        self.orig = pygame.image.load("ship.png")
        self.orig = pygame.transform.flip(self.orig, 0, 1)

        # sound
        self.laser = pygame.mixer.Sound('laser.wav')
        self.blast = pygame.mixer.Sound('blast.wav')

    def update(self, bullets):
        self.crash = self.check(bullets)

        text = str(self.score)
        color = (255, 255, 255)
        pos = (480, 16)
        screen.blit(self.font.render(text, True, color), pos)

        if self.crash:
            self.explode = True
        
        if self.explode:
            # stop moving
            self.speed = 0

            if self.frame >= len(self.sprites):
                # reset to initial frame
                self.frame = int(0)

                # play blast if explosion begins
                if self.frame == 0:
                    self.blast.play()

                # shift to original image
                self.image = self.orig
                x = self.rect.centerx
                y = self.rect.centery
                self.rect = self.image.get_rect(center=(x, y))

                # stop explosion
                self.explode = False

                # reset movement
                self.speed = self.amount

                # give one point to the opponent
                self.score += 1
            else:
                self.image = self.sprites[ int(self.frame) ]

            self.frame += 0.25
            
        else:
            self.move()

    def move(self):
        self.rect.centery += self.speed
        
        if self.rect.top <= self.vc or self.rect.bottom >= H - self.vc:
            self.speed *= -1

    def check(self, bullets):
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                return True

    def shoot(self, ticks):
        if self.explode:
            return None
        if not ticks % self.dt:
            if random.choice((1, 0)):
                self.laser.play()
                return Bullet(self)



class Bullet(pygame.sprite.Sprite):
    """ inherits from Sprite class """
    
    def __init__(self, player):
        super().__init__()

        # player from which the bullet is shot
        self.player = player
        
        if isinstance(player, Player):
            self.image = pygame.image.load("yellow_laser.png")
            x = player.rect.midright[0]
            y = player.rect.midright[1]
            self.rect = self.image.get_rect(center=(x, y))

        if isinstance(player, Enemy):
            self.image = pygame.image.load("red_laser.png")
            x = player.rect.midleft[0]
            y = player.rect.midleft[1]
            self.rect = self.image.get_rect(center=(x, y))
        
    def update(self):
        if isinstance(self.player, Player):
            self.rect.x += 5
        if isinstance(self.player, Enemy):
            self.rect.x -= 5
        self.destroy()

    def destroy(self):
        if isinstance(self.player, Player):
            if self.rect.x >= W - 16:
                self.kill()
        if isinstance(self.player, Enemy):
            if self.rect.x <= 16:
                self.kill()



""" Settings """
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

W, H = 1024, 512
screen = pygame.display.set_mode((W, H))

""" Sprites """
player = Player()
playerGroup = pygame.sprite.Group()
playerGroup.add(player)

enemy  = Enemy()
enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy)

yellowBulletGroup = pygame.sprite.Group()
redBulletGroup = pygame.sprite.Group()

""" Main Loop """
while 1:

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # QUIT
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # UP
            if event.key == pygame.K_w:
                player.speed -= player.amount
            # DOWN
            if event.key == pygame.K_s:
                player.speed += player.amount
            # SHOOT
            if event.key == pygame.K_SPACE:
                yellowBullet = player.shoot()
                yellowBulletGroup.add(yellowBullet)
        if event.type == pygame.KEYUP:
            # UP
            if event.key == pygame.K_w:
                player.speed = 0
            # DOWN
            if event.key == pygame.K_s:
                player.speed = 0
            
    # Drawing
    screen.fill((30, 30, 30))

    # Player update
    playerGroup.draw(screen)
    playerGroup.update(redBulletGroup)

    # Enemy shoots
    redBullet = enemy.shoot(pygame.time.get_ticks())
    if redBullet == None:
        pass
    else:
        redBulletGroup.add(redBullet)

    # Enemy update
    enemyGroup.draw(screen)
    enemyGroup.update(yellowBulletGroup)

    # Bullets update
    yellowBulletGroup.draw(screen)
    yellowBulletGroup.update()
    
    redBulletGroup.draw(screen)
    redBulletGroup.update()
    
    pygame.display.flip()
    clock.tick(60)
    
