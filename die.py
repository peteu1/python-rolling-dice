from graphics import *

class DieView:
    # shows graphical representation of a multi-sided dice with modern styling
    def __init__(self, win, center, size):
        # create a modern view of the die
        self.win = win
        self.is_hidden = False    # Flag to track visibility
        
        # Modern color scheme
        self.background = "#FFFFFF"     # White face
        self.border = "#CCCCCC"         # Light gray border
        self.foreground = "#333333"     # Dark gray pips
        self.highlight = "#F8F9FA"      # Highlight for 3D effect
        self.shadow = "#E9ECEF"         # Shadow for 3D effect
        
        self.psize = 0.1 * size        # radius of each pip
        hsize = size / 2.0             # half size of die
        offset = 0.6 * hsize           # distance from center to other pips
        cx, cy = center.getX(), center.getY()
        
        # Create rounded rectangle for die face
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill(self.background)
        self.rect.setOutline(self.border)
        self.rect.setWidth(2)
        self.rect.draw(win)
        
        # Create underlying shadow for 3D effect
        shadow_offset = 0.05 * size
        p1s = Point(cx - hsize + shadow_offset, cy - hsize - shadow_offset)
        p2s = Point(cx + hsize + shadow_offset, cy + hsize - shadow_offset)
        self.shadow_rect = Rectangle(p1s, p2s)
        self.shadow_rect.setFill(self.shadow)
        self.shadow_rect.setOutline(self.shadow)
        self.shadow_rect.draw(win)
        self.rect.undraw()
        self.rect.draw(win)  # Redraw on top of shadow

        # create 7 circles for pips
        self.pip1 = self.__makePip(cx - offset, cy - offset)
        self.pip2 = self.__makePip(cx - offset, cy)
        self.pip3 = self.__makePip(cx - offset, cy + offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx + offset, cy - offset)
        self.pip6 = self.__makePip(cx + offset, cy)
        self.pip7 = self.__makePip(cx + offset, cy + offset)

        # Add text for display of larger numbers
        self.value_text = Text(Point(cx, cy), "")
        self.value_text.setSize(18)
        self.value_text.setStyle("bold")
        self.value_text.setTextColor(self.foreground)
        self.value_text.draw(win)
        
        # draw an initial value
        self.setValue(1)

    def __makePip(self, x, y):
        # Internal helper method to draw a pip at (x,y)
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        # set this to display value
        # turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)
        self.value_text.setText("")  # Clear any existing text

        # For values 1-6, show standard pip patterns
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 6:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            # For values > 6, display the number as text
            self.value_text.setText(str(value))

    def hide(self):
        """Hide the die by making it invisible"""
        if not self.is_hidden:
            self.shadow_rect.undraw()
            self.rect.undraw()
            self.pip1.undraw()
            self.pip2.undraw()
            self.pip3.undraw()
            self.pip4.undraw()
            self.pip5.undraw()
            self.pip6.undraw()
            self.pip7.undraw()
            self.value_text.undraw()
            self.is_hidden = True
    
    def show(self):
        """Show the die if it's currently hidden"""
        if self.is_hidden:
            self.shadow_rect.draw(self.win)
            self.rect.draw(self.win)
            self.pip1.draw(self.win)
            self.pip2.draw(self.win)
            self.pip3.draw(self.win)
            self.pip4.draw(self.win)
            self.pip5.draw(self.win)
            self.pip6.draw(self.win)
            self.pip7.draw(self.win)
            self.value_text.draw(self.win)
            self.is_hidden = False
            # Refresh the display of the pips
            self.setValue(1)
