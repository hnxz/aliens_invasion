class Settings():
    '''Класс для хранения всех настроек игры'''

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (28, 28, 28)
        self.ship_speed = 3
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_collor = (3, 174, 255)
        self.bullets_allowed = 3
        self.alien_speed = 1
        self.fleet_drop_speed = 3

        #Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

        #fleet_direction = 1 обозначает вправо, а -1 - влево.
        self.fleet_direction = 1
        self.ship_limit = 3

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        #fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличение настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
