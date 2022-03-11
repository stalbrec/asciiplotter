import shutil
import numpy as np
from skimage.draw import line #fast bresenham implementation
__all__ = [
    '__version__'
    'Canvas'
]



class Canvas(object):
    def __init__(self,height=10,width=None):
        self._height = height
        self._width = shutil.get_terminal_size().columns if width is None else width

        self._rows = np.empty([self._height,self._width],dtype = "<U10")
        self._rows.fill(' ')
        
    def fill(self,char='#'):
        self._rows[:,:] = char

    def line(self,x1,y1,x2,y2,char='.'):
        y,x = line(y1,x1,y2,x2)
        self._rows[y,x] = char
            
    def point(self,x,y,char):
        self._rows[y,x] = char

    def rectangle(self,x1,y1,x2,y2,char='.'):
        self.line(x1,y1,x2,y1,char)
        self.line(x2,y1,x2,y2,char)
        self.line(x2,y2,x1,y2,char)
        self.line(x1,y2,x1,y1,char)

    def text(self,x,y,text):
        x_ = np.array(range(len(text)))+x
        self._rows[y,x_] = list(text)
        
    def __str__(self):
        return "\n".join("".join(l for l in row) for row in self._rows)
