import sys
import pygame
from pygame.examples.scrap_clipboard import screen
from pygame.sprite import Group

from alien import Alien
from settings import Settings
from  ship import Ship
import game_functions as gf
from bullet import Bullet






def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船、一个用于存储子弹的编组、一个外星人
    ship = Ship(ai_settings,screen)
    bullets = Group()
    #alien = Alien(ai_settings, screen)
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
