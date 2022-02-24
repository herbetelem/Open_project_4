from datetime import datetime
import pygame


class Date_selected:
    """Object to create the diffrente element of the date
    """

    def __init__(self, unity, x, y):
        """

        Args:
            unity (_type_): _description_
            x (_type_): _description_
            y (_type_): _description_
        """

        font_date = pygame.font.Font(None, 70)
        self.str = int(datetime.now().strftime(unity))
        self.str_font = font_date.render(str(self.str), 1, (255, 255, 255))
        self.rect = self.str_font.get_rect()
        self.rect.x = x
        self.rect.y = y
