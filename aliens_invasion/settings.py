class Settings():
    '''Класс для хранения всех настроек игры'''

    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (28, 28, 28)
        self.ship_speed = 15
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_collor = (3, 174, 255)
        self.bullets_allowed = 3
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        #fleet_direction = 1 обозначает вправо, а -1 - влево.
        self.fleet_direction = 1
        self.ship_limit = 3
