import pygame; #bring in this module
pygame.init() #get it ready to use
screen =pygame.display.set_mode((900,600)); #create game screen
pygame.display.set_caption("Brazil!") #set screen window title

img1=pygame.transform.smoothscale(pygame.image.load("brazil.jpg").convert_alpha(),(240,180)) #load picture

pygame.mixer.music.load("brazil.ogg"); #load music
pygame.mixer.music.play(-1) #start playing music

font1=pygame.font.SysFont("arial",48,True); #choose font
text1=font1.render("Brazil!",True,(255,255,255)); #say what to print to screen

screen.fill((0,0,0)) #background color for screen

pygame.draw.rect(screen,(0,156,59),(440,40,420,260)) #flag background
pygame.draw.polygon(screen,(255,223,0),[(650,53),(839,170),(650,287),(461,170)]) #diamond shape in flag
pygame.draw.circle(screen,(0,39,118),(650,170),57) #circle in center of flag

screen.blit(img1,(40,360)); #draw jpg 

screen.blit(text1,(40,20)); #draw text

pygame.display.flip() #display all images on screen
