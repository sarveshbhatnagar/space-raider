import bullet

class Player:
    xchange, ychange = 0, 0
    def __init__(self,x,y,screen,playerImg):
        self.x = x
        self.y = y
        self.screen = screen
        self.playerImg = playerImg
        self.bulletstate = False
    
    def playercontrol(self,):
        """
        Used to display player object to the screen
        """
        self.screen.blit(self.playerImg,(self.x, self.y))

    def updateXchange(self,val):
        """Used to update X change"""
        self.xchange = val
    
    def updateYchange(self, val):
        """Used to update Y change"""
        self.ychange = val

    def updateX(self):
        self.x += self.xchange
        if(self.x > 750):
            print('Greater')
            self.x = 750
            self.updateXchange(0)
        elif(self.x <0):
            self.x = 0
            self.updateXchange(0)
    
    def updateY(self):
        self.y += self.ychange
        if (self.y > 550):
            self.y = 550
            self.updateYchange(0)
        elif(self.y < 0):
            self.y = 0
            self.updateYchange(0)

    def createBullet(self,img):
        self.bobj = bullet.Bullet(self.x,self.y, self.screen,img)
        self.bulletstate = True

    def fireBullet(self):
        self.bobj.moveBullet()
        self.bobj.showBullet(self.screen)
        

