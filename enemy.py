import position

class MoonVader(position.Position):
    def __init__(self,x,y,screen,enemyImage):
        super().__init__(x,y,screen, enemyImage)
        self.posychange = 12
    
    def updateXchange(self,val):
        """Used to update X change"""
        self.posxchange = val
    
    def updateYchange(self, val):
        """Used to update Y change"""
        #Probably only this would be required!
        self.posychange = val

    def moveEnemy(self):
        # Enemy Move Logic Defined here.
        self.updatePosX(self.posx + self.posxchange)
        self.updatePosY(self.posy + self.posychange)
        if(self.posy<0):
            self.updateYchange(12)
            self.updatePosX(self.posx - 10)
        if(self.posy>550):
            self.updateYchange(-12)
            self.updatePosX(self.posx - 10)

    
    
        