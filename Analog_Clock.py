import pygame
import math
import datetime

pygame.init()

display = pygame.display.set_mode((800,800))
pygame.display.set_caption("Analog Clock")

clock = pygame.time.Clock()
FPS = 50

def print_text(text,position):
    font = pygame.font.SysFont("Times New Roman",40,True,False)
    surface = font.render(text,True,(0,0,0))
    display.blit(surface,position)

def convert_degrees_to_xy(radius, theta):
    x = math.sin(2*math.pi*theta/360)*radius
    y = math.cos(2*math.pi*theta/360)*radius

    return x+400-15, -(y-400)-15

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        current_time = datetime.datetime.now()

        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        display.fill((255,255,255))
        pygame.draw.circle(display, (0,0,0), (400,400),400,4)

        for num in range(1,13):
            print_text(str(num),convert_degrees_to_xy(350,num*30))

        #Minute Hand - Longest one
        radius = 350
        theta = (minute + (second/60))*(360/60)
        pygame.draw.line(display,(0,0,0),(400,400),convert_degrees_to_xy(radius,theta),3)

        #Second Hand - Medium length one
        radius = 300
        theta = second*(360/60)
        pygame.draw.line(display,(255,0,0),(400,400),convert_degrees_to_xy(radius,theta),3)

        #Hour Hand - Shortest one
        radius = 200
        theta = (hour + (minute/60) + (second/3600))*(360/60)
        pygame.draw.line(display,(0,0,0),(400,400),convert_degrees_to_xy(radius,theta),3)
        
        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit()
