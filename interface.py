import pygame


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
                window.blit(pygame.transform.scale(get_object_pic(gun), 
                                                   (70,50)), (0, 0))
                self.screen.blit(window,  (self.x + dx, self.y))
                dx += 70


class Button:
    def __init__(self, screen, x, y, image, scale=1):
        
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.screen = screen

        
    def display(self):
        '''
        отображает кнопку на поверхности
        '''
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


    def click(self):
        '''
        проверяет, была ли кнопка нажата

        '''
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return self.clicked
    
    
def MainMenu(screen):
    '''
    Функция отображает главное меню и возвращает данные о нажатых кнопках
    '''
    menu_w, menu_h = screen.get_size()
    menu_img = pygame.transform.scale(pygame.image.load('models/main_menu.jpg').convert_alpha(),
                                      screen.get_size())
    screen.blit(menu_img, (0,0))
    start_img = pygame.image.load('models/start_btn.png').convert_alpha()
    exit_img = pygame.image.load('models/exit_btn.png').convert_alpha()
    settings_img = pygame.image.load('models/settings_btn.png').convert_alpha()
    info_img = pygame.image.load('models/info_btn.png').convert_alpha()
    
    start_button = Button(screen, menu_w/7, menu_h*2/3, start_img, 0.15)
    exit_button = Button(screen, menu_w*7/20, menu_h*5/6, exit_img, 0.15)
    setting_button = Button(screen, menu_w*3/5, menu_h*2/3, settings_img, 0.15)
    info_button = Button(screen, 0, 0, info_img, 0.15)

    exit_button.display()
    start_button.display()
    setting_button.display()
    info_button.display()
    pygame.display.update()
    return start_button.click(), exit_button.click(), setting_button.click(), info_button.click()

def AboutMenu(screen):
    '''
    Отображает страницу об игре

    '''
    screen.fill((179, 218, 241))
    screen.blit(pygame.image.load('models/regularExplosion00.png'), (0,0))
    delta = 50
    draw_text(screen, 'made by', 50, pygame.font.get_default_font(), (0,0,0), 300, 200)
    draw_text(screen, 'ShurfLL', 30, pygame.font.get_default_font(), (0,0,0), 300, 200+delta)
    draw_text(screen, 'Shmyrkov', 30, pygame.font.get_default_font(), (0,0,0), 300, 200+2*delta)
    draw_text(screen, 'negaskolya', 30, pygame.font.get_default_font(), (0,0,0), 300, 200+3*delta)
    draw_text(screen, 'sHiNkO1975', 30, pygame.font.get_default_font(), (0,0,0), 300, 200+4*delta)
    pygame.display.update()


def SettingsMenu(screen):
    '''
    Отображает страницу с настройками и возвращает 0 или 1

    '''
    mid_w, mid_h = screen.get_size()[0]/2, screen.get_size()[1]/2
    offset = 70
    screen.fill((179, 218, 241))
    draw_text(screen, 'Settings', 50, pygame.font.get_default_font(), (0,0,0), mid_w-offset, mid_h-offset)
    draw_text(screen, 'Volume', 50, pygame.font.get_default_font(), (0,0,0), mid_w, mid_h)
    close_img = pygame.image.load('models/close.png').convert_alpha()
    close_button = Button(screen, screen.get_width()*4/5, 0, close_img, 0.15)
    close_button.display()
    if close_button.click():
        return False
    else:
        return True
    

def PauseMenu(screen):
    '''
    меню паузы
    '''
    new_state = [False, False, False]
    width, height= screen.get_size()
    dest = (width*5/6, height/6)
    offset = 150
    '''offset_x, offset_y, offset = width/5, width/5, 300
    pause_screen = pygame.Surface((width*3/5, height*3/5))
    pause_screen.fill((0,0,0))
    pause_screen.set_alpha(170)
    '''
    close_img = pygame.image.load('models/return.png').convert_alpha()
    exit_img = pygame.image.load('models/back_to_menu.png').convert_alpha()
    settings_img = pygame.image.load('models/settings_btn2.png').convert_alpha()
    
    close_button = Button(screen, dest[0] - offset, dest[1], close_img, 0.3)
    exit_button = Button(screen, dest[0] - 2*offset, dest[1], exit_img, 0.3)
    settings_button = Button(screen, dest[0] - 3*offset, dest[1], settings_img, 0.3)
    
    close_button.display()
    exit_button.display()
    settings_button.display()
    
    if close_button.click():
        new_state[0] = True
    if exit_button.click():
        new_state[1] = True
    if settings_button.click():
        new_state[2] = True
    return new_state