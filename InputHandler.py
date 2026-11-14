import pygame

class InputHandler:
    def __init__(self) -> None:
        self.input_vector_normalized = pygame.Vector2(0,0)
        self.space_pressed = False
    
    def Update(self):
        keys = pygame.key.get_pressed() # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

        self.input_vector_normalized = pygame.Vector2(0,0)

        if keys[pygame.K_LEFT]:
            self.input_vector_normalized += pygame.Vector2(-1, 0)
        if keys[pygame.K_RIGHT]:
            self.input_vector_normalized += pygame.Vector2(1, 0)
        if keys[pygame.K_DOWN]:
                self.input_vector_normalized += pygame.Vector2(0, 1)
        if keys[pygame.K_UP]:
                self.input_vector_normalized += pygame.Vector2(0, -1)

        self.input_vector_normalized.normalize # what i learned from unity 
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.space_pressed = True
            else:
                pass

