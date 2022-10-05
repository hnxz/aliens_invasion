import pygame
from settings import Settings
class Ship():
    '''Класс управления кораблем.'''
    def __init__(self,ai_game):
        '''Инициализирует корабль и задает его начальную позицию'''
        self.screen = ai_game
        self.settings = Settings()
        self.screen_rect = ai_game.get_rect()
        #Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    def update(self):
        '''Обновляет позицию коробля с учетом флага'''
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x
    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)