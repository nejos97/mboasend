class URL:
    def __init__(self, origin, mask):
        self.origin = origin
        self.mask = mask

    def getOrigin(self):
        return self.origin

    def getMask(self):
        return self.mask

    def setOrigin(self, newOrigin):
        self.origin = newOrigin

    def setMask(self, newMask):
        self.mask = newMask
    def __str__(self):
        return "{} pointe vers =  {}".format(self.mask,self.origin)
