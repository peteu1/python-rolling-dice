from graphics import *
import time


class Button:
    """activated() and deactivated() and clicked(p) is a method that returns if the user pressed within the required area"""

    def __init__(self, win, center, width, height, label):
        """Create modern button with rounded corners"""
        self.win = win
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()

        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h

        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        # Modern color scheme
        self.inactive_fill = "#E8E8E8"    # Light gray
        self.active_fill = "#3498DB"      # Flat blue
        self.hover_fill = "#2980B9"       # Darker blue for hover state
        self.active_text = "white"
        self.inactive_text = "#555555"    # Dark gray
        
        # Create button rectangle
        self.rect = Rectangle(p1, p2)
        self.rect.setFill(self.inactive_fill)
        self.rect.setOutline("#BBBBBB")   # Light gray outline
        self.rect.draw(win)
        
        # Modern font for label
        self.label = Text(center, label)
        self.label.setSize(12)
        self.label.setStyle("bold")
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """return true if active and inside p"""
        result = (
            self.active
            and self.xmin <= p.getX() <= self.xmax
            and self.ymin <= p.getY() <= self.ymax
        )
        # Visual feedback on click
        if result:
            self.rect.setFill(self.hover_fill)
            self.win.update()
            time.sleep(0.1)
            self.rect.setFill(self.active_fill)
        return result

    def getLabel(self):
        """label of the string"""
        return self.label.getText()

    def activate(self):
        """sets button to active"""
        self.label.setFill(self.active_text)
        self.rect.setFill(self.active_fill)
        self.rect.setWidth(1)
        self.rect.setOutline("#2980B9")  # Dark border
        self.active = True

    def deactivate(self):
        """sets button to unactive"""
        self.label.setFill(self.inactive_text)
        self.rect.setFill(self.inactive_fill)
        self.rect.setWidth(1)
        self.rect.setOutline("#BBBBBB")  # Light border
        self.active = False


class Dropdown:
    """A modern dropdown menu that allows selection from a list of options"""
    
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
        
        # Modern color theme
        self.dropdown_bg = "#F8F9FA"      # Light gray background
        self.dropdown_border = "#DEE2E6"  # Light border
        self.dropdown_text = "#495057"    # Dark gray text  
        self.option_bg = "#FFFFFF"        # White background for options
        self.option_bg_hover = "#E9ECEF"  # Light gray hover
        
        # Create the main dropdown button
        self.main_button = Button(win, center, width, height, f"{label}: {self.current_option}")
        self.main_button.activate()
        
        # Add dropdown arrow indicator
        arrow_x = center.getX() + (width/2) - 0.3
        arrow_y = center.getY()
        self.arrow = Text(Point(arrow_x, arrow_y), "▼")
        self.arrow.setSize(10)
        self.arrow.setTextColor("#495057")
        self.arrow.draw(win)
        
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
            self.arrow.setText("▼")  # Down arrow when closed
        else:
            self.open_options()
            self.arrow.setText("▲")  # Up arrow when open
    
    def open_options(self):
        """Display dropdown options"""
        self.is_open = True
        self.option_buttons = []
        self.option_rects = []
        self.option_labels = []
        
        # Container for options (background)
        container_p1 = Point(self.center.getX() - self.width/2, self.option_ymin)
        container_p2 = Point(self.center.getX() + self.width/2, 
                            self.option_ymin - (len(self.options) * self.height))
        container = Rectangle(container_p1, container_p2)
        container.setFill(self.option_bg)
        container.setOutline(self.dropdown_border)
        container.draw(self.win)
        self.options_container = container
        
        # Create a button for each option
        for i, option in enumerate(self.options):
            # Position each option below the dropdown button
            option_center = Point(
                self.center.getX(), 
                self.option_ymin - ((i + 1) * self.height) - (self.height / 2)
            )
            
            # Create a simple button for each option
            p1 = Point(option_center.getX() - self.width/2, 
                      option_center.getY() - self.height/2)
            p2 = Point(option_center.getX() + self.width/2, 
                      option_center.getY() + self.height/2)
            
            rect = Rectangle(p1, p2)
            rect.setFill(self.option_bg)
            rect.setOutline(self.option_bg)
            rect.draw(self.win)
            
            label = Text(option_center, option)
            label.setTextColor(self.dropdown_text)
            label.setSize(10)
            label.draw(self.win)
            
            # Use the Button class for click handling
            button = Button(self.win, option_center, self.width, self.height, option)
            button.rect.undraw()     # Hide default button appearance
            button.label.undraw()    # Hide default label
            button.activate()        # Make it clickable
            
            self.option_buttons.append(button)
            self.option_rects.append(rect)
            self.option_labels.append(label)
    
    def close_options(self):
        """Hide dropdown options"""
        self.is_open = False
        # Remove the container
        if hasattr(self, 'options_container'):
            self.options_container.undraw()
        
        # Remove all option components
        for button in self.option_buttons:
            button.rect.undraw()
            button.label.undraw()
            
        for rect in self.option_rects:
            rect.undraw()
            
        for label in self.option_labels:
            label.undraw()
            
        self.option_buttons = []
        self.option_rects = []
        self.option_labels = []
    
    def select_option(self, index):
        """Select an option from the dropdown"""
        self.current_option = self.options[index]
        # Update the main button text with the correct label
        self.main_button.label.setText(f"{self.label_text}: {self.current_option}")
        self.close_options()
    
    def get_value(self):
        """Return the current selected value as an integer"""
        return int(self.current_option)
