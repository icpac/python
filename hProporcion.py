
class Tul:
    def puntoRazon(self, x, y, r):
        x1 = (x[0]+ r*y[0]) / (r+1)
        y1 = (x[1]+ r*y[1]) / (r+1)
        return [x1, y1]
    
