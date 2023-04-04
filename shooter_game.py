from pygame import *
from random import randint

font.init()
font1 = font.SysFont('verdana', 70)
win = font1.render('YOU WIN', True, (255, 255, 255))
lose = font1.render(' YOU LOSE', True, (180, 0, 0))

font2 = font.SysFont('verdana', 32)

img_back = 'galaxy.jpg'
img_bullet = 'bulet.png'
img_hero = 'rocket.png'
img_enemy = 'ufo.png'
img_ast = 'asteroid.png'
img_hp = 'health.png'

score = 0
goal = 10
lost = 0
max_lost = 3



class GameSprite(sprite.Sprite):

    def __init__(self,player_x,player_y,player_image,size_x,size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.rect = self.image.get_rect(topleft =(self.x, self.y))

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



class Player(GameSprite):
    def __init__ (self, player_x,player_y,player_image,size_x,size_y, player_speed,hp):
        super().__init__(player_x,player_y,player_image,size_x,size_y, player_speed)
        self.hp = hp

    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < win_width -80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rest.top, 15, 20, -15)
        bulets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kill()

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('Shooter')
background = transform.scale(image.load('galaxy.jpg'), (win_width,win_height))
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10, 15)
monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1,5))
    monsters.add(monster)
bullets = sprite.Group()
run = True
finish = False
print(run)
while run:
    print('1')
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.type == K_SPACE:
                fire_sound.play()
                ship.fire()
    if not finish:
        window.blit(background, (0,0))
        ship.update()
        monsters.update()
        bullets.update()
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score +1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1,5))
            monsters.add(monster)
        if sprite.spritecollede(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200,200))
        if score >= goal:
            finish = True
            window.blit(win, (200,200))
        text = font2.render('Счет:' + str(score), 1, (255,255,255))
        window.blit(text_lose, (10,50))

        display.update()
    time.delay(50)