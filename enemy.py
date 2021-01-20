import position

# As of now there is only one enemy, can be updated
# to have multiple enemies with different properties.
# all the enemy classes will be stored in enemy.py

# TODO remove enemyimage from class as it should be fixed per class.


class MoonVader(position.Position):
    """
    MoonVader type enemy class, extends position.

    Attributes
    ---
    x: x coordinates for enemy object
    y: y coordinates for enemy object
    screen: screen to be displayed on
    enemyImage: image for enemy object

    Methods
    ---
    updateXchange(val): used to update speed for x.
    updateYchange(val): used to update speed for y.

    """

    def __init__(self, x, y, screen, enemyImage):
        super().__init__(x, y, screen, enemyImage)
        self.posychange = 12

    def updateXchange(self, val):
        """Used to update X change"""
        self.posxchange = val

    def updateYchange(self, val):
        """Used to update Y change"""
        # Probably only this would be required!
        self.posychange = val

    def moveEnemy(self):
        # Enemy Move Logic Defined here.
        self.updatePosX(self.posx + self.posxchange)
        self.updatePosY(self.posy + self.posychange)
        if(self.posy < 0):
            self.updateYchange(12)
            self.updatePosX(self.posx - 10)
        if(self.posy > 550):
            self.updateYchange(-12)
            self.updatePosX(self.posx - 10)
