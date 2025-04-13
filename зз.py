from pygame import *

img_back='now.png'

win_width=700
win_height=500
display.set_caption('Echo of Time')
window=display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (40, 40))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class WallSprite(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, x, y, width, height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def spawn(self):
        self.rect.x = 10000
        self.rect.y = 10000

class Enemy(GameSprite):
   direction = 'left'
   def update(self):
      if self.rect.x<=100:
         self.direction='right'
      if self.rect.x>=250:
         self.direction='left'
      if self.direction=='left':
         self.rect.x-=self.speed
      else:
         self.rect.x+=self.speed

w1= WallSprite(0,255, 0, 250,115,60,135)
w2= WallSprite(0,0, 255, 315,115,60,135)
w3= WallSprite(0,0, 255, 230,0,150,130)
w4= WallSprite(0,0, 255, 190,110,78,36)
w5=WallSprite(0,0,255,0,150,100,30)
w6=WallSprite(0,0,255,78,72,35,100)
w7=WallSprite(0,0,255,0,120,35,50)
w8=WallSprite(0,0,255,130,325,30,60)
w9=WallSprite(0,0,255,100,305,30,60)
w10=WallSprite(0,0,255,0,235,100,130)
w11=WallSprite(0,0,255,240,250,100,1000)
w12 = WallSprite(0,0, 255, 0,82,318,44)
w13=WallSprite(0,0,255,210,270,130,60)
w14=WallSprite(0,0,255,320,240,70,410)
w15 = WallSprite(0, 0, 255, 530, 20, 10, 410)
w16 = WallSprite(0, 0, 255, 310, 220, 190, 1000)
w17 = WallSprite(0, 0, 255, 270, 0, 10000, 80)
w18 = WallSprite(0, 0, 255, 580, 20, 1000,210)
w19 = WallSprite(0, 0, 255, 0, 0, 240, 110)
w20 = WallSprite(0, 0, 255, 0, 240, 240, 110)
w21 = WallSprite(0, 0, 255, 650, 270, 1000, 120)
w22 = WallSprite(255, 0, 0, 650, 350, 1000, 1020)
w23 = WallSprite(0, 0, 255, 0, 0, 1000, 130)
w24 = WallSprite(0, 0, 255, 655, 130, 100, 130)
w25 = WallSprite(0, 0, 255, 120, 190, 60, 140)
w26 = WallSprite(0, 0, 255, 310, 20, 60, 4130)
w27 = WallSprite(0, 0, 255, 250, 20, 60, 180)
w28 = WallSprite(0, 0, 255, 250, 350, 60, 180)
w29 = WallSprite(0, 0, 255, 190, 440, 60, 180)
w30 = WallSprite(0, 0, 255, 210, 0, 60, 130)
w31 = WallSprite(0, 0, 255, 0, 210, 140, 70)
w32 = WallSprite(255, 0, 0,999999, 150, 100, 140)

hp=3

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.default_image = player_image 
        self.alt_image1 = 'pramo1.png'
        self.alt_image2 = 'left1.png'
        self.alt_image3 = 'back1.png'
        self.alt_image4 = 'right1.png'
    def update(self, walls):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.image = transform.scale(image.load(self.alt_image2), (40, 40))
            if self.check_collision(walls):
                self.rect.x += self.speed
        if keys_pressed[K_d] and self.rect.x < win_width - 50:
            self.rect.x += self.speed
            self.image = transform.scale(image.load(self.alt_image4), (40, 40))
            if self.check_collision(walls):
                self.rect.x -= self.speed                
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
            self.image = transform.scale(image.load(self.alt_image1), (40, 40))
            if self.check_collision(walls):
                self.rect.y += self.speed 
        if keys_pressed[K_s] and self.rect.y < win_height - 50: 
            self.rect.y += self.speed
            self.image = transform.scale(image.load(self.alt_image3), (40, 40))
            if self.check_collision(walls):
                self.rect.y -= self.speed  
    def check_collision(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                return True
        return False
    def spawn(self):
        self.rect.x=5
        self.rect.y=500-80
        window.blit(self.image, (self.rect.x, self.rect.y))

run = True
finish = False

clock = time.Clock()
FPS = 60

player = Player('back1.png', 5, win_height - 80, 4)

walls = [w23,w24,w25,w26,w27,w28,w29,w30,w31]
#walls = [w14,w13, w12,w11,w10,w9,w8,w7,w6,w5,w4,w3,w2]
time='nastoiash'
kom=1

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        keys_pressed = key.get_pressed()
        if keys_pressed[K_r] and not key_pressed:
            print(time)
            if time == 'future':
                background = transform.scale(image.load('1.jpg'), (700,500))
                window.blit(background,(0, 0))
                time = '1'
                player = Player('back1.png', 1, win_height - 1, 1)
            elif time == '1':
                background = transform.scale(image.load('2.jpg'), (700,500))
                window.blit(background,(0, 0))
                time = '2'
                player = Player('back1.png', 1, win_height - 1, 1)
            elif time == '2':
                background = transform.scale(image.load('3.jpg'), (700,500))
                window.blit(background,(0, 0))
                time = '3'
                player = Player('back1.png', 1, win_height - 1, 1)
            elif time == '3':
                background = transform.scale(image.load('3.jpg'), (700,500))
                window.blit(background,(0, 0))
                time = '5'
                player = Player('back1.png', 1, win_height - 1, 1)
            elif time == '5':
                background = transform.scale(image.load('5.png'), (700,500))
                window.blit(background,(0, 0))
                time = '5'
                player = Player('back1.png', win_height - 1, 1)

            key_pressed = True
        elif not keys_pressed[K_r]:
            key_pressed = False

        window.blit(background, (0, 0))
        player.reset()
        player.update(walls)

        if time == 'proshloe' and kom == 1:
            walls=[w16,w17,w18,w19,w20,w21]
        if time == 'nastoiash' and kom == 1:
            walls=[w14,w13,w12,w11,w10,w9,w8,w7,w6,w5,w4,w3,w2]
        if time == 'future' and kom == 2:
            walls=[w23,w24,w25,w26,w27,w28,w29,w30,w31,w32]
        if time == 'nastoiash' and kom == 2:
            walls=[]
        if sprite.collide_rect(player,w1):
            w1.spawn()
            background = transform.scale(image.load('past.jpg'), (700,500))
            window.blit(background,(0, 0))
            time='proshloe'
        if sprite.collide_rect(player,w22):
            w22.spawn()
            background = transform.scale(image.load('simpl.2.0.png'), (700,500))
            window.blit(background,(0, 0))
            time='future'
            kom=2
            player.spawn()
        if sprite.collide_rect(player,w32):
            w32.spawn()
            background = transform.scale(image.load('now.jpg'), (700,500))
            window.blit(background,(0, 0))
            time='nastoiash'
            player.spawn()

#        if hp>=1:
#            if sprite.collide_rect(player, mon1):
#                player.spawn()
#                hp-=1
#        else:
#            print('sad')
    display.update()
    clock.tick(FPS)
