import pygame


def get_object_pic(weapon):
    """Загружает изображение объекта из модуля objects"""
    if weapon != None:
        return weapon.sprite
    else:
        pass

def draw_text(display, text, size, font_name, color, x, y):
    """Отрисовывает текст заданного размера и шрифта"""
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    display.blit(text_surface,text_rect)
    

class Inventory():
    """Инвентарь для игрока"""
    def __init__(self, screen, weapons):
        self.screen = screen
        self.inventory = weapons
        WIDTH, HEIGHT = screen.get_size()
        self.x, self.y = WIDTH/20, HEIGHT/10
    
    
    def draw(self, player):
        """Отрисовывает спрайт оружия на экране"""
        dx = 0
        if self.inventory[0] == None:
            return
        else:
            for gun in self.inventory:
                if gun == player.weapon:
                    window = pygame.Surface((70, 50))
                    window.fill((0, 0, 200))
                    window.blit(pygame.transform.scale(get_object_pic(gun), 
                                                       (70,50)), (0, 0))
                    self.screen.blit(window,  (self.x + dx, self.y))
                    dx += 70
                else:
                    window = pygame.Surface((70, 50))
                    window.fill((255, 255, 0))
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

        
    def draw(self):
        """Отображает кнопку на поверхности"""
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


    def click(self):
        """Проверяет, была ли кнопка нажата"""
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action
    
    
class Slider():
    '''Ползунок для меню'''
    def __init__(self, screen, text, start_val, maximum, minimum, pos, scale = 1):
        self.screen = screen
        self.txt_surf = pygame.Surface((100*scale, 40))
        draw_text(self.txt_surf, 'Volume', 40, pygame.font.get_default_font(), (100,0,0), 100*scale/2, 20)#pygame.font.SysFont("Verdana", 40).render(text, 1, (0, 0, 0))
        self.start_val = start_val
        self.max = maximum
        self.min = minimum
        self.pos = pos
        self.scale = scale
        self.width, self.height = 100, 50
        self.surf = pygame.surface.Surface((self.width*scale, self.height*scale))
        self.hit = False
        self.txt_rect = self.txt_surf.get_rect(center=(50*scale, 15*scale))
        self.surf.fill((100, 100, 100))
        pygame.draw.rect(self.surf, (100, 100, 100), [0, 0, self.width*scale, self.height*scale], 3*scale)
        pygame.draw.rect(self.surf, (255, 255, 255), [10*scale, 30*scale, 80*scale, 5*scale], 0)
        pygame.draw.rect(self.surf, (255, 140, 0), [10*scale, 10*scale, 80*scale, 10*scale], 0)
        self.surf.blit(self.txt_surf, self.txt_rect)
        self.button_surf = pygame.surface.Surface((20*scale, 20*scale))
        self.button_surf.fill((1, 1, 1))
        self.button_surf.set_colorkey((1, 1, 1))
        pygame.draw.circle(self.button_surf, (0, 0, 0), (10*scale, 10*scale), 6*scale/2, 0)
        pygame.draw.circle(self.button_surf, (255, 140, 0), (10*scale, 10*scale), 4*scale/2, 0)
        
    def draw(self):
        """Рисует ползунок"""
        surf = self.surf.copy()
        new_pos = (10*self.scale+int((self.start_val-self.min)/(self.max-self.min)*80*self.scale), 33*self.scale)
        self.button_rect = self.button_surf.get_rect(center=new_pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.pos[0], self.pos[1])
        self.screen.blit(surf, (self.pos[0], self.pos[1]))
        
    def move(self):
        """Меняет положение ползунка в зависимости от полодения мыши"""
        self.start_val = (pygame.mouse.get_pos()[0] - self.pos[0] - self.scale*10) / (self.scale*80) * (self.max - self.min) + self.min
        if self.start_val < self.min:
            self.start_val = self.min
        if self.start_val > self.max:
            self.start_val = self.max
            
            
class MainMenu():
    def __init__(self, screen):
        self.on, self.start_game, self.quit, self.settings = True, False, False, False
        self.info = False
        self.screen = screen
        menu_w, menu_h = screen.get_size()
        self.menu_img = pygame.transform.scale(pygame.image.load('models/main_menu.jpg').convert_alpha(),
                                          screen.get_size())
        start_img = pygame.image.load('models/start_btn.png').convert_alpha()
        exit_img = pygame.image.load('models/exit_btn.png').convert_alpha()
        settings_img = pygame.image.load('models/settings_btn.png').convert_alpha()
        info_img = pygame.image.load('models/info_btn.png').convert_alpha()
        self.bang_img = pygame.image.load('models/regularExplosion00.png')
        self.start_button = Button(self.screen, menu_w/7, menu_h*2/3, start_img, 0.15)
        self.exit_button = Button(self.screen, menu_w*7/20, menu_h*5/6, exit_img, 0.15)
        self.setting_button = Button(self.screen, menu_w*3/5, menu_h*2/3, settings_img, 0.15)
        self.info_button = Button(self.screen, 0, 0, info_img, 0.15)
    
    def draw(self):
        self.screen.blit(self.menu_img, (0,0))
        self.exit_button.draw()
        self.start_button.draw()
        self.setting_button.draw()
        self.info_button.draw()
        
    def check_events(self):
        """Проверяет, нажаты ли кнопки и обновляет состояния"""
        if self.exit_button.click():
            self.quit = True
        if self.start_button.click():
            self.on = False
            self.start_game = True
        if self.setting_button.click():
            self.on = False
            self.settings = True
        if self.info_button.click():
            self.info = True
            
    def AboutMenu(self):
        """Отрисовывает меню с информацией пока зажата кнопка"""
        self.screen.fill((179, 218, 241))
        self.screen.blit(self.bang_img, (0,0))
        delta = 50
        draw_text(self.screen, 'made by', 50, pygame.font.get_default_font(), (0,0,0), 300, 200)
        draw_text(self.screen, 'ShurfLL', 30, pygame.font.get_default_font(), (0,0,0), 300, 200+delta)
        draw_text(self.screen, 'Shmyrkov', 30, pygame.font.get_default_font(), (0,0,0), 300, 200+2*delta)
        draw_text(self.screen, 'negaskolya', 30, pygame.font.get_default_font(), (0,0,0), 300, 200+3*delta)
        draw_text(self.screen, 'sHiNkO1975', 30, pygame.font.get_default_font(), (0,0,0), 300, 200+4*delta)
        if not self.info_button.clicked:
            self.info = False
            self.on = True


class SettingsMenu():
    def __init__(self, screen):
        self.on = False
        self.screen = screen
        self.mid_w, self.mid_h = screen.get_size()[0]/2, screen.get_size()[1]/2
        self.offset = 70
        close_img = pygame.image.load('models/close.png').convert_alpha()
        self.close_button = Button(screen, screen.get_width()*4/5, 0, close_img, 0.15)
        self.volume = Slider(self.screen, 'Volume', 20,
                             100, 0, (self.mid_w - 3*self.offset, self.mid_h), 4)

    
    def draw(self):
        self.screen.fill((179, 218, 241))
        draw_text(self.screen, 'Settings', 50, pygame.font.get_default_font(),
                  (0,0,0), self.mid_w, self.mid_h - self.offset)
        self.close_button.draw()
        self.volume.draw()
        
    def check_events(self):
        """Обновляет состояния меню настроек и звук в игре"""
        if self.close_button.click():
            self.on = False
        if self.volume.hit:
            self.volume.move()
    

class PauseMenu():
    def __init__(self, screen):
        self.on = False
        self.to_menu = False
        self.settings = False
        width, height= screen.get_size()
        dest = (width*5/6, height/6)
        offset = 150
        close_img = pygame.image.load('models/return.png').convert_alpha()
        exit_img = pygame.image.load('models/back_to_menu.png').convert_alpha()
        settings_img = pygame.image.load('models/settings_btn2.png').convert_alpha()
        
        self.button = Button(screen, width*5/6, height/6,
                                     pygame.image.load('models/pause_btn.png').convert_alpha(), 0.15)
        self.close_button = Button(screen, dest[0] - offset, dest[1], close_img, 0.3)
        self.exit_button = Button(screen, dest[0] - 2*offset, dest[1], exit_img, 0.3)
        self.settings_button = Button(screen, dest[0] - 3*offset, dest[1], settings_img, 0.3)
    
    def draw(self):
        self.button.draw()
        if self.on:
            self.close_button.draw()
            self.exit_button.draw()
            self.settings_button.draw()
        
    def check_events(self):
        """Проверяет, нажаты ли кнопки о обновляет состояния"""
        if self.button.click():
            self.on = True
        if self.close_button.click() and self.on:
            self.on = False
        if self.exit_button.click() and self.on:
            self.on = False
            self.to_menu = True
        if self.settings_button.click() and self.on:
            self.settings = True
