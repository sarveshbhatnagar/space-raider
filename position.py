class Position:
    """
    Position class for position handling tasks of different
    objects.

    Attributes
    ---
    x: x coordinates
    y: y coordinates
    screen: screen to be displayed on
    image: object to be displayed

    Methods
    ---
    updatePosX(val): used to update x coordinates
    updatePosY(val): used to update y coordinates
    display(): used to display the object
    """

    def __init__(self, x, y, screen, image):
        self.posx = x
        self.posy = y
        self.screen = screen
        self.image = image
        self.posxchange = 0
        self.posychange = 0

    def updatePosX(self, val):
        """Update X Position"""
        self.posx = val

    def updatePosY(self, val):
        """Update Y Position"""
        self.posy = val

    def display(self,):
        """
        Used to display object to the screen
        """
        self.screen.blit(self.image, (self.posx, self.posy))
