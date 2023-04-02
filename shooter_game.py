#Создай собственный Шутер!

from pygame import *
from random import randint
win = display.set_mode((700, 500))
bg = transform.scale(image.load('galaxy.jpg'), (700, 500))


game = True
finish = False
lost = 0

 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 695:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(imq_bullet, self.rect.centerx-10, self.rect.top, -15, 20, 30)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 700:
            self.rect.x = randint(80, 420)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

monsters = sprite.Group()
ufo1 = Enemy('ufo.png', 10, -10, randint(1, 3), 70, 40)
ufo2 = Enemy('ufo.png', 10, -10, randint(1, 3), 70, 40)
ufo3 = Enemy('ufo.png', 10, -10, randint(1, 3), 70, 40)
ufo4 = Enemy('ufo.png', 10, -10, randint(1, 3), 70, 40)
ufo5 = Enemy('ufo.png', 10, -10, randint(1, 3), 70, 40)
monsters.add(ufo1)
monsters.add(ufo2)
monsters.add(ufo3)
monsters.add(ufo4)
monsters.add(ufo5)

asteroids = sprite.Group()
asteroid1 = Enemy('asteroid.png', 10, -10, randint(1, 3), 70, 70)
asteroid2 = Enemy('asteroid.png', 10, -10, randint(1, 3), 70, 70)
asteroid3 = Enemy('asteroid.png', 10, -10, randint(1, 3), 70, 70)
asteroid4 = Enemy('asteroid.png', 10, -10, randint(1, 3), 70, 70)
asteroid5 = Enemy('asteroid.png', 10, -10, randint(1, 3), 70, 70)
monsters.add(asteroid1)
monsters.add(asteroid2)
monsters.add(asteroid3)
monsters.add(asteroid4)
monsters.add(asteroid5)

rocket = Player('rocket.png', 5, 400, 4, 40, 70)


while game:
    
    

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        win.blit(bg,(0, 0))
        rocket.update()
        ufo1.reset()
        ufo1.update()
        ufo2.reset()
        ufo2.update()
        ufo3.reset()
        ufo3.update()
        ufo4.reset()
        ufo4.update()
        ufo5.reset()
        ufo5.update()
    rocket.reset()
    display.update()
    
    
    clock.tick(FPS)
    










