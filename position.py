class Position:
    def __init__(self,x,y,screen,image):
        self.posx = x
        self.posy = y
        self.screen = screen
        self.image = image
        self.posxchange = 0
        self.posychange = 0

    def updatePosX(self,val):
        """Update X Position"""
        self.posx = val
    
    def updatePosY(self, val):
        """Update Y Position"""
        self.posy = val
    
    def display(self,):
        """
        Used to display object to the screen
        """
        self.screen.blit(self.image,(self.posx, self.posy))