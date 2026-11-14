import pygame

class InputHandler:
    def __init__(self) -> None:
        self.input_vector = pygame.Vector2(0,0)
    
    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.input_vector += pygame.Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.input_vector += pygame.Vector2(1, 0)
                if event.key == pygame.K_DOWN:
                    self.input_vector += pygame.Vector2(0, 1)
                if event.key == pygame.K_UP:
                    self.input_vector += pygame.Vector2(0, -1)
