import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Класс для управления ресурсами поведения игры.'''
    def __init__(self):
        '''Инициализирует игру и создает игровые ресурсы'''
        pygame.init()
        #Назначение цвета фона
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen)

    def run_game(self):
        '''Запускает основной цикл игры'''
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #переместить корабль вправо.
                    self.ship.rect.x += 1

    def _update_screen(self):
        # При каждом проходе цикла перересовывается экран.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
