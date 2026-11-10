from scripts.settings import *
import pygame as pg
import os

class Player:
    def __init__(self):
        self.speed = PLAYER_SPEED
        self.angle = PLAYER_ANGLE
        self.angle_speed = PLAYER_ANGLE_SPEED
        self.hp = PLAYER_HP
        self.dp = PLAYER_DP
        self.idle_img = pg.image.load(os.path.join('assets/Mike', 'Mike_idle_1.png'))
        self.idle_img = pg.transform.scale(self.idle_img, (200, 200))
        self.talk_imgs = [pg.transform.scale(pg.image.load(os.path.join('assets/Mike', f'Mike_talk_{x}.png')), (200, 200)) for x in range(1, 3)]
        self.curr_img = self.idle_img
        self.animation_count = 0
        self.x = 120
        self.y = 120
        self.is_dead = False
        self.tick = 0 
        self.timer = FPS // 2
        self.frame = 0

    def draw(self, sc):
        sc.blit(self.curr_img, (self.x, self.y))

    def hit(self, dmg):
        self.hp = self.hp - dmg
        if self.hp <= 0:
            self.is_dead = True
            return False
        else: return True

    def idle(self):
        self.curr_img = self.idle_img

    def talk(self):
        self.tick += 1
        if self.tick >= self.timer:
            self.tick = 0
            if self.frame == 1: self.frame = 0
            elif self.frame == 0: self.frame = 1
            self.curr_img = self.talk_imgs[self.frame]
        