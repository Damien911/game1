import random
import pygame
import os

#Opcje
whatShow = "menu"
iloscBiedr = 200
points = 0
pygame.init()

windowX = 1200
windowY =  800

screen = pygame.display.set_mode((windowX, windowY))
pygame.mouse.set_visible(False)
biedronki = []

borders = []



def write(text, x, y, size):
    fo = pygame.font.SysFont("Arial", size)
    rend = fo.render(text, 1, (255,0, 0))
    screen.blit(rend, (x, y))
    #width = (windowX - rend.get_rect().width)/2
    #hight = (windowY - rend.get_rect().height)/2
    

class biedronka():

    def __init__(self, direction):
        self.szerBiedr = 30
        self.wysBiedr = 30
        self.spawnX = random.randint(0, 1199)
        self.spawnY = random.randint(0, 799)
        self.speed = 2
        self.direction = direction
        self.kolor = (0, 0, 0) # - kolor tła biedronki
        self.ksztaltBiedronki = pygame.Rect(self.spawnX, self.spawnY, self.szerBiedr, self.wysBiedr)
        self.png = pygame.image.load(os.path.join("png.png"))
        screen.blit(self.png, (600,400))
        
    def draw(self):
        pygame.draw.rect(screen, self.kolor, self.ksztaltBiedronki, 0)
        screen.blit(self.png, (self.spawnX, self.spawnY))

    def move(self):
        self.spawnX = self.spawnX + random.randint(-10,10)
        self.spawnY = self.spawnY + random.randint(-10,10)

#mechanizm odbijania od scian
        if self.spawnX >= 0:
           self.spawnX = self.spawnX - 5
        if self.spawnX <= 1199:
            self.spawnX = self.spawnX + 5
        if self.spawnY >= 0:
           self.spawnY = self.spawnY - 5
        if self.spawnY <= 1199:
            self.spawnY = self.spawnY + 5
         
                        
        self.ksztaltBiedronki = pygame.Rect(self.spawnX, self.spawnY, self.szerBiedr, self.wysBiedr)

    def mouseCollide(self):

        mousePos = pygame.mouse.get_pos()
        bWidth = self.szerBiedr
        bHeight = self.wysBiedr
        bPosX = self.spawnX
        bPosY = self.spawnY
        mousePoint = pygame.draw.circle(screen, (255, 0, 0), (mousePos), 5)
        pointRectCollision = pygame.Rect(bPosX, bPosY, bWidth, bHeight).collidepoint(mousePos)
            
        return pointRectCollision
    
class border():

    def __init__ (self, begin, end):
        self.begin = begin
        self.end = end
        self.color = (255, 0, 0)
        
    def draws(self):
        pygame.draw.line(screen, self.color, self.begin, self.end)

borders.append(border((0, 0),(0, 799)))
borders.append(border((1199, 0),(0, 0)))
borders.append(border((1199, 0),(1199, 799)))
borders.append(border((1199, 799),(0, 799)))

for i in range(iloscBiedr):

    biedronki.append(biedronka(iloscBiedr))
    
while True:
        
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if whatShow != "game":
                    points = 0
                    whatShow = "game"
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))
            
        if whatShow == "menu":
            logo = pygame.image.load(os.path.join("inwazjaBiedronek1200x800.png"))
            screen.blit(logo, (0,0))
            write("INWAZJA BIEDRONEK",506, 70, 30)
            write("Naciśnij spację by zacząć",900, 600, 20)

        elif whatShow == "game":
            for b in biedronki:
                b.move()
                b.draw()
                mC = b.mouseCollide()
                if mC == True:
                    whatShow = ("lose")
            points = points + 1
            score =str(points)
            write(f"WYNIK: {score}" , 100, 100, 35)
            for p in borders:
               p.draws()

        elif whatShow == "lose":
            
            screen.blit(logo, (0,0))
            write("ZJADŁY CIĘ!!!",506, 70, 30)
            write(f"Twój wynik: {score}" ,506, 650, 30)
            write("Naciśnij spację by zacząć od nowa", 880, 600, 20)
            
            
    pygame.display.update()

    

