class scraper:

    def __init__(self, au):
        self.autoit = au

    #Tower focus = 11209740
    def searchPixel(self, left, top, right, bottom, color):
        self.autoit.PixelSearch(left, top, right, bottom, color)
        if self.autoit.error == 1:
            return False
        else:
            return True
