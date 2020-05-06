import pygame


class Game:
    COLORS = {'white': (255, 255, 255)}

    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 600
        self.bg = pygame.transform.scale(pygame.image.load('assets/bg.png'), (self.width, self.height))
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        pygame.font.init()
        self.font = 'comicsans'
        self.big_font = pygame.font.SysFont(self.font, 72)
        self.med_font = pygame.font.SysFont(self.font, 36)
        self.small_font = pygame.font.SysFont(self.font, 18)

    def main_menu(self):
        menu_font = self.small_font.render('Press any key to start', True, self.COLORS['white'])
        instructions_font = self.med_font.render(
            'Use wasd keys to move and space bar to shoot',
            True,
            self.COLORS['white']
        )

        while True:
            self.window.blit(self.bg, (0, 0))
            self.window.blit(
                instructions_font,
                (
                    (self.width / 2) - (instructions_font.get_width() / 2),
                    (self.height / 2) - (instructions_font.get_height() / 2)
                )
            )
            self.window.blit(
                menu_font,
                ((self.width / 2) - (menu_font.get_width() / 2), (self.height / 2) + instructions_font.get_height())
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    #TODO: Lead to level
                    pass

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.main_menu()