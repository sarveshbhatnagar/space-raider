import position


class Bullet(position.Position):
    def __init__(self,x,y,screen,img):
        super().__init__(x,y, screen, img)

    def moveBullet(self):
        self.updatePosX(self.posx + 15)

    def showBullet(self,screen):
        screen.blit(self.image,(self.posx, self.posy))
    