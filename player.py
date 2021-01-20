import bullet


class Player:
    """
    A class for handling Player interface.

    Attributes
    ---
    x: x coordinates for Player
    y: y coordinates for Player
    screen: Screen where player should be displayed
    playerImg: Player image

    Methods
    ---
    playercontrol() : displays player object to screen.
    updateXchange(val) : updates xchange of player.
    updateYchange(val) : updates ychange of player.
    updateX() : updates X coordinates for player.
    updateY() : updates Y coordinates for player.

    """
    xchange, ychange = 0, 0

    def __init__(self, x, y, screen, playerImg):
        self.x = x
        self.y = y
        self.screen = screen
        self.playerImg = playerImg
        self.bulletstate = False

    def playercontrol(self,):
        """
        Used to display player object to the screen
        """
        self.screen.blit(self.playerImg, (self.x, self.y))

    def updateXchange(self, val):
        """Used to update X change"""
        self.xchange = val

    def updateYchange(self, val):
        """Used to update Y change"""
        self.ychange = val

    def updateX(self):
        """
        Updates X coordinates of player.
        """
        self.x += self.xchange
        if(self.x > 750):
            print('Greater')
            self.x = 750
            self.updateXchange(0)
        elif(self.x < 0):
            self.x = 0
            self.updateXchange(0)

    def updateY(self):
        """
        updates y coordinates of player.
        """
        self.y += self.ychange
        if (self.y > 550):
            self.y = 550
            self.updateYchange(0)
        elif(self.y < 0):
            self.y = 0
            self.updateYchange(0)

    def createBullet(self, img):
        """
        creates a bullet object for player and sets bullet state to true

        params
        ---
        img: bullet image that is to be displayed on the screen.
        """
        self.bobj = bullet.Bullet(self.x, self.y, self.screen, img)
        self.bulletstate = True

    def fireBullet(self):
        """
        responsible for showing bullet and moving bullet on the screen
        """
        self.bobj.moveBullet()
        self.bobj.showBullet(self.screen)
