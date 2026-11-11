from settings import *
from scripts.core.players import Player
from subprocess import run
import pygame as pg

class Game:
    def __init__(self):
        self.running = True
        self.sc = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.events = None

    def _cls(self): run(['cls'], shell=True)

    def run(self):
        self._cls()
        p = Player()
        while self.running:
            pg.display.set_caption(f'{TITLE}    FPS: {round(self.clock.get_fps())}')
            self.sc.fill(GRAY)
            self.clock.tick(FPS)
            self.events = pg.event.get()
            for event in self.events:
                if event.type == pg.QUIT:
                    self.running = False

            p.talk()
            p.draw(self.sc)

            pg.display.flip()            

if __name__ == "__main__":
    g = Game()
    g.run()