class Settings:
    """En klasse for å lagre alle innstillinger for spillet."""

    def __init__(self):
        """Initialiserer spillets innstillinger."""
        # self.screen_witdh = 1200  # Skjermens bredde
        # self.screen_height = 800  # Skjermens høyde
        self.bg_color = (28, 37, 60)  # Bakgrunnsfargen (RGB-verdi)

        # Skipets innstillinger
        self.ship_speed = 0.2  # Hvor raskt skipet beveger seg

        # Bullet settings

        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        self.bullet_color = (247, 246, 187)