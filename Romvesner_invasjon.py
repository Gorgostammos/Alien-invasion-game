import sys
import pygame
from ship import Ship
from setting import Settings

class Alieninvasion:
    """Hovedklassen som håndterer spillets ressurser og oppførsel."""

    def __init__(self):
        """Initialiser spillet og opprett spillressurser."""
        pygame.init()  # Initialiserer Pygame-modulen
        self.settings = Settings()  # Oppretter et Settings-objekt med spillets innstillinger

        # Setter opp skjermen med bredde og høyde fra Settings
        self.screen = pygame.display.set_mode((self.settings.screen_witdh, self.settings.screen_height))
        pygame.display.set_caption("Romvesner Kommer")  # Gir spillet en tittel

        self.ship = Ship(self)  # Oppretter et skip-objekt (spillerens figur)

    def run_game(self):
        """Starter hovedløkken for spillet."""
        while True:
            self._check_events()  # Sjekker brukerens input (f.eks. tastetrykk)
            self.ship.update()  # Oppdaterer skipets posisjon
            self._update_screen()  # Tegner skjermen på nytt

    def _check_events(self):
        """Sjekker for brukerens input-hendelser."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Avslutt spillet når brukeren lukker vinduet
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Når en tast trykkes ned
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # Når en tast slippes
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Håndterer tastetrykk."""
        if event.key == pygame.K_RIGHT:  # Hvis høyre pil trykkes
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # Hvis venstre pil trykkes
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # Hvis 'Q'-tasten trykkes (avslutt spillet)
            sys.exit()

    def _check_keyup_events(self, event):
        """Håndterer når en tast slippes."""
        if event.key == pygame.K_RIGHT:  # Stopper bevegelsen til høyre
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  # Stopper bevegelsen til venstre
            self.ship.moving_left = False

    def _update_screen(self):
        """Oppdaterer skjermen ved å tegne den på nytt."""
        self.screen.fill(self.settings.bg_color)  # Fyller bakgrunnen med valgt farge
        self.ship.blitme()  # Tegner skipet på skjermen
        pygame.display.flip()  # Oppdaterer skjermen for å vise de nyeste tegningene

if __name__ == '__main__':
    ai = Alieninvasion()  # Oppretter en instans av spillet
    ai.run_game()  # Starter spillet



## er på side 245ddfd