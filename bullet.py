import position


class Bullet(position.Position):
    """
    Class file for handling bullet

    Attributes
    ---
    x: position for x coordinates
    y: position for y coordinates
    """

    def __init__(self, x, y, screen, img):
        super().__init__(x, y, screen, img)

    def moveBullet(self):
        """
        Updates bullet +15px in x direction.
        """
        self.updatePosX(self.posx + 15)

    def showBullet(self, screen):
        """
        Displays bullet on screen at position x and y
        """
        screen.blit(self.image, (self.posx, self.posy))
