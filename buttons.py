from graphics import *


class Button:
    """activated() and deactivated() and clicked(p) is a method that returns if the user pressed within the required area"""

    def __init__(self, win, center, width, height, label):
        """Create rectangular button e.g qb=Button(myWin,centerPoint,width,height,'Quit')"""
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()

        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h

        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgrey")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """return true if active and inside p"""
        return (
            self.active
            and self.xmin <= p.getX() <= self.xmax
            and self.ymin <= p.getY() <= self.ymax
        )  # use return when you change an already set variable/variables

    def getLabel(self):
        """label of the string"""
        return self.label.getText()  # here as well

    def activate(self):
        """sets button to active"""
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """sets button to unactive"""
        self.label.setFill("darkgray")
        self.rect.setWidth(1)
        self.active = False


class Dropdown:
    """A dropdown menu that allows selection from a list of options"""
    
    def __init__(self, win, center, width, height, options, label=""):
        """Create a dropdown with options
        Parameters:
            win: the GraphWin to draw on
            center: Point for the center of the dropdown
            width, height: dimensions of the dropdown
            options: list of strings for the dropdown options
            label: optional label to display above the dropdown
        """
        self.win = win
        self.options = options
        self.current_option = options[0]
        self.is_open = False
        self.option_buttons = []
        self.label_text = label
        
        # Create the main dropdown button
        self.main_button = Button(win, center, width, height, f"{label}: {self.current_option}")
        self.main_button.activate()
        
        # Save dimensions for option buttons
        self.width = width
        self.height = height
        self.center = center
        
        # Save dimensions for the option buttons that will appear when clicked
        self.option_ymin = center.getY() + height/2.0
        
    def clicked(self, p):
        """Check if dropdown is clicked and handle the action"""
        # Check if main dropdown button is clicked
        if self.main_button.clicked(p):
            self.toggle_options()
            return True
            
        # If dropdown is open, check if any option is clicked
        if self.is_open:
            for i, button in enumerate(self.option_buttons):
                if button.clicked(p):
                    self.select_option(i)
                    return True
                    
        return False
        
    def toggle_options(self):
        """Toggle showing/hiding the dropdown options"""
        if self.is_open:
            self.close_options()
        else:
            self.open_options()
    
    def open_options(self):
        """Display dropdown options"""
        self.is_open = True
        self.option_buttons = []
        
        # Create a button for each option
        for i, option in enumerate(self.options):
            # Position each option below the dropdown button
            option_center = Point(
                self.center.getX(), 
                self.option_ymin - (i * self.height) - (self.height / 2)
            )
            
            button = Button(self.win, option_center, self.width, self.height, option)
            button.activate()
            self.option_buttons.append(button)
    
    def close_options(self):
        """Hide dropdown options"""
        self.is_open = False
        for button in self.option_buttons:
            # Undraw all components of the button
            button.rect.undraw()
            button.label.undraw()
        self.option_buttons = []
    
    def select_option(self, index):
        """Select an option from the dropdown"""
        self.current_option = self.options[index]
        # Update the main button text with the correct label
        self.main_button.label.setText(f"{self.label_text}: {self.current_option}")
        self.close_options()
    
    def get_value(self):
        """Return the current selected value as an integer"""
        return int(self.current_option)