import pygame


game_running, game_playing = True, False
START_KEY, BACK_KEY, DOWN_KEY, UP_KEY, ESCAPE_KEY = 0,0,0,0,0


def get_object_pic(weapon):
    if weapon != None:
        return pygame.image.load(weapon.sprite)
    else:
        pass

def draw_text(display, text, size, font_name, color, x, y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    display.blit(text_surface,text_rect)
    

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running, game_playing = False, False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                START_KEY = True
            if event.key == pygame.K_BACKSPACE:
                BACK_KEY = True
            if event.key == pygame.K_DOWN:
                DOWN_KEY = True
            if event.key == pygame.K_UP:
                UP_KEY = True
            if event.key == pygame.K_ESCAPE:
                ESCAPE_KEY = True

class Inventory():
    def __init__(self, screen, weapons):
        self.screen = screen
        self.inventory = weapons
        WIDTH, HEIGHT = screen.get_size()
        self.x, self.y = WIDTH/3, HEIGHT*5/6
    
    
    def display(self):
        dx = 0
        if self.inventory[0] == None:
            return
        else:
            for gun in self.inventory:
                window = pygame.Surface((70, 50))
                window.fill((186, 140, 99))
                print(type(get_object_pic(gun)))
                window.blit(pygame.transform.scale(get_object_pic(gun), 
                                                   (70,50)), (0, 0))
                self.screen.blit(window,  (self.x + dx, self.y))
                dx += 70


class Button:
    def __init__(self, screen: pygame.Surface, text, size: tuple, x=40, y=450, color=(255, 255, 255)):
        '''
        text - str: name of the picture or text to draw
        '''
        self.screen = screen
        self.x = x
        self.y = y
        self.r = size
        self.color = color
        self.clicked = False
        self.text = text

        
    def display_text(self):
        button = pygame.Surface((self.r[0], self.r[1]))
        button.fill((255, 0, 0))
        draw_text(button, self.text, 16, pygame.font.get_default_font(),
                  self.color, self.r[0]/2, self.r[1]/2)
        self.screen.blit(button, (self.x, self.y))
        
    def display_pic(self):
        window = pygame.Surface(self.r)
        window.fill((255,255,255))
        window.blit(pygame.transform.scale(pygame.image.load(self.text),
                                           (70,50)), (0, 0))
        self.screen.blit(window,  (self.x, self.y))
        
        
    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and game_running == True:
            mouse_coord = (event.pos)
            if (abs(mouse_coord[0]-self.x) <= self.r[0] and 
                abs(mouse_coord[1]-self.y) <= self.r[1]):
                self.clicked = True