import pygame,sys,os
os.environ["SDL_VIDEODRIVER"]="windib"



class backgroundimage(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
    


class myballclass(pygame.sprite.Sprite):
    def __init__(self,image_file,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
        self.speed=speed

    def move(self):
        global points,score_text,points_music,walls_hit
        self.rect=self.rect.move(self.speed)

        if self.rect.left <= 1 or self.rect.right >= screen.get_width()- 10:
            walls_hit.play()
            self.speed[0]=-self.speed[0]
            

        if self.rect.top <=0:
            points_music.play() 
            self.speed[1]=-self.speed[1]
            points=points+1   
            score_text = font.render(str(points),1,(0,0,0))
           

        
            
          

class mypaddle(pygame.sprite.Sprite):
    def __init__(self,location=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface=pygame.surface.Surface([100,20])
        image_surface.fill([250,200,0])
        self.image=image_surface.convert()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location

        

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([640,480])
pygame.time.delay(1000)
adolf=backgroundimage("gunngirl.jpg",[0,400])
clock=pygame.time.Clock()
ball_speed=[20,10]
myball=myballclass("littleball.png",[100,50],ball_speed)
ballGroup=pygame.sprite.Group(myball)
paddle=mypaddle([270,400])
another_paddle=mypaddle([500,200])
paddle1=mypaddle([100,100])

pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

points_music=pygame.mixer.Sound("get_point.wav")
points_music.set_volume(0.2)

paddle_music=pygame.mixer.Sound("hit_paddle.wav")
paddle_music.set_volume(0.4)

walls_hit=pygame.mixer.Sound("hit_wall.wav")
walls_hit.set_volume(0.3)

new_life=pygame.mixer.Sound("new_life.wav")
new_life.set_volume(0.5)

splat=pygame.mixer.Sound("splat.wav")
splat.set_volume(0.4)

game_over=pygame.mixer.Sound("game_over.wav")
game_over.set_volume(1)

points = 0
font= pygame.font.Font(None,50)
score_text = font.render(str(points),1,(0,0,0))
textpos =[10,10]

lives=3
done=False



while 1:
    clock.tick(20)
    screen.fill([255,255,255])

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEMOTION:
            paddle.rect.centerx=event.pos[0]

    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        paddle_music.play()
        myball.speed[1]= -myball.speed[1]       
    myball.move()

    
    if pygame.sprite.spritecollide(another_paddle, ballGroup, False):
        paddle_music.play()
        myball.speed[1]= -myball.speed[1]       
    myball.move()
	
    if pygame.sprite.spritecollide(paddle1, ballGroup, False):
        paddle_music.play()
        myball.speed[1]= -myball.speed[1]       
    myball.move()



    if not done:
        screen.blit(adolf.image,[20,20])
        screen.blit(another_paddle.image,another_paddle.rect)
        screen.blit(paddle1.image,paddle1.rect)
        screen.blit(myball.image,myball.rect)
        screen.blit(paddle.image,paddle.rect)
        screen.blit(score_text,textpos)    
        for i in range(lives):
            screen.blit(myball.image,[640-40*i,20])
        pygame.display.flip()
    
    if myball.rect.bottom >= screen.get_height():     
            lives=lives-1
            
            if lives==0:
                pygame.mixer.music.fadeout(2000)
                points_music.set_volume(0)
                paddle_music.set_volume(0)
                walls_hit.set_volume(0)
                new_life.set_volume(0)
                splat.set_volume(0)
                ball_speed=[0,0]
                game_over.play()
                ft1="Game Over"
                ft2="Your Final Score is "+ str(points)
                ft1_font=pygame.font.Font(None,70)
                ft2_font=pygame.font.Font(None,60)
                ft1_surface=font.render(str(ft1),1,(0,0,0))
                ft2_surface=font.render(str(ft2),1,(0,0,0))
                screen.blit(ft1_surface,[screen.get_width()/2 - ft1_surface.get_width()/2,100])
                screen.blit(ft2_surface,[screen.get_width()/2 - ft1_surface.get_width()/2,200])
                pygame.time.delay(2000)
                pygame.display.flip()
                done=True
        
            else:
                splat.play() 
                pygame.time.delay(2000)
                new_life.play()
                myball.rect.topleft=[50,50]
            
            

         
    
