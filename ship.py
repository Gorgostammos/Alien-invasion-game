import pygame

class Ship:
    """En klasse som håndterer skipet."""

    def __init__(self, ai_game):
        """Initialiserer skipet og setter startposisjonen."""
        self.screen = ai_game.screen  # Henter skjermen fra hovedspillet
        self.settings = ai_game.settings  # Henter innstillinger fra hovedspillet
        self.screen_rect = ai_game.screen.get_rect()  # Får rektangelet til skjermen

        # Laster inn bildet av skipet og får rektangelet til bildet
        self.image = pygame.image.load('bilder/ship.png')
        self.rect = self.image.get_rect()

        # Plasserer skipet nederst i midten av skjermen
        self.rect.midbottom = self.screen_rect.midbottom

        # Lagrer skipets posisjon som et desimaltall for presis bevegelse
        self.x = float(self.rect.x)

        # Flag for å holde oversikt over bevegelse
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Oppdaterer skipets posisjon basert på bevegelsesflagget."""
        # Flytter skipet mot høyre hvis flagget er satt, og det ikke går utenfor skjermen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # Flytter skipet mot venstre hvis flagget er satt, og det ikke går utenfor skjermen
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Oppdaterer skipets rektangel basert på den nye x-posisjonen
        self.rect.x = self.x

    def blitme(self):
        """Tegner skipet på skjermen på sin nåværende posisjon."""
        self.screen.blit(self.image, self.rect)
