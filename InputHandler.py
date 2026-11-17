import pygame

class InputHandler:
    def __init__(self, window) -> None:
        self.window = window

        self.input_vector_normalized = pygame.Vector2(0,0)
        self.space_pressed = False
        self.shift_pressed = False

        self.is_max = False
    
    def update(self) -> bool:
        keys = pygame.key.get_pressed() # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

        self.input_vector_normalized = pygame.Vector2(0,0)
        self.space_pressed = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.input_vector_normalized += pygame.Vector2(-1, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.input_vector_normalized += pygame.Vector2(1, 0)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.input_vector_normalized += pygame.Vector2(0, 1)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.input_vector_normalized += pygame.Vector2(0, -1)

        self.shift_pressed = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

        if self.input_vector_normalized.length() > 0:
            self.input_vector_normalized.normalize_ip() # what i learned from unity
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.space_pressed = True
            else:
                pass

        return True

